# 🔧 开发环境 .env 配置指南

## 📋 问题说明

在开发环境中，你需要能够访问 `.env` 文件来获取 API Key。当前配置中，`.env` 不被打包到 APK 中（为了安全性），但在开发环境中应该能够正常加载。

## ✅ 解决方案

### 步骤 1️⃣：创建 `.env` 文件

在项目根目录创建 `.env` 文件：

```bash
cd ai_role_play_app
touch .env  # Mac/Linux
# 或
type nul > .env  # Windows
```

### 步骤 2️⃣：添加 API Key

编辑 `.env` 文件，添加你的 API Key：

```env
# 硅基流动 API Key（推荐）
SILICONFLOW_API_KEY=your-siliconflow-api-key-here

# OpenAI API Key（可选）
OPENAI_API_KEY=sk-your-openai-api-key-here

# 智谱 AI API Key（可选）
ZHIPU_API_KEY=your-zhipu-api-key-here
```

### 步骤 3️⃣：验证 `.env` 文件

确保 `.env` 文件在项目根目录：

```bash
# Mac/Linux
ls -la .env

# Windows
dir .env
```

输出应该显示 `.env` 文件存在。

### 步骤 4️⃣：运行应用

```bash
# 清理构建
flutter clean

# 获取依赖
flutter pub get

# 运行应用（开发环境）
flutter run
```

## 🔍 工作原理

### 开发环境（`flutter run`）

在开发环境中运行应用时：

```
1. Flutter 启动应用
2. main.dart 执行 dotenv.load(fileName: ".env")
3. .env 文件从项目根目录加载
4. API Key 被读取到内存
5. 应用可以正常使用 API
```

### 发布环境（`flutter build apk`）

在构建 APK 时：

```
1. Flutter 构建应用
2. .env 文件 NOT 被打包到 APK（安全性）
3. 用户安装应用时，没有 .env 文件
4. 应用启动时，dotenv.load() 会失败
5. 应用优雅地处理失败，继续运行
6. 生产环境应该使用后端服务器或 Firebase Remote Config
```

## 📁 文件结构

### 开发环境

```
ai_role_play_app/
├── .env                    ← 你创建的文件（包含 API Key）
├── .env.example            ← 模板文件（已提供）
├── .gitignore              ← 忽略 .env（防止提交）
├── pubspec.yaml            ← 不包含 .env 资源
├── lib/
│   ├── main.dart           ← 优雅处理缺失的 .env
│   └── services/
│       └── ai_service.dart ← 验证 API Key
└── ...
```

### 发布环境

```
app-release.apk
├── assets/                 ← 只包含这个
├── lib/                    ← 应用代码
└── ...
# .env 不在 APK 中 ✅
```

## 🚀 快速开始（开发环境）

### 1. 复制模板

```bash
cp .env.example .env
```

### 2. 编辑 `.env`

```bash
# 使用你喜欢的编辑器打开 .env
# 添加你的 API Key
```

### 3. 运行应用

```bash
flutter run
```

### 4. 测试

- 打开应用
- 选择一个角色
- 发送一条消息
- 应该收到 AI 的响应

## 📊 API Key 获取

### 硅基流动（推荐）

```
1. 访问：https://www.siliconflow.cn/
2. 点击"注册"或"登录"
3. 进入"控制台"
4. 找到"API Key"部分
5. 复制你的 API Key
6. 粘贴到 .env 文件中
```

**示例：**
```env
SILICONFLOW_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

### OpenAI

```
1. 访问：https://platform.openai.com/api-keys
2. 登录你的账户
3. 点击"Create new secret key"
4. 复制 API Key
5. 粘贴到 .env 文件中
```

**示例：**
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

### 智谱 AI

```
1. 访问：https://open.bigmodel.cn/
2. 登录你的账户
3. 进入"API 密钥管理"
4. 创建新的 API Key
5. 复制 API Key
6. 粘贴到 .env 文件中
```

**示例：**
```env
ZHIPU_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```

## 🔒 安全性说明

### 开发环境

✅ **安全做法：**
- 创建 `.env` 文件（本地开发）
- 添加你的 API Key
- `.env` 在 `.gitignore` 中（不提交到 Git）
- 每个开发者有自己的 `.env` 文件

❌ **不安全做法：**
- 将 `.env` 提交到 Git
- 将 API Key 硬编码到代码中
- 在日志中输出 API Key
- 将 API Key 分享给他人

### 生产环境

✅ **推荐方案：**
- 使用后端服务器管理 API Key
- 使用 Firebase Remote Config
- 使用环境变量（CI/CD）
- 不在应用中存储 API Key

## 🔧 代码工作流程

### `lib/main.dart`

```dart
void main() async {
  // 尝试加载 .env 文件
  try {
    await dotenv.load(fileName: ".env");
    debugPrint('✅ .env file loaded successfully');
  } catch (e) {
    // 开发环境：打印警告
    // 生产环境：继续运行（使用其他方式获取 API Key）
    debugPrint('⚠️ Warning: .env file not found. $e');
  }
  runApp(const MyApp());
}
```

### `lib/services/ai_service.dart`

```dart
static String? _getApiKey(String provider) {
  switch (provider) {
    case 'siliconflow':
      return dotenv.env['SILICONFLOW_API_KEY'];
    case 'openai':
      return dotenv.env['OPENAI_API_KEY'];
    case 'zhipu':
      return dotenv.env['ZHIPU_API_KEY'];
    default:
      return null;
  }
}

static Future<String> sendMessage(...) async {
  final apiKey = _getApiKey(provider);
  if (apiKey == null || apiKey.isEmpty) {
    throw Exception('API密钥未配置');
  }
  // 继续处理请求
}
```

## ✅ 验证清单

### 创建 `.env` 前

- [ ] 项目根目录位置正确
- [ ] 有权限创建文件

### 创建 `.env` 后

- [ ] `.env` 文件已创建
- [ ] `.env` 在项目根目录（与 `pubspec.yaml` 同级）
- [ ] `.env` 在 `.gitignore` 中
- [ ] `.env` 不是空文件

### 配置 API Key 后

- [ ] 添加了 API Key
- [ ] API Key 格式正确（没有多余空格）
- [ ] 没有在 API Key 周围添加引号
- [ ] 没有在 API Key 中包含注释符号

### 运行应用后

- [ ] 运行 `flutter clean`
- [ ] 运行 `flutter pub get`
- [ ] 运行 `flutter run`
- [ ] 应用启动时没有 `.env` 错误
- [ ] 可以发送消息
- [ ] 收到 AI 的响应

## ❓ 常见问题

### Q1: 为什么 `.env` 不在 APK 中？

**A:** 这是安全性考虑。API Key 是敏感信息，不应该被打包到 APK 中。任何人都可以解包 APK 并获得 API Key。

### Q2: 开发环境中 `.env` 在哪里加载？

**A:** 在开发环境中，`flutter run` 命令会从项目根目录加载 `.env` 文件。这不会被打包到 APK 中。

### Q3: 如何验证 `.env` 是否被正确加载？

**A:** 查看应用启动时的日志：

```
✅ .env file loaded successfully
```

或者在代码中添加调试输出：

```dart
void main() async {
  await dotenv.load(fileName: ".env");
  print('API Key: ${dotenv.env['SILICONFLOW_API_KEY']}');
  runApp(const MyApp());
}
```

### Q4: 如果 `.env` 文件找不到怎么办？

**A:** 检查以下几点：

```
1. ✅ .env 文件是否在项目根目录
2. ✅ 文件名是否正确（.env，不是 env 或 .env.txt）
3. ✅ 文件是否有内容（不是空文件）
4. ✅ 是否运行了 flutter clean
5. ✅ 是否运行了 flutter pub get
```

### Q5: 如何在多个开发者之间共享配置？

**A:** 使用 `.env.example` 作为模板：

```bash
# 1. `.env.example` 已经提供
# 2. 其他开发者复制模板
cp .env.example .env

# 3. 编辑 .env，添加自己的 API Key
# 4. .env 在 .gitignore 中，不会被提交
```

### Q6: 生产环境应该如何处理 API Key？

**A:** 不要在应用中存储 API Key。使用以下方案之一：

#### 方案 1：后端服务器

```
用户手机 → Flutter 应用 → 你的后端服务器 → AI API
         （无 API Key）    （有 API Key）
```

#### 方案 2：Firebase Remote Config

```dart
final remoteConfig = FirebaseRemoteConfig.instance;
await remoteConfig.fetchAndActivate();
final apiKey = remoteConfig.getString('SILICONFLOW_API_KEY');
```

#### 方案 3：环境变量（CI/CD）

```yaml
# GitHub Actions
- run: flutter build apk
  env:
    SILICONFLOW_API_KEY: ${{ secrets.SILICONFLOW_API_KEY }}
```

## 📚 相关文件

- `.env` - 你创建的文件（包含 API Key）
- `.env.example` - 模板文件（已提供）
- `.gitignore` - Git 忽略配置（已更新）
- `lib/main.dart` - 应用入口（已更新）
- `lib/services/ai_service.dart` - AI 服务（已配置）
- `ENVIRONMENT_SETUP.md` - 完整的环境配置指南
- `API_KEY_SECURITY.md` - API Key 安全分析

## 🎯 总结

### 开发环境

```bash
# 1. 创建 .env 文件
touch .env

# 2. 添加 API Key
# 编辑 .env，添加：
# SILICONFLOW_API_KEY=your-api-key

# 3. 运行应用
flutter run

# ✅ 完成！应用可以访问 .env 中的 API Key
```

### 发布环境

```bash
# 1. 构建 APK
flutter build apk --release

# 2. .env 不被打包到 APK
# 3. 用户需要通过其他方式获取 API Key
# （后端服务器、Firebase Remote Config 等）
```

---

**现在你可以在开发环境中正常使用 `.env` 文件了！** 🚀✨
