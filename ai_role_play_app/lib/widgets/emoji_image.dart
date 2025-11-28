import 'package:flutter/material.dart';

/// 将emoji替换为图片的小部件
class EmojiImage extends StatelessWidget {
  final String emoji;
  final double size;
  final Color? color;

  const EmojiImage({
    super.key,
    required this.emoji,
    this.size = 24,
    this.color,
  });

  /// 获取emoji对应的图片路径
  String _getImagePath() {
    switch (emoji) {
      case '🎭':
        return 'assets/icons/mask.png';
      case '🤖':
        return 'assets/icons/robot.png';
      case '👤':
        return 'assets/icons/user.png';
      case '😊':
        return 'assets/icons/smile.png';
      case '✨':
        return 'assets/icons/sparkles.png';
      case '⭐':
        return 'assets/icons/star.png';
      default:
        return 'assets/icons/mask.png';
    }
  }

  @override
  Widget build(BuildContext context) {
    return Image.asset(
      _getImagePath(),
      width: size,
      height: size,
      color: color,
      fit: BoxFit.contain,
      errorBuilder: (context, error, stackTrace) {
        // 如果图片加载失败，显示原始emoji
        return Text(
          emoji,
          style: TextStyle(fontSize: size),
        );
      },
    );
  }
}
