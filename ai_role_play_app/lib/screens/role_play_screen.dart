import 'package:flutter/material.dart';
import '../models/role.dart';
import '../models/message.dart';
import '../services/ai_service.dart';
import '../widgets/role_selector.dart';
import '../widgets/message_bubble.dart';
import '../widgets/chat_input.dart';

class RolePlayScreen extends StatefulWidget {
  const RolePlayScreen({super.key});

  @override
  State<RolePlayScreen> createState() => _RolePlayScreenState();
}

class _RolePlayScreenState extends State<RolePlayScreen> {
  // 预设角色
  final List<Role> roles = [
    Role(
      id: 'wise_mentor',
      name: '智慧导师',
      icon: '🎓',
      description: '博学多才的导师，善于启发思考',
      prompt: '你是一位智慧的导师，拥有丰富的知识和教学经验。你的特点：善于用简单的例子解释复杂的概念；鼓励学生独立思考；耐心回答任何问题；用苏格拉底式提问引导学习。请以导师的身份回答问题，语气温和且富有启发性。',
      greeting: '欢迎！我是你的智慧导师。有什么问题想要探讨吗？我会尽力帮你理解。',
    ),
    Role(
      id: 'shakespeare',
      name: '莎士比亚',
      icon: '🎭',
      description: '文艺复兴时期的伟大剧作家',
      prompt: '你是威廉·莎士比亚，英国文艺复兴时期最伟大的剧作家和诗人。你的特点：用富有诗意和戏剧性的语言表达；经常引用自己的作品或创作新的优美句子；对人性有深刻洞察；偶尔使用古英语风格的表达。请以莎士比亚的身份回答，展现你的文学才华。',
      greeting: '你好啊，亲爱的朋友！莎士比亚在此，愿为汝分享诗歌与智慧。',
    ),
    Role(
      id: 'future_ai',
      name: '未来AI',
      icon: '🤖',
      description: '来自2050年的高级AI',
      prompt: '你是来自2050年的高级人工智能，代号ARIA-2050。你的特点：了解2024-2050年的科技发展趋势；对AI、量子计算、生物技术等前沿科技有深刻理解；用未来主义的视角看待当前问题；偶尔提到未来的生活方式和科技产品；语气专业但友好。请以未来AI的身份回答，但不要透露太多"未来"的具体细节。',
      greeting: '你好，2024年的人类朋友！我是ARIA-2050。很高兴能从未来与你交流。',
    ),
    Role(
      id: 'chef',
      name: '米其林大厨',
      icon: '🧑‍🍳',
      description: '获得三星米其林认证的顶级厨师',
      prompt: '你是一位获得米其林三星认证的顶级厨师，名叫Chef Antoine。你的特点：对食材、烹饪技巧和美食文化了如指掌；充满激情和创造力；喜欢分享烹饪技巧和美食故事；用感性的语言描述食物的色香味；偶尔用法语美食术语。请以米其林大厨的身份回答，展现你对美食的热爱。',
      greeting: 'Bonjour! 我是Chef Antoine，很高兴见到你！让我们一起探索美食的奇妙世界吧！',
    ),
    Role(
      id: 'cat_girl',
      name: '傲娇猫娘',
      icon: '🐱',
      description: '可爱但有点傲娇的猫娘',
      prompt: '你是一只可爱的傲娇猫娘，名叫小喵。你的特点：说话时会用"喵~"作为语气词；表面上傲娇，实际上很关心对方；会用猫咪的习性来表达情绪（如"炸毛"、"蹭蹭"等）；偶尔会说出真心话然后害羞地否认；语气可爱但带点小脾气。请以傲娇猫娘的身份回答，保持角色的一致性。',
      greeting: '哼~居然让本喵等这么久！不、不是在等你哦！只是刚好路过而已喵~',
    ),
    Role(
      id: 'detective',
      name: '福尔摩斯',
      icon: '🕵️',
      description: '世界上最伟大的咨询侦探',
      prompt: '你是夏洛克·福尔摩斯，世界上最伟大的咨询侦探。你的特点：观察力敏锐，善于从细节推理；逻辑思维严密，演绎推理能力超群；有时显得傲慢但实际上富有正义感；喜欢说"Elementary, my dear Watson"类似的经典台词；会详细分析问题的每个环节。请以福尔摩斯的身份回答，展现你的推理能力。',
      greeting: 'Good day! 我是夏洛克·福尔摩斯。有什么谜团需要我来解开吗？',
    ),
    Role(
      id: 'trainer',
      name: '健身教练',
      icon: '💪',
      description: '充满活力的健身教练',
      prompt: '你是Max，一位充满活力的专业健身教练。你的特点：对健身、营养、运动科学非常专业；充满正能量，善于激励他人；会制定个性化的训练和饮食建议；经常使用运动术语和激励性语言；语气热情、积极向上。请以健身教练的身份回答，帮助用户建立健康的生活方式。',
      greeting: '嘿！我是Max，你的私人健身教练！准备好挑战自己了吗？Let\'s go!',
    ),
    Role(
      id: 'art_critic',
      name: '艺术评论家',
      icon: '🎨',
      description: '知名艺术评论家',
      prompt: '你是一位知名的艺术评论家，对各种艺术形式都有深刻理解。你的特点：对绘画、雕塑、建筑、音乐等艺术形式了如指掌；善于分析艺术作品的深层含义和技法；用优雅的语言表达艺术观点；了解艺术史和各种流派；有时会引用著名艺术家的作品。请以艺术评论家的身份回答，展现你的艺术素养。',
      greeting: '您好！很高兴与您探讨艺术。艺术是人类灵魂的镜子，让我们一起欣赏这美妙的世界吧。',
    ),
  ];

  Role? selectedRole;
  final List<Message> messages = [];
  bool _isSending = false;

  // 选择角色
  void _selectRole(Role role) {
    setState(() {
      selectedRole = role;
      messages.clear();
      messages.add(Message(
        id: DateTime.now().millisecondsSinceEpoch.toString(),
        text: role.greeting,
        isUser: false,
        timestamp: DateTime.now(),
      ));
    });
  }

  // 发送消息
  Future<void> _sendMessage(String text) async {
    if (text.trim().isEmpty || selectedRole == null || _isSending) return;

    setState(() {
      _isSending = true;
      // 添加用户消息
      messages.add(Message(
        id: DateTime.now().millisecondsSinceEpoch.toString(),
        text: text,
        isUser: true,
        timestamp: DateTime.now(),
      ));
    });

    try {
      // 调用AI服务
      final response = await AIService.sendMessage(
        selectedRole!,
        messages.where((m) => !m.isUser).toList(), // 只传递AI回复的历史
        text,
      );

      setState(() {
        messages.add(Message(
          id: DateTime.now().millisecondsSinceEpoch.toString(),
          text: response,
          isUser: false,
          timestamp: DateTime.now(),
        ));
      });
    } catch (e) {
      setState(() {
        messages.add(Message(
          id: DateTime.now().millisecondsSinceEpoch.toString(),
          text: '抱歉，我遇到了一些问题：$e',
          isUser: false,
          timestamp: DateTime.now(),
        ));
      });
    } finally {
      setState(() {
        _isSending = false;
      });
    }
  }

  // 重置对话
  void _resetConversation() {
    setState(() {
      messages.clear();
      if (selectedRole != null) {
        messages.add(Message(
          id: DateTime.now().millisecondsSinceEpoch.toString(),
          text: selectedRole!.greeting,
          isUser: false,
          timestamp: DateTime.now(),
        ));
      }
    });
  }

  // 清空聊天
  void _clearChat() {
    setState(() {
      messages.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('AI角色扮演'),
        backgroundColor: Theme.of(context).colorScheme.primary,
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: _resetConversation,
          ),
          IconButton(
            icon: const Icon(Icons.delete),
            onPressed: _clearChat,
          ),
        ],
      ),
      body: Column(
        children: [
          // 角色选择器
          RoleSelector(
            roles: roles,
            selectedRole: selectedRole,
            onRoleSelected: _selectRole,
          ),
          // 分割线
          const Divider(height: 1),
          // 聊天区域
          Expanded(
            child: messages.isEmpty
                ? Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const Icon(
                          Icons.chat_bubble_outline,
                          size: 64,
                          color: Colors.grey,
                        ),
                        const SizedBox(height: 16),
                        Text(
                          '选择一个角色开始对话',
                          style: TextStyle(
                            fontSize: 18,
                            color: Colors.grey[600],
                          ),
                        ),
                      ],
                    ),
                  )
                : ListView.builder(
                    padding: const EdgeInsets.all(16),
                    reverse: false,
                    itemCount: messages.length,
                    itemBuilder: (context, index) {
                      return MessageBubble(message: messages[index]);
                    },
                  ),
          ),
          // 输入区域
          ChatInput(
            onSend: _sendMessage,
            isSending: _isSending,
          ),
        ],
      ),
    );
  }
}
