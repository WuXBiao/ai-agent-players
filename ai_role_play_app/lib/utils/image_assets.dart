/// 图片资源管理器
class ImageAssets {
  // 图标资源
  static const String maskIcon = 'assets/icons/mask.png'; // 🎭 剧院面具
  static const String robotIcon = 'assets/icons/robot.png'; // 🤖 机器人
  static const String userIcon = 'assets/icons/user.png'; // 👤 用户
  static const String smileIcon = 'assets/icons/smile.png'; // 😊 微笑
  static const String sparklesIcon = 'assets/icons/sparkles.png'; // ✨ 闪闪发光
  static const String starIcon = 'assets/icons/star.png'; // ⭐ 星星

  // 获取所有图标资源
  static const Map<String, String> allIcons = {
    'mask': maskIcon,
    'robot': robotIcon,
    'user': userIcon,
    'smile': smileIcon,
    'sparkles': sparklesIcon,
    'star': starIcon,
  };
}
