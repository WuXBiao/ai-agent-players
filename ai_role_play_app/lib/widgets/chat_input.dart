import 'package:flutter/material.dart';
import 'custom_emoji_icon.dart';

class ChatInput extends StatefulWidget {
  final Function(String) onSend;
  final bool isSending;

  const ChatInput({
    super.key,
    required this.onSend,
    this.isSending = false,
  });

  @override
  State<ChatInput> createState() => _ChatInputState();
}

class _ChatInputState extends State<ChatInput>
    with SingleTickerProviderStateMixin {
  final TextEditingController _textController = TextEditingController();
  late AnimationController _buttonAnimationController;
  late Animation<double> _buttonScaleAnimation;
  bool _hasText = false;

  @override
  void initState() {
    super.initState();
    _initializeAnimations();
    _textController.addListener(() {
      setState(() {
        _hasText = _textController.text.isNotEmpty;
      });
    });
  }

  void _initializeAnimations() {
    _buttonAnimationController = AnimationController(
      duration: const Duration(milliseconds: 200),
      vsync: this,
    );

    _buttonScaleAnimation =
        Tween<double>(begin: 1.0, end: 0.95).animate(
          CurvedAnimation(
            parent: _buttonAnimationController,
            curve: Curves.easeInOut,
          ),
        );
  }

  void _handleSend() {
    final text = _textController.text.trim();
    if (text.isNotEmpty && !widget.isSending) {
      if (mounted && !_buttonAnimationController.isAnimating) {
        _buttonAnimationController.forward().then((_) {
          if (mounted) {
            _buttonAnimationController.reverse();
          }
        });
      }
      widget.onSend(text);
      _textController.clear();
    }
  }

  @override
  void dispose() {
    _textController.dispose();
    try {
      if (_buttonAnimationController.isAnimating) {
        _buttonAnimationController.stop();
      }
      _buttonAnimationController.dispose();
    } catch (e) {
      // 忽略已释放的控制器错误
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return RepaintBoundary(
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Colors.white,
              Colors.grey.shade50,
            ],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
          boxShadow: [
            BoxShadow(
              color: Colors.grey.withOpacity(0.1),
              blurRadius: 10,
              offset: const Offset(0, -2),
            ),
          ],
        ),
        child: Row(
          children: [
            // 表情按钮
            Container(
              width: 40,
              height: 40,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: Colors.grey.shade100,
              ),
              child: Material(
                color: Colors.transparent,
                child: InkWell(
                  onTap: () {
                    // 可以添加表情选择功能
                  },
                  borderRadius: BorderRadius.circular(20),
                  child: const Center(
                    child: EmojiIcon(
                      emoji: '😊',
                      size: 20,
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(width: 12),
          // 输入框
          Expanded(
            child: Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: [
                    Colors.grey.shade100,
                    Colors.grey.shade50,
                  ],
                ),
                borderRadius: BorderRadius.circular(25),
                boxShadow: [
                  BoxShadow(
                    color: Colors.blue.withOpacity(0.1),
                    blurRadius: 8,
                  ),
                ],
              ),
              child: TextField(
                controller: _textController,
                maxLines: null,
                textInputAction: TextInputAction.send,
                decoration: InputDecoration(
                  hintText: '说点什么吧...',
                  hintStyle: TextStyle(
                    color: Colors.grey.shade400,
                    fontSize: 15,
                  ),
                  border: InputBorder.none,
                  contentPadding: const EdgeInsets.symmetric(
                    horizontal: 20,
                    vertical: 12,
                  ),
                  prefixIcon: Padding(
                    padding: const EdgeInsets.only(left: 16, right: 8),
                    child: Icon(
                      Icons.edit_note,
                      color: Colors.grey.shade400,
                      size: 20,
                    ),
                  ),
                ),
                onSubmitted: (_) => _handleSend(),
              ),
            ),
          ),
          const SizedBox(width: 12),
          // 发送按钮
          ScaleTransition(
            scale: _buttonScaleAnimation,
            child: Container(
              width: 44,
              height: 44,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: LinearGradient(
                  colors: _hasText && !widget.isSending
                      ? [
                          Colors.green.shade400,
                          Colors.green.shade600,
                        ]
                      : [
                          Colors.grey.shade300,
                          Colors.grey.shade400,
                        ],
                ),
                boxShadow: [
                  BoxShadow(
                    color: (_hasText && !widget.isSending
                            ? Colors.green
                            : Colors.grey)
                        .withOpacity(0.3),
                    blurRadius: 8,
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              child: Material(
                color: Colors.transparent,
                child: InkWell(
                  onTap: _hasText && !widget.isSending ? _handleSend : null,
                  borderRadius: BorderRadius.circular(22),
                  child: Center(
                    child: widget.isSending
                        ? SizedBox(
                            width: 20,
                            height: 20,
                            child: CircularProgressIndicator(
                              strokeWidth: 2.5,
                              valueColor: AlwaysStoppedAnimation<Color>(
                                Colors.white.withOpacity(0.8),
                              ),
                            ),
                          )
                        : Icon(
                            Icons.send_rounded,
                            color: Colors.white,
                            size: 20,
                          ),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
        ),
    );
  }
}
