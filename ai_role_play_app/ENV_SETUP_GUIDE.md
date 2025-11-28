# 🔑 环境变量配置指南

## 问题说明

应用启动时出现以下错误：

```
E/flutter: [ERROR] Unhandled Exception: Instance of 'FileNotFoundError'
E/flutter: #0 DotEnv._getEntriesFromFile (package:flutter_dotenv/src/dotenv.dart:172:7)
```

**原因：** `.env` 文件不存在或无法找到。

## ✅ 解决方案

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

### 步骤 2️⃣：添加 API Key

编辑 `.env` 文件，添加你的 API Key：

```env
# OpenAI API Key（可选）
OPENAI_API_KEY=sk-your-openai-api-key-here

# 智谱 AI API Key（可选）
ZHIPU_API_KEY=your-zhipu-api-key-here

# 硅基流动 API Key（推荐）
SILICONFLOW_API_KEY=your-siliconflow-api-key-here
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

### 步骤 4️⃣：验证配置

运行应用：

```bash
flutter run
```

应该看到应用正常启动，没有 `.env` 文件错误。

## 📋 .env 文件位置

```
ai_role_play_app/
├── .env                    ← 在这里创建
├── .gitignore              ← 已配置忽略 .env
├── pubspec.yaml
├── lib/
│   ├── main.dart
│   └── services/
│       └── ai_service.dart
└── ...
```

## 🔒 安全性说明

### ✅ 已实施的安全措施

1. **`.env` 不在 Git 中**
   ```
   # .gitignore
   .env  ← 防止 API Key 被提交到 Git
   ```

2. **`.env` 不在 APK 中**
   ```yaml
   # pubspec.yaml
   flutter:
     assets:
       - assets/  ← 只包含 assets 目录
       # .env 不在这里
   ```

3. **应用启动时处理缺失的 `.env`**
   ```dart
   // lib/main.dart
   try {
     await dotenv.load(fileName: ".env");
   } catch (e) {
     debugPrint('Warning: .env file not found.');
   }
   ```

4. **API 调用时验证 API Key**
   ```dart
   // lib/services/ai_service.dart
   if (apiKey == null || apiKey.isEmpty) {
     throw Exception('API密钥未配置');
   }
   ```

### ⚠️ 重要提示

```
❌ 不要：
- 将 .env 文件提交到 Git
- 将 API Key 硬编码到代码中
- 在日志中输出 API Key
- 将 API Key 分享给他人

✅ 应该：
- 将 .env 添加到 .gitignore
- 每个开发者有自己的 .env 文件
- 定期轮换 API Key
- 使用后端服务器管理 API Key（生产环境）
```

## 🚀 开发环境配置

### 完整的 .env 示例

```env
# 硅基流动（推荐用于开发）
SILICONFLOW_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx

# OpenAI（可选）
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx

# 智谱 AI（可选）
ZHIPU_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```

### 验证 API Key 是否有效

运行应用后，尝试发送消息。如果 API Key 有效，应该收到 AI 的响应。

## 📱 生产环境配置

### 推荐方案

在生产环境中，**不要在应用中存储 API Key**。使用以下方案之一：

#### 方案 1：后端服务器（最安全）

```
用户手机 → Flutter 应用 → 你的后端服务器 → AI API
         （无 API Key）    （有 API Key）
```

**优点：**
- ✅ API Key 完全隐藏
- ✅ 可以集中管理
- ✅ 可以添加速率限制

#### 方案 2：Firebase Remote Config

```dart
// 从 Firebase 获取 API Key
final remoteConfig = FirebaseRemoteConfig.instance;
await remoteConfig.fetchAndActivate();
final apiKey = remoteConfig.getString('SILICONFLOW_API_KEY');
```

**优点：**
- ✅ 动态更新 API Key
- ✅ Google 官方支持
- ✅ 无需修改应用代码

#### 方案 3：环境变量（CI/CD）

```bash
# GitHub Actions 或其他 CI/CD
export SILICONFLOW_API_KEY=sk-xxxxx
flutter build apk
```

**优点：**
- ✅ API Key 不在代码中
- ✅ 自动化构建

## ❓ 常见问题

### Q1: .env 文件找不到怎么办？

**A:** 确保：
1. `.env` 文件在项目根目录
2. 文件名正确（`.env`，不是 `env` 或 `.env.txt`）
3. 文件有内容（不是空文件）

```bash
# 检查文件是否存在
ls -la .env  # Mac/Linux
dir .env     # Windows
```

### Q2: API Key 无效怎么办？

**A:** 
1. 检查 API Key 是否正确复制
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

### Q4: 如何在多个开发者之间共享 API Key？

**A:** 不要共享 API Key！每个开发者应该：

1. 有自己的 `.env` 文件
2. 有自己的 API Key
3. `.env` 文件在 `.gitignore` 中

```bash
# 创建 .env.example 作为模板
cp .env .env.example

# 编辑 .env.example，移除实际的 API Key
# 提交 .env.example 到 Git
git add .env.example
git commit -m "Add .env.example template"

# 其他开发者复制模板
cp .env.example .env

# 编辑 .env，添加自己的 API Key
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

## 📚 相关文件

- `API_KEY_SETUP.md`：API Key 配置指南
- `API_KEY_SECURITY.md`：API Key 安全分析
- `lib/main.dart`：应用入口（已更新）
- `lib/services/ai_service.dart`：AI 服务（已配置）
- `.gitignore`：Git 忽略配置（已配置）

## 🎯 快速开始

### 5 分钟快速配置

```bash
# 1. 创建 .env 文件
cd ai_role_play_app
touch .env

# 2. 添加 API Key
# 编辑 .env，添加：
# SILICONFLOW_API_KEY=your-api-key

# 3. 运行应用
flutter run

# 完成！
```

## ✅ 验证清单

- [ ] 创建了 `.env` 文件
- [ ] 添加了 API Key
- [ ] 应用可以正常启动
- [ ] 可以发送消息并收到响应
- [ ] `.env` 在 `.gitignore` 中
- [ ] 没有将 API Key 提交到 Git

---

**总结：** 创建 `.env` 文件并添加 API Key，应用就可以正常运行了！🚀✨
