import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'screens/role_play_screen.dart';

void main() async {
  // 尝试加载 .env 文件（如果存在）
  // 在生产环境中，API Key 应该通过其他方式获取
  try {
    // 尝试多个可能的路径
    bool loaded = false;
    
    // 尝试 1: 直接路径 .env
    try {
      await dotenv.load(fileName: ".env");
      debugPrint('✅ .env file loaded successfully from .env');
      loaded = true;
    } catch (e1) {
      debugPrint('📝 Trying alternative path...');
      
      // 尝试 2: 相对路径 ai_role_play_app/.env
      try {
        await dotenv.load(fileName: "ai_role_play_app/.env");
        debugPrint('✅ .env file loaded successfully from ai_role_play_app/.env');
        loaded = true;
      } catch (e2) {
        debugPrint('📝 Trying with assets path...');
        
        // 尝试 3: 使用 assets 路径
        try {
          await dotenv.load(fileName: "assets/.env");
          debugPrint('✅ .env file loaded successfully from assets/.env');
          loaded = true;
        } catch (e3) {
          // 所有尝试都失败
          if (!loaded) {
            debugPrint('⚠️ Warning: .env file not found in any expected location');
            debugPrint('Tried paths: .env, ai_role_play_app/.env, assets/.env');
          }
        }
      }
    }
    
    // 检查是否成功加载了 API Key
    _checkApiKeys();
  } catch (e) {
    debugPrint('❌ Error loading .env file: $e');
  }
  
  runApp(const MyApp());
}

// 检查所有 API Key 是否已加载
void _checkApiKeys() {
  debugPrint('🔍 Checking API Keys...');
  
  final keys = {
    'SILICONFLOW_API_KEY': dotenv.env['SILICONFLOW_API_KEY'],
    'OPENAI_API_KEY': dotenv.env['OPENAI_API_KEY'],
    'ZHIPU_API_KEY': dotenv.env['ZHIPU_API_KEY'],
  };
  
  for (final entry in keys.entries) {
    if (entry.value != null && entry.value!.isNotEmpty) {
      final masked = entry.value!.length > 10
          ? '${entry.value!.substring(0, 10)}...'
          : entry.value!;
      debugPrint('✅ ${entry.key}: $masked');
    } else {
      debugPrint('⚠️ ${entry.key}: NOT SET');
    }
  }
  
  debugPrint('📝 提示：应用完全依赖用户输入的 API Key');
  debugPrint('📝 请在应用启动后点击钥匙图标输入 API Key');
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '虚拟角色聊天',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.blue,
          brightness: Brightness.light,
        ),
      ),
      home: const RolePlayScreen(),
    );
  }
}
