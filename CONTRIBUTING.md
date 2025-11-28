# 🤝 贡献指南

感谢你对 AI 角色扮演应用的兴趣！我们欢迎各种形式的贡献。

## 📋 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
- [开发流程](#开发流程)
- [代码规范](#代码规范)
- [提交 PR](#提交-pr)
- [报告 Bug](#报告-bug)
- [功能建议](#功能建议)

---

## 行为准则

### 我们的承诺

为了营造开放和热情的社区环境，我们承诺：

- 尊重所有贡献者，无论其经验水平
- 接受建设性的批评
- 专注于对社区最有利的事情
- 对其他社区成员表示同情

### 不可接受的行为

以下行为是不可接受的：

- 使用带有性暗示的语言或图像
- 人身攻击、侮辱或贬低评论
- 公开或私下骚扰
- 发布他人的私人信息
- 其他可能被合理认为在专业环境中不适当的行为

---

## 如何贡献

### 1. 报告 Bug

发现 Bug？请提交 Issue！

**提交 Bug 时请包括：**
- 清晰的标题和描述
- 重现步骤
- 实际行为 vs 预期行为
- 截图或日志
- 你的环境信息（OS、浏览器、Go 版本等）

### 2. 建议功能

有好的想法？我们很想听听！

**提交功能建议时请包括：**
- 清晰的用例描述
- 为什么这个功能有用
- 可能的实现方式
- 相关的 Issue 链接

### 3. 改进文档

文档总是可以改进的！

- 修复拼写错误
- 改进清晰度
- 添加示例
- 翻译文档

### 4. 代码贡献

想要贡献代码？太好了！

---

## 开发流程

### 第1步：Fork 项目

```bash
# 在 GitHub 上点击 Fork 按钮
```

### 第2步：克隆你的 Fork

```bash
git clone https://github.com/your-username/ai-role-play.git
cd ai-role-play
```

### 第3步：添加上游远程

```bash
git remote add upstream https://github.com/original-owner/ai-role-play.git
```

### 第4步：创建特性分支

```bash
git checkout -b feature/your-feature-name
# 或修复 Bug
git checkout -b fix/issue-number
```

### 第5步：进行更改

```bash
# 编辑文件
# 测试你的更改
```

### 第6步：提交更改

```bash
git add .
git commit -m "feat: add amazing feature"
```

### 第7步：推送到你的 Fork

```bash
git push origin feature/your-feature-name
```

### 第8步：提交 Pull Request

在 GitHub 上创建 Pull Request，描述你的更改。

---

## 代码规范

### Go 代码规范

遵循 [Effective Go](https://golang.org/doc/effective_go)：

```go
// 好的例子
func (l *GetRolesLogic) GetRoles(req *types.GetRolesRequest) (resp *types.GetRolesResponse, err error) {
    // 实现逻辑
    return resp, nil
}

// 不好的例子
func GetRoles(r *types.GetRolesRequest) (*types.GetRolesResponse, error) {
    // 实现逻辑
    return nil, nil
}
```

**规范：**
- 使用 `camelCase` 命名变量和函数
- 使用 `PascalCase` 命名类型和接口
- 添加注释说明公开函数
- 使用 `gofmt` 格式化代码

### Python 代码规范

遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/)：

```python
# 好的例子
def generate_response(role_id: int, content: str) -> str:
    """生成 AI 回复"""
    response = ai_client.chat.completions.create(...)
    return response.choices[0].message.content

# 不好的例子
def GenerateResponse(roleId, content):
    response = ai_client.chat.completions.create(...)
    return response.choices[0].message.content
```

**规范：**
- 使用 `snake_case` 命名函数和变量
- 使用 `PascalCase` 命名类
- 添加类型提示
- 添加 docstring
- 使用 `black` 格式化代码

### Vue 代码规范

遵循 [Vue 风格指南](https://v3.vuejs.org/style-guide/)：

```vue
<!-- 好的例子 -->
<template>
  <div class="message-bubble">
    <p class="message-content">{{ message.content }}</p>
    <span class="message-time">{{ message.timestamp }}</span>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  message: {
    type: Object,
    required: true
  }
})

const formattedTime = computed(() => {
  return new Date(props.message.timestamp).toLocaleString()
})
</script>

<style scoped>
.message-bubble {
  padding: 1rem;
  border-radius: 8px;
  background: #f0f0f0;
}
</style>
```

**规范：**
- 使用 `kebab-case` 命名 CSS 类
- 使用 `PascalCase` 命名组件
- 使用 `<script setup>` 语法
- 添加 `scoped` 样式
- 使用 `prettier` 格式化代码

---

## 提交 PR

### PR 标题格式

使用以下格式：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type（类型）

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码风格（不影响功能）
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建、依赖等

### Scope（范围）

- `go`: Go 后端
- `python`: Python 服务
- `vue`: Vue 前端
- `app`: Android APP
- `docs`: 文档
- `ci`: CI/CD

### 例子

```
feat(go): add caching layer for role queries

- Implement Redis-based caching
- Add cache invalidation on role updates
- Improve response time by 50%

Closes #123
```

### PR 检查清单

提交 PR 前，请确保：

- [ ] 代码遵循项目的代码规范
- [ ] 添加了必要的注释和文档
- [ ] 添加了测试（如适用）
- [ ] 所有测试都通过
- [ ] 没有引入新的警告
- [ ] 提交信息清晰有意义
- [ ] 更新了相关文档

---

## 报告 Bug

### 提交 Bug 报告

1. 使用清晰的标题
2. 描述确切的步骤来重现问题
3. 提供具体的例子来演示步骤
4. 描述你观察到的行为
5. 解释你期望的行为
6. 包括截图或日志
7. 提供你的环境信息

### Bug 报告模板

```markdown
## 描述
清晰简洁的问题描述。

## 重现步骤
1. 第一步
2. 第二步
3. ...

## 预期行为
应该发生什么。

## 实际行为
实际发生了什么。

## 环境
- OS: [e.g. Windows 10]
- Go Version: [e.g. 1.24.6]
- Python Version: [e.g. 3.9]
- Browser: [e.g. Chrome 120]

## 日志
```
粘贴相关的日志或错误信息
```
```

---

## 功能建议

### 提交功能建议

1. 使用清晰的标题
2. 提供详细的描述
3. 解释为什么这个功能有用
4. 列出可能的实现方式
5. 提供相关的例子或用例

### 功能建议模板

```markdown
## 功能描述
清晰简洁的功能描述。

## 用例
为什么需要这个功能？谁会使用它？

## 建议的实现
如何实现这个功能？

## 替代方案
是否有其他方式来解决这个问题？

## 其他信息
任何其他相关信息。
```

---

## 开发环境设置

### 前置要求

- Git
- Go 1.24+
- Python 3.9+
- Node.js 16+
- Docker（可选）

### 本地开发

```bash
# 克隆项目
git clone https://github.com/your-username/ai-role-play.git
cd ai-role-play

# 安装依赖
cd server-go && go mod tidy && cd ..
cd server-python && pip install -r requirements.txt && cd ..
cd role-play-vue && npm install && cd ..

# 启动服务
# 终端 1: Go 服务
cd server-go && go run main.go

# 终端 2: Python 服务
cd server-python && python grpc/server.py

# 终端 3: Vue 前端
cd role-play-vue && npm run dev
```

### 运行测试

```bash
# Go 测试
cd server-go && go test ./...

# Python 测试
cd server-python && python -m pytest

# Vue 测试
cd role-play-vue && npm run test
```

---

## 获取帮助

- 📖 查看 [README.md](./README.md)
- 💬 在 Issue 中提问
- 📧 发送邮件给维护者
- 🐦 在 Twitter 上联系我们

---

## 许可证

通过贡献，你同意你的贡献将在 MIT 许可证下进行许可。

---

感谢你的贡献！🎉
