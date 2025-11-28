import 'package:flutter/material.dart';

/// 丰富多彩的主题颜色配置
class ColorTheme {
  // AppBar 渐变色 - 彩虹渐变
  static const List<Color> appBarGradient = [
    Color(0xFFFF6B6B), // 鲜红
    Color(0xFFFF8E72), // 橙红
    Color(0xFFFFA502), // 橙色
  ];

  // 用户消息颜色 - 紫蓝渐变
  static const List<Color> userMessageGradient = [
    Color(0xFF667EEA), // 紫蓝
    Color(0xFF764BA2), // 深紫
  ];

  // AI 头像颜色 - 橙黄渐变
  static const List<Color> aiAvatarGradient = [
    Color(0xFFFFB347), // 浅橙
    Color(0xFFFF8C42), // 深橙
  ];

  // 用户头像颜色 - 绿蓝渐变
  static const List<Color> userAvatarGradient = [
    Color(0xFF56AB2F), // 绿色
    Color(0xFF00B4DB), // 蓝色
  ];

  // 角色选择器背景 - 彩虹渐变
  static const List<Color> roleSelectorGradient = [
    Color(0xFFFFF5E1), // 浅黄
    Color(0xFFFFE4E1), // 浅粉
  ];

  // 背景渐变 - 多彩渐变
  static const List<Color> backgroundGradient = [
    Color(0xFFFFE5E5), // 浅红
    Color(0xFFFFE8CC), // 浅橙
    Color(0xFFFFEED5), // 浅黄
    Color(0xFFE8F5E9), // 浅绿
    Color(0xFFE1F5FE), // 浅蓝
  ];

  // 角色特定颜色 - 为每个角色分配独特的颜色
  static const Map<String, List<Color>> roleColors = {
    // 智慧导师 - 蓝紫
    'teacher': [Color(0xFF5E72E4), Color(0xFF825EE4)],
    // 莎士比亚 - 紫红
    'shakespeare': [Color(0xFFE91E63), Color(0xFF9C27B0)],
    // 爱因斯坦 - 黄橙
    'einstein': [Color(0xFFFFC107), Color(0xFFFF9800)],
    // 克里斯托弗·诺兰 - 青蓝
    'nolan': [Color(0xFF00BCD4), Color(0xFF2196F3)],
    // 乔布斯 - 灰黑
    'jobs': [Color(0xFF757575), Color(0xFF424242)],
    // 玛丽亚·居里 - 绿青
    'curie': [Color(0xFF4CAF50), Color(0xFF009688)],
    // 达芬奇 - 棕金
    'davinci': [Color(0xFF8D6E63), Color(0xFFD4AF37)],
    // 图灵 - 靛蓝
    'turing': [Color(0xFF3F51B5), Color(0xFF1A237E)],
  };

  // 装饰元素颜色
  static const List<Color> decorativeColors = [
    Color(0xFFFF6B6B), // 红
    Color(0xFFFFA502), // 橙
    Color(0xFFFFD93D), // 黄
    Color(0xFF6BCB77), // 绿
    Color(0xFF4D96FF), // 蓝
    Color(0xFF9D84B7), // 紫
  ];

  // 获取角色颜色
  static List<Color> getRoleColors(String roleId) {
    return roleColors[roleId] ?? [Color(0xFF667EEA), Color(0xFF764BA2)];
  }

  // 获取随机装饰颜色
  static Color getRandomDecorativeColor(int index) {
    return decorativeColors[index % decorativeColors.length];
  }

  // 空状态图标背景 - 彩虹渐变
  static const List<Color> emptyStateGradient = [
    Color(0xFFFF6B6B),
    Color(0xFFFFA502),
    Color(0xFFFFD93D),
    Color(0xFF6BCB77),
    Color(0xFF4D96FF),
  ];

  // 输入框阴影颜色
  static const Color inputShadowColor = Color(0xFFE0E0E0);

  // 按钮颜色 - 发送按钮
  static const List<Color> sendButtonGradient = [
    Color(0xFF56AB2F),
    Color(0xFF00B4DB),
  ];

  // 角色计数标签背景
  static const List<Color> roleBadgeGradient = [
    Color(0xFFFF6B6B),
    Color(0xFFFFA502),
  ];
}
