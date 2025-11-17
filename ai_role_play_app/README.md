# AI角色扮演移动应用

使用Flutter开发的原生移动应用，提供更好的用户体验。

## 功能特性

- 🎭 8个预设AI角色
- 💬 流畅的聊天气泡界面
- 🔄 对话重置和清空功能
- 📱 原生移动体验
- 🌐 支持多种AI模型

## 技术栈

- **Flutter**: 跨平台移动开发框架
- **Dart**: 编程语言
- **http**: 网络请求库
- **flutter_dotenv**: 环境变量管理

## 开发环境要求

- Flutter 3.0+ ([安装指南](https://flutter.dev/docs/get-started/install))
- Dart 3.0+
- Android Studio / VS Code
- Android/iOS模拟器或真机（可选）
- Windows桌面支持（可选）
- Web浏览器支持（可选）

## 安装依赖

确保已安装Flutter SDK并添加到PATH环境变量中。

### Windows环境变量配置

1. 下载Flutter SDK并解压到目录（如 `C:\flutter`）
2. 将 `C:\flutter\bin` 添加到系统PATH环境变量
3. 验证安装：
   ```bash
   flutter --version
   ```

### 获取项目依赖

```bash
flutter pub get
```

如果遇到依赖问题，可以尝试：

```bash
flutter pub add http:^1.6.0
```

### 启用多平台支持

```bash
# 启用Windows桌面支持
flutter config --enable-windows-desktop

# 启用Web支持
flutter config --enable-web

# 重新创建项目以支持所有平台
flutter create .
```

## 配置API Key

在 `.env` 文件中配置您的API密钥：

```env
OPENAI_API_KEY=your_openai_api_key_here
ZHIPU_API_KEY=your_zhipu_api_key_here
SILICONFLOW_API_KEY=your_siliconflow_api_key_here
```

## 运行应用

### 开发模式

```bash
# 运行到连接的设备
flutter run

# 运行到特定平台
flutter run -d windows  # Windows桌面
flutter run -d chrome   # Chrome浏览器
flutter run -d edge     # Edge浏览器

# 启用所有平台支持后重新创建项目
flutter create .
```

### 构建APK (Android)

```bash
flutter build apk
```

### 构建IPA (iOS)

```bash
flutter build ios
```

### 构建Windows应用

```bash
flutter build windows
```

## 项目结构

```
lib/
├── main.dart              # 主程序入口
├── models/                # 数据模型
├── screens/               # 页面组件
├── widgets/               # 自定义组件
└── services/              # 服务层
```

## 角色列表

1. **智慧导师** - 教育和启发
2. **莎士比亚** - 文学和诗歌
3. **未来AI** - 科技展望
4. **米其林大厨** - 美食和烹饪
5. **傲娇猫娘** - 可爱互动
6. **福尔摩斯** - 推理侦探
7. **健身教练** - 健康和运动
8. **艺术评论家** - 艺术和美学

## 自定义角色

可以通过修改 `roles` 列表添加更多角色。

## 许可证

MIT License
