# 📱 AI 角色扮演移动应用 - 架构设计

## 项目概览

这是一个基于 **Flutter** 开发的独立移动应用，采用 **分层架构** 设计，直接调用 AI API（OpenAI、智谱 AI、硅基流动）。

## 架构图

```
┌─────────────────────────────────────────────────────────────┐
│                    UI 层（Presentation）                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ RolePlayScreen│  │ RoleSelector │  │  ChatInput   │      │
│  │  (主屏幕)    │  │  (角色选择)  │  │  (输入框)    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│  ┌──────────────┐                                           │
│  │MessageBubble │  (消息气泡)                              │
│  └──────────────┘                                           │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                  业务逻辑层（Service）                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              AIService                               │  │
│  │  - 构建消息历史                                      │  │
│  │  - 调用 AI API                                       │  │
│  │  - 处理多个 LLM 提供商                               │  │
│  │  - 解析 API 响应                                     │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                  数据模型层（Models）                        │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │    Role      │  │   Message    │                        │
│  │  (角色数据)  │  │  (消息数据)  │                        │
│  └──────────────┘  └──────────────┘                        │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                  外部 API 层（External）                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  OpenAI API  │  │ 智谱 AI API  │  │硅基流动 API  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

## 目录结构

```
ai_role_play_app/
├── lib/
│   ├── main.dart                    # 应用入口
│   ├── models/                      # 数据模型
│   │   ├── role.dart               # 角色模型
│   │   └── message.dart            # 消息模型
│   ├── screens/                     # 屏幕/页面
│   │   └── role_play_screen.dart   # 主聊天屏幕
│   ├── services/                    # 业务逻辑服务
│   │   └── ai_service.dart         # AI 调用服务
│   └── widgets/                     # 可复用组件
│       ├── role_selector.dart      # 角色选择器
│       ├── message_bubble.dart     # 消息气泡
│       └── chat_input.dart         # 输入框
├── pubspec.yaml                     # 依赖配置
├── .env                             # 环境变量（API Key）
└── .env.example                     # 环境变量模板
```

## 核心模块说明

### 1. 数据模型层（Models）

#### Role（角色模型）
```dart
class Role {
  final String id;           // 角色唯一标识
  final String name;         // 角色名称
  final String icon;         // 角色图标（emoji）
  final String description;  // 角色描述
  final String prompt;       // 系统提示词
  final String greeting;     // 初始问候语
}
```

**作用**：定义 AI 角色的数据结构，包含角色的人设和提示词。

#### Message（消息模型）
```dart
class Message {
  final String id;           // 消息唯一标识
  final String text;         // 消息内容
  final bool isUser;         // 是否为用户消息
  final DateTime timestamp;  // 时间戳
}
```

**作用**：定义聊天消息的数据结构，区分用户消息和 AI 回复。

### 2. 业务逻辑层（Services）

#### AIService（AI 调用服务）

**核心职责**：
- 管理多个 LLM 提供商的 API 调用
- 构建消息历史
- 处理 API 请求和响应

**关键方法**：
```dart
// 发送消息到 AI
static Future<String> sendMessage(
  Role role,
  List<Message> history,
  String userMessage,
  {String provider = 'siliconflow'}
)

// 构建消息历史
static List<Map<String, dynamic>> _buildMessages(
  String prompt,
  List<Message> history,
  String userMessage
)

// 获取 API 密钥
static String? _getApiKey(String provider)

// 提取响应内容
static String _extractResponseContent(dynamic data, String provider)
```

**支持的 LLM 提供商**：
- **OpenAI**：GPT-3.5-turbo
- **智谱 AI**：GLM-4-Flash
- **硅基流动**：Qwen/Qwen2.5-7B-Instruct

### 3. UI 层（Screens & Widgets）

#### RolePlayScreen（主屏幕）

**职责**：
- 管理应用的整体状态
- 处理角色选择
- 管理消息列表
- 处理消息发送和接收
- 实现自动滚动功能

**关键状态**：
```dart
late ScrollController _scrollController;  // 滚动控制器
Role? selectedRole;                       // 当前选中的角色
final List<Message> messages = [];        // 消息列表
bool _isSending = false;                  // 发送状态
```

**关键方法**：
```dart
void _selectRole(Role role)           // 选择角色
Future<void> _sendMessage(String text) // 发送消息
void _scrollToBottom()                 // 自动滚动到底部
void _resetConversation()              // 重置对话
void _clearChat()                      // 清空聊天
```

#### RoleSelector（角色选择器）

**功能**：
- 水平滚动显示所有可用角色
- 高亮显示当前选中的角色
- 点击选择角色

#### MessageBubble（消息气泡）

**功能**：
- 显示单条消息
- 区分用户消息（右对齐）和 AI 回复（左对齐）
- 不同的样式和颜色

#### ChatInput（输入框）

**功能**：
- 文本输入框
- 发送按钮
- 加载状态显示
- 回车发送支持

### 4. 应用入口（main.dart）

**职责**：
- 加载环境变量（API Key）
- 初始化 Flutter 应用
- 配置主题
- 设置首页

## 数据流向

### 消息发送流程

```
1. 用户输入消息
   ↓
2. ChatInput 触发 onSend 回调
   ↓
3. RolePlayScreen._sendMessage() 被调用
   ↓
4. 添加用户消息到 messages 列表
   ↓
5. 调用 AIService.sendMessage()
   ↓
6. AIService 构建消息历史和请求体
   ↓
7. 发送 HTTP POST 请求到 AI API
   ↓
8. 解析 API 响应
   ↓
9. 添加 AI 回复到 messages 列表
   ↓
10. 自动滚动到最新消息
   ↓
11. UI 更新显示新消息
```

### 消息历史构建

```
系统提示词（System）
  ↓
历史消息（User/Assistant）
  ↓
当前用户消息（User）
```

## 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| **Flutter** | 3.0+ | UI 框架 |
| **Dart** | 3.0+ | 编程语言 |
| **http** | 1.6.0 | HTTP 请求 |
| **flutter_dotenv** | 5.0.2 | 环境变量管理 |
| **Material Design 3** | - | UI 设计系统 |

## 设计模式

### 1. 分层架构
- **UI 层**：负责用户界面和交互
- **业务逻辑层**：处理应用逻辑和数据处理
- **数据模型层**：定义数据结构
- **外部 API 层**：与外部服务通信

### 2. 单一职责原则
- 每个类只负责一个功能
- `AIService` 专门处理 AI 调用
- `RolePlayScreen` 专门处理 UI 逻辑
- 各个 Widget 专注于自己的渲染

### 3. 依赖注入
- 通过构造函数传递依赖
- 降低耦合度

### 4. 状态管理
- 使用 `StatefulWidget` 管理应用状态
- `ScrollController` 管理滚动状态
- `setState()` 触发 UI 更新

## 关键特性

### 1. 多 LLM 支持
- 支持 OpenAI、智谱 AI、硅基流动
- 灵活的 API 切换
- 统一的接口

### 2. 角色扮演
- 8 个预设角色
- 每个角色有独特的系统提示词
- 支持自定义角色

### 3. 消息管理
- 完整的消息历史
- 消息去重和验证
- 时间戳记录

### 4. 用户体验
- 自动滚动到最新消息
- 加载状态提示
- 错误处理和提示
- 流畅的动画

## 扩展性

### 添加新的 LLM 提供商

1. 在 `AIService` 中添加新的 URL 和 API Key 获取方法
2. 在 `_getHeaders()` 中添加请求头配置
3. 在 `_buildRequestBody()` 中添加请求体构建逻辑
4. 在 `_extractResponseContent()` 中添加响应解析逻辑

### 添加新的角色

在 `RolePlayScreen` 的 `roles` 列表中添加新的 `Role` 对象：

```dart
Role(
  id: 'new_role',
  name: '新角色',
  icon: '🎭',
  description: '角色描述',
  prompt: '系统提示词...',
  greeting: '初始问候语',
)
```

### 添加本地数据存储

可以集成 `sqflite` 或 `hive` 来实现：
- 消息历史持久化
- 用户偏好设置
- 离线消息缓存

## 性能优化

1. **消息列表优化**
   - 使用 `ListView.builder()` 实现虚拟化列表
   - 只渲染可见的消息

2. **API 调用优化**
   - 使用异步操作避免阻塞 UI
   - 添加请求超时控制
   - 实现重试机制

3. **内存管理**
   - 及时释放 `ScrollController`
   - 清理不需要的资源

## 安全性

1. **API Key 管理**
   - 使用 `.env` 文件存储敏感信息
   - 不在代码中硬编码 API Key
   - `.env` 文件不提交到版本控制

2. **错误处理**
   - 捕获所有异常
   - 提供用户友好的错误提示
   - 记录错误日志

## 测试策略

### 单元测试
- 测试 `AIService` 的消息构建逻辑
- 测试数据模型的序列化/反序列化

### Widget 测试
- 测试各个 Widget 的渲染
- 测试用户交互

### 集成测试
- 测试完整的消息发送流程
- 测试 API 调用

## 部署

### 构建 APK（Android）
```bash
flutter build apk
```

### 构建 iOS
```bash
flutter build ios
```

### 构建 Web
```bash
flutter build web
```

## 总结

这个项目采用了清晰的分层架构，将 UI、业务逻辑和数据分离，易于维护和扩展。通过支持多个 LLM 提供商和丰富的角色扮演功能，提供了灵活而强大的 AI 交互体验。
