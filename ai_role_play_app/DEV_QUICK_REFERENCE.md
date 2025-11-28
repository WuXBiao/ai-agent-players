# ⚡ 开发环境快速参考

## 🚀 5 分钟快速开始

### 1️⃣ 创建 `.env` 文件

```bash
cd ai_role_play_app
touch .env  # Mac/Linux
# 或
type nul > .env  # Windows
```

### 2️⃣ 编辑 `.env` 文件

```env
SILICONFLOW_API_KEY=your-api-key-here
```

### 3️⃣ 运行应用

```bash
flutter clean
flutter pub get
flutter run
```

## 📊 API Key 快速获取

### 硅基流动（推荐）

```
https://www.siliconflow.cn/ → 注册 → 控制台 → 复制 API Key
```

### OpenAI

```
https://platform.openai.com/api-keys → 登录 → 创建 Key → 复制
```

### 智谱 AI

```
https://open.bigmodel.cn/ → 注册 → API 密钥管理 → 复制
```

## 🔍 验证 `.env` 是否加载

### 查看日志

```
✅ .env file loaded successfully
```

### 调试代码

```dart
void main() async {
  await dotenv.load(fileName: ".env");
  print('API Key loaded: ${dotenv.env['SILICONFLOW_API_KEY'] != null}');
  runApp(const MyApp());
}
```

## ❌ 常见错误

### 错误 1：FileNotFoundError

```
E/flutter: [ERROR] Unhandled Exception: Instance of 'FileNotFoundError'
```

**解决：** 创建 `.env` 文件并添加 API Key

### 错误 2：API 密钥未配置

```
Exception: API密钥未配置
```

**解决：** 检查 `.env` 文件中的 API Key 是否正确

### 错误 3：API 请求失败

```
Exception: API请求失败: 401
```

**解决：** 检查 API Key 是否有效、是否过期、是否有配额

## 📁 文件位置

```
ai_role_play_app/
├── .env                    ← 创建这个文件
├── .env.example            ← 参考这个模板
├── .gitignore              ← 已配置忽略 .env
└── pubspec.yaml            ← 不包含 .env
```

## ✅ 检查清单

- [ ] `.env` 文件已创建
- [ ] `.env` 在项目根目录
- [ ] 添加了 API Key
- [ ] 运行 `flutter clean`
- [ ] 运行 `flutter pub get`
- [ ] 运行 `flutter run`
- [ ] 应用启动成功
- [ ] 可以发送消息

## 🔒 安全提示

- ✅ `.env` 在 `.gitignore` 中
- ✅ 不要提交 `.env` 到 Git
- ✅ 不要在代码中硬编码 API Key
- ✅ 不要在日志中输出 API Key
- ✅ 每个开发者有自己的 `.env` 文件

## 📚 详细文档

- `DEV_ENV_SETUP.md` - 完整的开发环境配置指南
- `ENVIRONMENT_SETUP.md` - 环境配置完整指南
- `API_KEY_SECURITY.md` - API Key 安全分析

---

**现在你可以开始开发了！** 🎉
