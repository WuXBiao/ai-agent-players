import 'package:flutter/material.dart';
import '../models/role.dart';
import '../theme/color_theme.dart';
import 'custom_emoji_icon.dart';

class RoleSelector extends StatefulWidget {
  final List<Role> roles;
  final Role? selectedRole;
  final Function(Role) onRoleSelected;

  const RoleSelector({
    super.key,
    required this.roles,
    required this.selectedRole,
    required this.onRoleSelected,
  });

  @override
  State<RoleSelector> createState() => _RoleSelectorState();
}

class _RoleSelectorState extends State<RoleSelector>
    with SingleTickerProviderStateMixin {
  late AnimationController _hoverController;
  int? _hoveredIndex;

  @override
  void initState() {
    super.initState();
    _initializeAnimations();
  }

  void _initializeAnimations() {
    _hoverController = AnimationController(
      duration: const Duration(milliseconds: 300),
      vsync: this,
    );
  }

  @override
  void dispose() {
    try {
      if (_hoverController.isAnimating) {
        _hoverController.stop();
      }
      _hoverController.dispose();
    } catch (e) {
      // 忽略已释放的控制器错误
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: ColorTheme.roleSelectorGradient,
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
        ),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFFFF6B6B).withOpacity(0.08),
            blurRadius: 12,
            offset: const Offset(0, 3),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.only(left: 4, bottom: 12),
            child: Row(
              children: [
                Row(
                  children: [
                    const EmojiIcon(
                      emoji: '🎭',
                      size: 16,
                    ),
                    const SizedBox(width: 4),
                    const Text(
                      '选择角色',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                        color: Colors.black87,
                      ),
                    ),
                  ],
                ),
                const SizedBox(width: 8),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 8,
                    vertical: 4,
                  ),
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: ColorTheme.roleBadgeGradient,
                    ),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Text(
                    '${widget.roles.length}个角色',
                    style: const TextStyle(
                      fontSize: 12,
                      color: Colors.white,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
              ],
            ),
          ),
          // 网格布局 - 不需要左右滑动
          GridView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 4, // 每行显示 4 个角色
              childAspectRatio: 0.85,
              crossAxisSpacing: 8,
              mainAxisSpacing: 8,
            ),
            itemCount: widget.roles.length,
            itemBuilder: (context, index) {
              final role = widget.roles[index];
              final isSelected = widget.selectedRole?.id == role.id;

              return MouseRegion(
                onEnter: (_) {
                  setState(() => _hoveredIndex = index);
                  _hoverController.forward();
                },
                onExit: (_) {
                  setState(() => _hoveredIndex = null);
                  _hoverController.reverse();
                },
                child: GestureDetector(
                  onTap: () => widget.onRoleSelected(role),
                  child: AnimatedBuilder(
                    animation: _hoverController,
                    builder: (context, child) {
                      final scale = isSelected
                          ? 1.05
                          : 1.0 + (_hoveredIndex == index ? 0.05 : 0.0);

                      return Transform.scale(
                        scale: scale,
                        child: child,
                      );
                    },
                    child: Container(
                      decoration: BoxDecoration(
                        gradient: isSelected
                            ? LinearGradient(
                                colors: ColorTheme.getRandomDecorativeColor(index) == ColorTheme.decorativeColors[0]
                                    ? [const Color(0xFFFF6B6B), const Color(0xFFFF8E72)]
                                    : ColorTheme.getRandomDecorativeColor(index) == ColorTheme.decorativeColors[1]
                                        ? [const Color(0xFFFFA502), const Color(0xFFFFB347)]
                                        : ColorTheme.getRandomDecorativeColor(index) == ColorTheme.decorativeColors[2]
                                            ? [const Color(0xFFFFD93D), const Color(0xFFFFC107)]
                                            : ColorTheme.getRandomDecorativeColor(index) == ColorTheme.decorativeColors[3]
                                                ? [const Color(0xFF6BCB77), const Color(0xFF4CAF50)]
                                                : ColorTheme.getRandomDecorativeColor(index) == ColorTheme.decorativeColors[4]
                                                    ? [const Color(0xFF4D96FF), const Color(0xFF2196F3)]
                                                    : [const Color(0xFF9D84B7), const Color(0xFF9C27B0)],
                                begin: Alignment.topLeft,
                                end: Alignment.bottomRight,
                              )
                            : LinearGradient(
                                colors: [
                                  Colors.grey.shade100,
                                  Colors.grey.shade200,
                                ],
                              ),
                        borderRadius: BorderRadius.circular(16),
                        boxShadow: [
                          BoxShadow(
                            color: isSelected
                                ? ColorTheme.getRandomDecorativeColor(index).withOpacity(0.3)
                                : Colors.grey.withOpacity(0.2),
                            blurRadius: 12,
                            offset: const Offset(0, 4),
                          ),
                        ],
                      ),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          // 角色图标
                          Container(
                            width: 45,
                            height: 45,
                            decoration: BoxDecoration(
                              shape: BoxShape.circle,
                              color: isSelected
                                  ? Colors.white.withOpacity(0.2)
                                  : Colors.white.withOpacity(0.5),
                            ),
                            child: Center(
                              child: Text(
                                role.icon,
                                style: const TextStyle(fontSize: 24),
                              ),
                            ),
                          ),
                          const SizedBox(height: 4),
                          // 角色名称
                          Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 4),
                            child: Text(
                              role.name,
                              style: TextStyle(
                                fontSize: 11,
                                fontWeight: FontWeight.bold,
                                color: isSelected
                                    ? Colors.white
                                    : Colors.black87,
                              ),
                              textAlign: TextAlign.center,
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                          // 选中指示器
                          if (isSelected)
                            Padding(
                              padding: const EdgeInsets.only(top: 3),
                              child: Container(
                                width: 5,
                                height: 5,
                                decoration: BoxDecoration(
                                  shape: BoxShape.circle,
                                  color: Colors.white,
                                ),
                              ),
                            ),
                        ],
                      ),
                    ),
                  ),
                ),
              );
            },
          ),
        ],
      ),
    );
  }
}
