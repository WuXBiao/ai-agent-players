# 🔐 移动端 API Key 配置指南

## API Key 存放位置

移动端应用的 API Key 存放在**项目根目录的 `.env` 文件**中。

### 📁 文件结构

```
ai_role_play_app/
├── lib/
│   ├── main.dart                    # 应用入口（加载 .env）
│   ├── services/
│   │   └── ai_service.dart          # AI 服务（读取 API Key）
│   ├── screens/
│   ├── widgets/
│   └── models/
├── pubspec.yaml                     # 项目配置（声明 .env 资源）
├── .env                             # ✅ API Key 存放位置（需要手动创建）
└── .gitignore                       # Git 忽略配置（.env 被忽略）
```

## 🔑 API Key 配置

### 1. 创建 `.env` 文件

在 `ai_role_play_app/` 目录下创建 `.env` 文件：

```bash
# 在 ai_role_play_app/ 目录下
touch .env
```

### 2. 添加 API Key

在 `.env` 文件中添加你的 API Key：

```env
# OpenAI API Key
OPENAI_API_KEY=sk-your-openai-api-key-here

# 智谱 AI API Key
ZHIPU_API_KEY=your-zhipu-api-key-here

# 硅基流动 API Key
SILICONFLOW_API_KEY=your-siliconflow-api-key-here
```

### 3. 获取 API Key

#### OpenAI
- 网址：https://platform.openai.com/api-keys
- 格式：`sk-...`

#### 智谱 AI
- 网址：https://open.bigmodel.cn/
- 格式：`glm-...`

#### 硅基流动
- 网址：https://www.siliconflow.cn/
- 格式：`sk-...`

## 🔄 工作流程

### 1. 应用启动时加载 `.env`

```dart
// lib/main.dart
void main() async {
  await dotenv.load(fileName: ".env");  // ← 加载 .env 文件
  runApp(const MyApp());
}
```

### 2. AI Service 读取 API Key

```dart
// lib/services/ai_service.dart
static String? _getApiKey(String provider) {
  switch (provider) {
    case 'openai':
      return dotenv.env['OPENAI_API_KEY'];      // ← 从 .env 读取
    case 'zhipu':
      return dotenv.env['ZHIPU_API_KEY'];       // ← 从 .env 读取
    case 'siliconflow':
      return dotenv.env['SILICONFLOW_API_KEY']; // ← 从 .env 读取
    default:
      return null;
  }
}
```

### 3. 发送 API 请求

```dart
// 使用默认提供商（硅基流动）
final response = await AIService.sendMessage(
  role,
  history,
  userMessage,
  provider: 'siliconflow',  // ← 使用 .env 中的 SILICONFLOW_API_KEY
);
```

## 📦 依赖配置

### pubspec.yaml

```yaml
dependencies:
  flutter_dotenv: ^5.0.2  # ← 用于加载 .env 文件

flutter:
  assets:
    - .env                 # ← 声明 .env 为资源文件
```

## 🔒 安全性

### `.env` 文件被 Git 忽略

```
# .gitignore
.env  # ← .env 文件不会被提交到 Git
```

### 为什么要忽略 `.env`？

- ✅ **保护敏感信息**：API Key 不会被上传到 GitHub
- ✅ **避免泄露**：防止 API Key 被公开
- ✅ **本地开发**：每个开发者可以有自己的 `.env` 文件

### 安全最佳实践

1. **不要提交 `.env` 到 Git**
   ```bash
   # 确保 .gitignore 包含 .env
   echo ".env" >> .gitignore
   ```

2. **使用 `.env.example` 作为模板**
   ```bash
   # 创建示例文件（可以提交到 Git）
   cp .env .env.example
   
   # 编辑 .env.example，用占位符替换真实 Key
   ```

3. **`.env.example` 内容**
   ```env
   # OpenAI API Key (从 https://platform.openai.com/api-keys 获取)
   OPENAI_API_KEY=sk-your-api-key-here

   # 智谱 AI API Key (从 https://open.bigmodel.cn/ 获取)
   ZHIPU_API_KEY=your-api-key-here

   # 硅基流动 API Key (从 https://www.siliconflow.cn/ 获取)
   SILICONFLOW_API_KEY=your-api-key-here
   ```

## 🚀 快速开始

### 第 1 步：创建 `.env` 文件

```bash
cd ai_role_play_app
touch .env
```

### 第 2 步：添加 API Key

编辑 `.env` 文件，添加你的 API Key：

```env
OPENAI_API_KEY=sk-your-key
ZHIPU_API_KEY=your-key
SILICONFLOW_API_KEY=your-key
```

### 第 3 步：运行应用

```bash
flutter run
```

## ❓ 常见问题

### Q1: 为什么应用启动时出现 "API密钥未配置" 错误？

**A:** 说明 `.env` 文件不存在或 API Key 未正确配置。

**解决方案：**
1. 确保 `.env` 文件存在于 `ai_role_play_app/` 目录
2. 检查 API Key 是否正确填写
3. 确保没有多余的空格或换行符

### Q2: 如何切换 AI 提供商？

**A:** 在调用 `AIService.sendMessage()` 时指定 `provider` 参数：

```dart
// 使用 OpenAI
await AIService.sendMessage(role, history, message, provider: 'openai');

// 使用智谱 AI
await AIService.sendMessage(role, history, message, provider: 'zhipu');

// 使用硅基流动（默认）
await AIService.sendMessage(role, history, message, provider: 'siliconflow');
```

### Q3: 如何验证 API Key 是否正确？

**A:** 在应用中发送一条消息，如果成功收到回复，说明 API Key 配置正确。

如果出现错误，检查：
1. API Key 是否正确
2. 网络连接是否正常
3. API 配额是否充足

### Q4: `.env` 文件可以提交到 Git 吗？

**A:** **不可以！** `.env` 文件包含敏感信息，不应该提交到 Git。

`.gitignore` 已经配置为忽略 `.env` 文件。

### Q5: 如何与他人共享项目？

**A:** 提供 `.env.example` 文件作为模板：

```bash
# 创建示例文件
cp .env .env.example

# 编辑 .env.example，用占位符替换真实 Key
# 然后提交到 Git
git add .env.example
git commit -m "Add .env.example template"

# 告诉他人复制 .env.example 并填入自己的 API Key
# cp .env.example .env
```

## 📚 相关文件

### `lib/main.dart`
```dart
void main() async {
  await dotenv.load(fileName: ".env");  // 加载 .env
  runApp(const MyApp());
}
```

### `lib/services/ai_service.dart`
```dart
static String? _getApiKey(String provider) {
  switch (provider) {
    case 'openai':
      return dotenv.env['OPENAI_API_KEY'];
    case 'zhipu':
      return dotenv.env['ZHIPU_API_KEY'];
    case 'siliconflow':
      return dotenv.env['SILICONFLOW_API_KEY'];
    default:
      return null;
  }
}
```

### `pubspec.yaml`
```yaml
dependencies:
  flutter_dotenv: ^5.0.2

flutter:
  assets:
    - .env
```

### `.gitignore`
```
.env  # API Key 不会被提交
```

## 🎯 总结

| 项目 | 说明 |
|------|------|
| **存放位置** | `ai_role_play_app/.env` |
| **文件格式** | 纯文本，KEY=VALUE |
| **加载时机** | 应用启动时（`main()` 函数） |
| **读取方式** | `dotenv.env['KEY_NAME']` |
| **安全性** | `.env` 被 Git 忽略，不会泄露 |
| **支持的提供商** | OpenAI、智谱 AI、硅基流动 |

---

现在你知道 API Key 的存放位置和配置方法了！🔐✨
