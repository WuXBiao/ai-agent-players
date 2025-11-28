import 'package:flutter/material.dart';

/// 自定义emoji图标小部件 - 使用Flutter内置图标替代emoji
class CustomEmojiIcon extends StatelessWidget {
  final String emoji;
  final double size;
  final Color? color;

  const CustomEmojiIcon({
    super.key,
    required this.emoji,
    this.size = 24,
    this.color,
  });

  /// 根据emoji返回对应的Flutter图标
  IconData _getIconData() {
    switch (emoji) {
      case '🎭':
        return Icons.theater_comedy; // 剧院面具
      case '🤖':
        return Icons.smart_toy; // 机器人
      case '👤':
        return Icons.person; // 用户
      case '😊':
        return Icons.sentiment_very_satisfied; // 微笑
      case '✨':
        return Icons.star; // 闪闪发光（用星星表示）
      case '⭐':
        return Icons.star; // 星星
      default:
        return Icons.theater_comedy;
    }
  }

  /// 获取emoji对应的颜色
  Color _getColor() {
    if (color != null) return color!;
    
    switch (emoji) {
      case '🎭':
        return Colors.purple.shade400; // 紫色
      case '🤖':
        return Colors.orange.shade400; // 橙色
      case '👤':
        return Colors.blue.shade400; // 蓝色
      case '😊':
        return Colors.yellow.shade600; // 黄色
      case '✨':
        return Colors.yellow.shade400; // 黄色
      case '⭐':
        return Colors.amber.shade400; // 琥珀色
      default:
        return Colors.grey;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Icon(
      _getIconData(),
      size: size,
      color: _getColor(),
    );
  }
}

/// 简化版本 - 直接返回Icon小部件
class EmojiIcon extends StatelessWidget {
  final String emoji;
  final double size;
  final Color? color;

  const EmojiIcon({
    super.key,
    required this.emoji,
    this.size = 24,
    this.color,
  });

  @override
  Widget build(BuildContext context) {
    return CustomEmojiIcon(
      emoji: emoji,
      size: size,
      color: color,
    );
  }
}
