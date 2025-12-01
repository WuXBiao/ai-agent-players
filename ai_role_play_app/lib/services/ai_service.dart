import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:flutter_dotenv/flutter_dotenv.dart';
import '../models/role.dart';
import '../models/message.dart';
import '../utils/api_key_manager.dart';

class AIService {
  static const String _openaiBaseUrl = 'https://api.openai.com/v1/chat/completions';
  static const String _zhipuBaseUrl = 'https://open.bigmodel.cn/api/paas/v4/chat/completions';
  static const String _siliconflowBaseUrl = 'https://api.siliconflow.cn/v1/chat/completions';

  // 获取API密钥（从内存或 .env 获取）
  static String? _getApiKey(String provider) {
    final apiKey = APIKeyManager.getAPIKey(provider);
    
    if (apiKey != null && apiKey.isNotEmpty) {
      debugPrint('✅ API Key found for provider: $provider');
      return apiKey;
    }
    
    debugPrint('❌ API Key NOT found for provider: $provider');
    return null;
  }

  // 构建消息历史
  static List<Map<String, dynamic>> _buildMessages(String prompt, List<Message> history, String userMessage) {
    final messages = <Map<String, dynamic>>[
      {'role': 'system', 'content': prompt},
    ];

    for (final msg in history) {
      messages.add({
        'role': msg.isUser ? 'user' : 'assistant',
        'content': msg.text,
      });
    }

    messages.add({
      'role': 'user',
      'content': userMessage,
    });

    return messages;
  }

  // 发送请求到AI
  static Future<String> sendMessage(Role role, List<Message> history, String userMessage, {String provider = 'siliconflow'}) async {
    debugPrint('📤 Sending message to AI provider: $provider');
    
    final apiKey = _getApiKey(provider);
    if (apiKey == null || apiKey.isEmpty) {
      debugPrint('❌ Error: API Key is missing for provider: $provider');
      throw Exception('API密钥未配置: $provider');
    }

    final url = _getUrl(provider);
    final headers = _getHeaders(provider, apiKey);
    final messages = _buildMessages(role.prompt, history, userMessage);
    final body = _buildRequestBody(provider, messages);

    try {
      debugPrint('📡 Making request to: $url');
      final response = await http.post(
        Uri.parse(url),
        headers: headers,
        body: jsonEncode(body),
      ).timeout(
        const Duration(seconds: 30),
        onTimeout: () => throw Exception('请求超时'),
      );

      if (response.statusCode == 200) {
        debugPrint('✅ Response received successfully');
        final data = jsonDecode(response.body);
        return _extractResponseContent(data, provider);
      } else {
        debugPrint('❌ API Error: ${response.statusCode}');
        debugPrint('Response body: ${response.body}');
        throw Exception('API请求失败: ${response.statusCode} - ${response.body}');
      }
    } catch (e) {
      debugPrint('❌ Network error: $e');
      throw Exception('网络请求错误: $e');
    }
  }

  // 获取URL
  static String _getUrl(String provider) {
    switch (provider) {
      case 'openai':
        return _openaiBaseUrl;
      case 'zhipu':
        return _zhipuBaseUrl;
      case 'siliconflow':
        return _siliconflowBaseUrl;
      default:
        return _siliconflowBaseUrl;
    }
  }

  // 获取请求头
  static Map<String, String> _getHeaders(String provider, String apiKey) {
    switch (provider) {
      case 'openai':
        return {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer $apiKey',
        };
      case 'zhipu':
      case 'siliconflow':
        return {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer $apiKey',
        };
      default:
        return {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer $apiKey',
        };
    }
  }

  // 构建请求体
  static Map<String, dynamic> _buildRequestBody(String provider, List<Map<String, dynamic>> messages) {
    switch (provider) {
      case 'openai':
        return {
          'model': 'gpt-3.5-turbo',
          'messages': messages,
          'temperature': 0.9,
        };
      case 'zhipu':
        return {
          'model': 'glm-4-flash',
          'messages': messages,
          'temperature': 0.9,
        };
      case 'siliconflow':
        return {
          'model': 'Qwen/Qwen2.5-7B-Instruct',
          'messages': messages,
          'temperature': 0.9,
        };
      default:
        return {
          'model': 'Qwen/Qwen2.5-7B-Instruct',
          'messages': messages,
          'temperature': 0.9,
        };
    }
  }

  // 提取响应内容
  static String _extractResponseContent(dynamic data, String provider) {
    try {
      switch (provider) {
        case 'openai':
        case 'zhipu':
        case 'siliconflow':
          return data['choices'][0]['message']['content'] as String;
        default:
          return data['choices'][0]['message']['content'] as String;
      }
    } catch (e) {
      throw Exception('解析响应失败: $e');
    }
  }
}
