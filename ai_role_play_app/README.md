# 📱 Android APP（Kivy）

基于 **Kivy 框架**的 AI 角色扮演 Android 原生应用。

> 📖 [← 返回项目主页](../README.md)

## 📋 应用说明

这是项目的 **移动端应用**，负责：
- 提供原生 Android 体验
- 离线聊天支持
- 本地消息存储
- 流畅的移动界面

**特点**：
- 📱 原生 Android 体验（使用 Kivy）
- 💾 本地数据存储
- 🔋 低功耗设计
- 🎨 移动优化 UI

## 功能特性

- 🎭 8 个预设 AI 角色
- 💬 流畅的聊天气泡界面
- 🔄 对话重置和清空功能
- 📱 原生移动体验
- 🌐 支持多种 AI 模型（OpenAI、智谱 AI、硅基流动）

## 技术栈

- **Kivy**: 跨平台 Python UI 框架
- **Python**: 3.9+
- **Buildozer**: Android 打包工具
- **gRPC**: 与后端通信

## 开发环境要求

- Python 3.9+
- Kivy 2.0+
- Buildozer（用于打包）
- Android SDK/NDK（用于编译）
- Java Development Kit (JDK)

## 安装依赖

### 1. 安装 Python 依赖

```bash
cd ai_role_play_app
pip install -r requirements.txt
```

### 2. 安装 Buildozer（用于打包）

```bash
pip install buildozer
```

### 3. 配置 API Key

在 `.env` 文件中配置您的 API 密钥：

```env
OPENAI_API_KEY=your_openai_api_key_here
ZHIPU_API_KEY=your_zhipu_api_key_here
SILICONFLOW_API_KEY=your_siliconflow_api_key_here
```

## 在电脑上测试运行

### 1. 安装 Kivy

```bash
pip install kivy
```

### 2. 运行 APP

```bash
cd ai_role_play_app
python main.py
```

## 打包成 Android APK

### 方法 1：使用 Buildozer（Linux/Mac）

#### 1. 初始化（已完成）

配置文件 `buildozer.spec` 已创建。

#### 2. 打包 APK

```bash
cd ai_role_play_app
buildozer android debug
```

生成的 APK 在 `bin/` 目录下。

### 方法 2：使用 GitHub Actions（推荐 Windows 用户）

在 GitHub 上配置 CI/CD 自动打包。

### 方法 3：使用在线服务

- [Replit](https://replit.com/) - 在线编译
- [Google Colab](https://colab.research.google.com/) - 免费 Linux 环境

## 项目结构

```
ai_role_play_app/
├── main.py                 # APP 主程序
├── buildozer.spec          # Android 打包配置
├── requirements.txt        # Python 依赖
├── .env.example            # 环境变量示例
└── README.md              # 说明文档
```

## 角色列表

1. **🧙‍♂️ 智慧导师** - 教育和启发
2. **📚 莎士比亚** - 文学和诗歌
3. **🚀 未来 AI** - 科技展望
4. **👨‍🍳 米其林大厨** - 美食和烹饪
5. **😸 傲娇猫娘** - 可爱互动
6. **🔍 福尔摩斯** - 推理侦探
7. **💪 健身教练** - 健康和运动
8. **🎨 艺术评论家** - 艺术和美学

## 自定义角色

可以通过修改 `main.py` 中的 `ROLES` 列表添加更多角色。

## 注意事项

1. **网络权限**：APP 需要联网访问 AI API
2. **API Key**：需要配置至少一个 LLM 的 API Key
3. **打包环境**：
   - Windows 用户建议使用 WSL 或虚拟机
   - 或使用 GitHub Actions 自动打包
4. **APK 大小**：约 50-80MB（包含 Python 运行时）

## 常见问题

### Q: 如何在 Windows 上打包 APK？

A: 有三种方法：
1. 使用 WSL（Windows Subsystem for Linux）
2. 使用虚拟机（VirtualBox、VMware）
3. 使用 GitHub Actions 自动打包（推荐）

### Q: APP 闪退怎么办？

A: 检查：
1. API Key 是否正确配置
2. 网络连接是否正常
3. 查看 Android 日志：`adb logcat`

### Q: 如何修改 APP 名称和图标？

A: 编辑 `buildozer.spec` 文件中的相关配置。

## 许可证

MIT License

