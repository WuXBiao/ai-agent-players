# 🔧 环境配置完整指南

## 📋 问题回顾

应用启动时出现错误：

```
E/flutter: [ERROR] Unhandled Exception: Instance of 'FileNotFoundError'
E/flutter: #0 DotEnv._getEntriesFromFile (package:flutter_dotenv/src/dotenv.dart:172:7)
```

**原因：** `.env` 文件不存在或无法找到。

## ✅ 完整解决方案

### 步骤 1️⃣：创建 `.env` 文件

在项目根目录创建 `.env` 文件：

```bash
# 进入项目目录
cd ai_role_play_app

# 创建 .env 文件
touch .env  # Mac/Linux
# 或
type nul > .env  # Windows
```

### 步骤 2️⃣：配置 API Key

编辑 `.env` 文件，添加你的 API Key：

```env
# 硅基流动 API Key（推荐）
SILICONFLOW_API_KEY=your-api-key-here

# OpenAI API Key（可选）
OPENAI_API_KEY=sk-your-api-key-here

# 智谱 AI API Key（可选）
ZHIPU_API_KEY=your-api-key-here
```

### 步骤 3️⃣：获取 API Key

#### 硅基流动（推荐）

```
1. 访问：https://www.siliconflow.cn/
2. 注册账户
3. 进入控制台
4. 复制 API Key
5. 粘贴到 .env 文件
```

#### OpenAI

```
1. 访问：https://platform.openai.com/api-keys
2. 登录账户
3. 创建新的 API Key
4. 复制 API Key
5. 粘贴到 .env 文件
```

#### 智谱 AI

```
1. 访问：https://open.bigmodel.cn/
2. 注册账户
3. 进入 API 密钥管理
4. 创建新的 API Key
5. 复制 API Key
6. 粘贴到 .env 文件
```

### 步骤 4️⃣：运行应用

```bash
# 清理构建
flutter clean

# 获取依赖
flutter pub get

# 运行应用
flutter run
```

## 🔒 安全配置

### 已实施的安全措施

#### 1. `.env` 不在 Git 中

```
# .gitignore
.env  ← 防止 API Key 被提交到 Git
```

#### 2. `.env` 不在 APK 中

```yaml
# pubspec.yaml
flutter:
  assets:
    - assets/  ← 只包含 assets 目录
    # .env 不在这里
```

#### 3. 应用启动时处理缺失的 `.env`

```dart
// lib/main.dart
try {
  await dotenv.load(fileName: ".env");
} catch (e) {
  debugPrint('Warning: .env file not found.');
}
```

#### 4. API 调用时验证 API Key

```dart
// lib/services/ai_service.dart
if (apiKey == null || apiKey.isEmpty) {
  throw Exception('API密钥未配置');
}
```

### 安全最佳实践

#### ✅ 应该做

- ✅ 创建 `.env` 文件
- ✅ 添加 API Key
- ✅ 将 `.env` 添加到 `.gitignore`
- ✅ 每个开发者有自己的 `.env` 文件
- ✅ 定期轮换 API Key
- ✅ 使用后端服务器管理 API Key（生产环境）

#### ❌ 不应该做

- ❌ 将 `.env` 提交到 Git
- ❌ 将 API Key 硬编码到代码中
- ❌ 在日志中输出 API Key
- ❌ 将 API Key 分享给他人
- ❌ 在 APK 中打包 `.env` 文件

## 📁 文件结构

### 项目根目录

```
ai_role_play_app/
├── .env                    ← 你需要创建（包含 API Key）
├── .env.example            ← 模板文件（已创建）
├── .gitignore              ← 已配置忽略 .env
├── pubspec.yaml            ← 已配置（不包含 .env）
├── lib/
│   ├── main.dart           ← 已更新（处理缺失的 .env）
│   └── services/
│       └── ai_service.dart ← 已配置（验证 API Key）
└── ...
```

### `.env` 文件内容

```env
# 硅基流动 API Key（推荐用于开发）
SILICONFLOW_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx

# OpenAI API Key（可选）
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx

# 智谱 AI API Key（可选）
ZHIPU_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```

## 🚀 快速开始（3 分钟）

### 1. 复制模板

```bash
cp .env.example .env
```

### 2. 编辑 `.env`

```bash
# 编辑 .env 文件，添加你的 API Key
# 使用你喜欢的编辑器打开 .env
```

### 3. 运行应用

```bash
flutter run
```

## 📊 配置检查清单

### 创建前

- [ ] 项目根目录位置正确
- [ ] 有权限创建文件

### 创建后

- [ ] `.env` 文件已创建
- [ ] `.env` 在项目根目录
- [ ] `.env` 在 `.gitignore` 中
- [ ] `.env.example` 已创建（模板）

### 配置后

- [ ] 添加了 API Key
- [ ] API Key 格式正确
- [ ] 没有多余的空格或引号
- [ ] 没有将 `.env` 提交到 Git

### 运行后

- [ ] 应用启动时没有 `.env` 错误
- [ ] 可以发送消息
- [ ] 收到 AI 的响应
- [ ] 没有 API Key 错误

## ❓ 常见问题

### Q1: `.env` 文件找不到怎么办？

**A:** 确保：
1. `.env` 文件在项目根目录（与 `pubspec.yaml` 同级）
2. 文件名正确（`.env`，不是 `env` 或 `.env.txt`）
3. 文件有内容（不是空文件）

```bash
# 检查文件是否存在
ls -la .env  # Mac/Linux
dir .env     # Windows
```

### Q2: API Key 无效怎么办？

**A:** 
1. 检查 API Key 是否正确复制（没有多余空格）
2. 检查 API Key 是否过期
3. 检查 API Key 是否有配额
4. 检查网络连接

### Q3: 应用启动时仍然出错怎么办？

**A:** 检查以下几点：

```
1. ✅ .env 文件是否存在
2. ✅ .env 文件是否在项目根目录
3. ✅ API Key 是否正确配置
4. ✅ 是否运行了 flutter pub get
5. ✅ 是否清理了构建：flutter clean
```

### Q4: 如何在多个开发者之间共享配置？

**A:** 使用 `.env.example` 作为模板：

```bash
# 1. 创建 .env.example（已创建）
# 2. 其他开发者复制模板
cp .env.example .env

# 3. 编辑 .env，添加自己的 API Key
# 4. .env 在 .gitignore 中，不会被提交
```

### Q5: 如何在 CI/CD 中配置 API Key？

**A:** 使用环境变量：

```yaml
# GitHub Actions 示例
name: Build

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: subosito/flutter-action@v2
      - run: flutter pub get
      - run: flutter build apk
        env:
          SILICONFLOW_API_KEY: ${{ secrets.SILICONFLOW_API_KEY }}
```

### Q6: 生产环境应该如何配置 API Key？

**A:** 不要在应用中存储 API Key。使用以下方案之一：

#### 方案 1：后端服务器（最安全）

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

## 📚 相关文档

- `ENV_SETUP_GUIDE.md`：详细的环境变量配置指南
- `API_KEY_SETUP.md`：API Key 配置指南
- `API_KEY_SECURITY.md`：API Key 安全分析
- `.env.example`：API Key 配置模板
- `.gitignore`：Git 忽略配置

## 🔧 代码变更

### `lib/main.dart`（已更新）

```dart
void main() async {
  // 尝试加载 .env 文件（如果存在）
  try {
    await dotenv.load(fileName: ".env");
  } catch (e) {
    // .env 文件不存在或无法读取，继续运行
    debugPrint('Warning: .env file not found.');
  }
  runApp(const MyApp());
}
```

### `.gitignore`（已更新）

```
# Environment variables
.env
```

### `pubspec.yaml`（已配置）

```yaml
flutter:
  uses-material-design: true
  assets:
    - assets/  # .env 不在这里
```

## 🎯 总结

| 项目 | 状态 | 说明 |
|------|------|------|
| **`.env` 文件** | 📝 需要创建 | 包含你的 API Key |
| **`.env.example`** | ✅ 已创建 | 模板文件，供参考 |
| **`.gitignore`** | ✅ 已更新 | 防止 `.env` 被提交 |
| **`pubspec.yaml`** | ✅ 已配置 | `.env` 不在 APK 中 |
| **`lib/main.dart`** | ✅ 已更新 | 处理缺失的 `.env` |
| **`lib/services/ai_service.dart`** | ✅ 已配置 | 验证 API Key |

## 🚀 立即开始

```bash
# 1. 创建 .env 文件
touch .env

# 2. 添加 API Key
# 编辑 .env，添加：
# SILICONFLOW_API_KEY=your-api-key

# 3. 运行应用
flutter run

# 完成！✨
```

---

**现在你的应用已经可以正常运行了！** 🎉

如果遇到任何问题，请参考本文档中的常见问题部分。
