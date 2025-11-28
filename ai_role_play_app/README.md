# 📱 Android APP（Kivy）

基于 **Kivy 框架**的 AI 角色扮演 Android 原生应用。

> 📖 [← 返回项目主页](../README.md)

## 📋 应用说明

这是项目的 **独立移动端应用**，特点：
- ✅ **独立运行** - 不依赖 Go/Python 后端服务
- ✅ **直接调用 AI API** - 直接调用 OpenAI、智谱 AI 等 LLM
- ✅ **原生 Android 体验** - 使用 Kivy 框架
- ✅ **本地数据存储** - 离线聊天支持
- ✅ **流畅的移动界面** - 移动优化 UI

**与 Web 前端的区别**：
| 特性 | Web 前端 | 移动端 APP |
|------|---------|----------|
| 后端依赖 | 需要 Go + Python 服务 | 无需后端服务 |
| AI 调用 | Go → Python → AI | 直接 → AI |
| 部署方式 | 浏览器访问 | Android APK |
| 网络要求 | 需要连接到后端服务器 | 只需连接到 AI API |

## 功能特性

- 🎭 8 个预设 AI 角色
- 💬 流畅的聊天气泡界面
- 🔄 对话重置和清空功能
- 📱 原生 Android 体验
- 🌐 支持多种 AI 模型（OpenAI、智谱 AI、硅基流动）
- 💾 本地消息存储
- 🔋 低功耗设计

## 技术栈

- **Kivy**: 跨平台 Python UI 框架
- **Python**: 3.9+
- **Buildozer**: Android 打包工具
- **OpenAI/智谱 AI SDK**: 直接调用 AI API

## 开发环境要求

- Python 3.9+
- Kivy 2.0+
- Buildozer（用于打包）
- Android SDK/NDK（用于编译）
- Java Development Kit (JDK)

## 快速开始

### 1. 配置 API Key（必须）

在 `.env` 文件中配置您的 API 密钥（至少配置一个）：

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，添加 API Key
```

```env
# OpenAI
OPENAI_API_KEY=sk-your-api-key-here

# 或智谱 AI
ZHIPU_API_KEY=your-zhipu-api-key-here

# 或硅基流动
SILICONFLOW_API_KEY=sk-your-siliconflow-key-here

# 选择使用的 LLM 提供商
LLM_PROVIDER=openai  # 或 zhipu, siliconflow
```

### 2. 安装 Python 依赖

```bash
cd ai_role_play_app
pip install -r requirements.txt
```

### 3. 安装 Buildozer（仅用于打包）

```bash
pip install buildozer
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

## 重要说明

### ⚠️ 不需要后端服务

**移动端 APP 是独立的，不需要启动 Go 和 Python 后端服务**。

- ❌ 不需要 Go 服务（`server-go`）
- ❌ 不需要 Python gRPC 服务（`server-python`）
- ✅ 只需要配置 AI API Key（OpenAI、智谱 AI 等）

### 与 Web 前端的对比

**Web 前端**（需要后端）：
```
Vue 前端 → Go 服务 → Python gRPC 服务 → AI API
```

**移动端 APP**（独立运行）：
```
Kivy APP → AI API（直接）
```

## 注意事项

1. **API Key 配置**：必须配置至少一个 LLM 的 API Key（OpenAI、智谱 AI 或硅基流动）
2. **网络权限**：APP 需要联网访问 AI API，不支持离线使用
3. **打包环境**：
   - Windows 用户建议使用 WSL 或虚拟机
   - 或使用 GitHub Actions 自动打包（推荐）
4. **APK 大小**：约 50-80MB（包含 Python 运行时）
5. **API 成本**：直接调用 AI API，费用由 API 提供商收取

## 常见问题

### Q: 移动端 APP 需要启动 Go 和 Python 服务吗？

A: **不需要**。移动端 APP 是独立的，直接调用 AI API，不依赖任何后端服务。

### Q: 移动端 APP 和 Web 前端有什么区别？

A: 
- **Web 前端**：需要启动 Go + Python 后端服务，通过后端调用 AI
- **移动端 APP**：独立运行，直接调用 AI API，无需后端服务

### Q: 如何在 Windows 上打包 APK？

A: 有三种方法：
1. 使用 WSL（Windows Subsystem for Linux）
2. 使用虚拟机（VirtualBox、VMware）
3. 使用 GitHub Actions 自动打包（推荐）

### Q: APP 闪退怎么办？

A: 检查：
1. API Key 是否正确配置在 `.env` 文件中
2. 网络连接是否正常
3. API Key 是否有效且有足够的配额
4. 查看 Android 日志：`adb logcat`

### Q: 如何修改 APP 名称和图标？

A: 编辑 `buildozer.spec` 文件中的相关配置。

### Q: 支持哪些 AI 模型？

A: 支持以下 LLM 提供商：
- **OpenAI**：GPT-4、GPT-3.5 等
- **智谱 AI**：GLM-4 等
- **硅基流动**：支持多个开源模型

## 许可证

MIT License

