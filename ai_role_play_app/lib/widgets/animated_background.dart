import 'package:flutter/material.dart';
import '../theme/color_theme.dart';
import 'custom_emoji_icon.dart';

class AnimatedBackground extends StatefulWidget {
  final Widget child;

  const AnimatedBackground({
    super.key,
    required this.child,
  });

  @override
  State<AnimatedBackground> createState() => _AnimatedBackgroundState();
}

class _AnimatedBackgroundState extends State<AnimatedBackground>
    with TickerProviderStateMixin {
  late AnimationController _controller1;
  late AnimationController _controller2;

  @override
  void initState() {
    super.initState();
    _controller1 = AnimationController(
      duration: const Duration(seconds: 20),
      vsync: this,
    )..repeat();

    _controller2 = AnimationController(
      duration: const Duration(seconds: 30),
      vsync: this,
    )..repeat();
  }

  @override
  void dispose() {
    if (_controller1.isAnimating) {
      _controller1.stop();
    }
    if (_controller2.isAnimating) {
      _controller2.stop();
    }
    _controller1.dispose();
    _controller2.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        // 背景渐变 - 多彩渐变
        Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: ColorTheme.backgroundGradient,
            ),
          ),
        ),
        // 浮动装饰元素 1
        Positioned(
          top: 50,
          right: 20,
          child: RepaintBoundary(
            child: AnimatedBuilder(
              animation: _controller1,
              builder: (context, child) {
                return Transform.translate(
                  offset: Offset(
                    20 * (1 - (_controller1.value - 0.5).abs() * 2),
                    -10 * (1 - (_controller1.value - 0.5).abs() * 2),
                  ),
                  child: child,
                );
              },
              child: Container(
                width: 80,
                height: 80,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: LinearGradient(
                    colors: [
                      const Color(0xFFFF6B6B).withOpacity(0.15),
                      const Color(0xFFFFA502).withOpacity(0.08),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
        // 浮动装饰元素 2
        Positioned(
          bottom: 100,
          left: 30,
          child: RepaintBoundary(
            child: AnimatedBuilder(
              animation: _controller2,
              builder: (context, child) {
                return Transform.translate(
                  offset: Offset(
                    -15 * (1 - (_controller2.value - 0.5).abs() * 2),
                    15 * (1 - (_controller2.value - 0.5).abs() * 2),
                  ),
                  child: child,
                );
              },
              child: Container(
                width: 60,
                height: 60,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: LinearGradient(
                    colors: [
                      Colors.red.shade200.withOpacity(0.3),
                      Colors.red.shade100.withOpacity(0.1),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
        // 浮动装饰元素 3
        Positioned(
          top: 200,
          left: 20,
          child: RepaintBoundary(
            child: AnimatedBuilder(
              animation: _controller1,
              builder: (context, child) {
                return Transform.rotate(
                  angle: _controller1.value * 6.28,
                  child: child,
                );
              },
              child: EmojiIcon(
                emoji: '✨',
                size: 30,
                color: Colors.yellow.withOpacity(0.3),
              ),
            ),
          ),
        ),
        // 浮动装饰元素 4
        Positioned(
          bottom: 300,
          right: 50,
          child: RepaintBoundary(
            child: AnimatedBuilder(
              animation: _controller2,
              builder: (context, child) {
                return Transform.rotate(
                  angle: -_controller2.value * 6.28,
                  child: child,
                );
              },
              child: EmojiIcon(
                emoji: '⭐',
                size: 25,
                color: Colors.amber.withOpacity(0.3),
              ),
            ),
          ),
        ),
        // 主要内容
        widget.child,
      ],
    );
  }
}
