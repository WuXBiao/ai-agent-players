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

## 项目结构

```
app/
├── main.py              # APP 主程序
├── buildozer.spec       # Android 打包配置
├── requirements.txt     # Python 依赖
└── README.md           # 说明文档
```

## 功能特性

- 🎭 8个预设AI角色可选
- 💬 流畅的聊天界面
- 🔄 对话重置功能
- 📱 原生 Android 体验
- 🌐 支持多种 LLM（智谱AI、硅基流动、OpenAI）

## 在电脑上测试运行

### 1. 安装 Kivy

```bash
pip install kivy
```

### 2. 运行 APP

```bash
cd app
python main.py
```

## 打包成 Android APK

### 方法 1：使用 Buildozer（Linux/Mac）

#### 1. 安装 Buildozer

```bash
pip install buildozer
```

#### 2. 初始化（已完成）

配置文件 `buildozer.spec` 已创建。

#### 3. 打包 APK

```bash
cd app
buildozer android debug
```

生成的 APK 在 `bin/` 目录下。

### 方法 2：使用 GitHub Actions（推荐 Windows 用户）

在 GitHub 上配置 CI/CD 自动打包。

### 方法 3：使用在线服务

- [Replit](https://replit.com/) - 在线编译
- [Google Colab](https://colab.research.google.com/) - 免费 Linux 环境

## 配置 API Key

在 `app/` 目录下创建 `.env` 文件：

```env
# 智谱 AI（推荐）
ZHIPU_API_KEY=your_zhipu_api_key

# 或硅基流动
SILICONFLOW_API_KEY=your_siliconflow_api_key

# 或 OpenAI
OPENAI_API_KEY=your_openai_api_key
```

## 注意事项

1. **网络权限**：APP 需要联网访问 AI API
2. **API Key**：需要配置至少一个 LLM 的 API Key
3. **打包环境**：
   - Windows 用户建议使用 WSL 或虚拟机
   - 或使用 GitHub Actions 自动打包
4. **APK 大小**：约 50-80MB（包含 Python 运行时）

## 开发说明

### 代码结构

- `RolePlayApp`：主应用类
- `init_llm()`：初始化大模型
- `send_message()`：发送消息逻辑
- `get_ai_response()`：获取 AI 响应

### 复用现有代码

APP 代码复用了项目中的：
- LLM 初始化逻辑
- 角色配置（ROLES）
- 对话历史管理

可以直接导入使用：
```python
from role_play_cli import ROLES, init_llm
```

## 进阶功能

可以添加：
- 🎨 自定义角色
- 💾 对话历史保存
- 🔊 语音输入/输出
- 🌙 夜间模式
- 📊 使用统计

## 问题排查

### 打包失败

- 检查 Buildozer 版本
- 确保 Android SDK/NDK 已安装
- 查看日志：`buildozer android debug 2>&1 | tee build.log`

### APP 闪退

- 检查 API Key 配置
- 查看 Android 日志：`adb logcat`

## 许可证

MIT License
