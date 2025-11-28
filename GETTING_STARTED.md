# 🚀 快速入门指南

欢迎！这个指南将帮助你快速上手 AI 角色扮演应用。

## 📋 目录

- [系统要求](#系统要求)
- [5 分钟快速开始](#5-分钟快速开始)
- [详细安装步骤](#详细安装步骤)
- [验证安装](#验证安装)
- [常见问题](#常见问题)
- [下一步](#下一步)

---

## 系统要求

### 最低要求

| 组件 | 版本 | 说明 |
|------|------|------|
| **Go** | 1.24+ | 后端服务 |
| **Python** | 3.9+ | AI 服务 |
| **Node.js** | 16+ | 前端构建 |
| **RAM** | 4GB+ | 运行所有服务 |
| **磁盘** | 2GB+ | 依赖和代码 |

### 操作系统

- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu 20.04+)

---

## 5 分钟快速开始

### 步骤 1：克隆项目

```bash
git clone https://github.com/yourusername/ai-role-play.git
cd ai-role-play
```

### 步骤 2：配置 API Key

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env，添加你的 API Key
# 使用你喜欢的编辑器打开 .env
```

**获取 API Key：**
- **OpenAI**: https://platform.openai.com/api-keys
- **智谱 AI**: https://open.bigmodel.cn/
- **硅基流动**: https://cloud.siliconflow.cn/

### 步骤 3：启动所有服务

⚠️ **重要**：启动顺序必须是 Python → Go → Vue

#### 方式 A：使用脚本（推荐）

**Windows:**
```bash
# 创建 start-all.bat
@echo off
REM 1. 先启动 Python gRPC 服务
start "Python Server" cmd /k "cd server-python && python grpc/server.py"

REM 等待 Python 服务启动
timeout /t 3

REM 2. 再启动 Go 服务
start "Go Server" cmd /k "cd server-go && go run main.go"

REM 等待 Go 服务启动
timeout /t 2

REM 3. 最后启动 Vue 前端
start "Vue Frontend" cmd /k "cd role-play-vue && npm install && npm run dev"
```

**Linux/Mac:**
```bash
# 创建 start-all.sh
#!/bin/bash

# 1. 先启动 Python gRPC 服务
cd server-python && python grpc/server.py &
sleep 3

# 2. 再启动 Go 服务
cd ../server-go && go run main.go &
sleep 2

# 3. 最后启动 Vue 前端
cd ../role-play-vue && npm install && npm run dev &
```

#### 方式 B：手动启动（推荐用这个方式）

**终端 1 - Python gRPC 服务（必须先启动！）：**
```bash
cd server-python
pip install -r requirements.txt
python grpc/server.py
# 输出: gRPC server running on port 50051
```

**终端 2 - Go 后端服务：**
```bash
cd server-go
go mod tidy
go run main.go
# 输出: Starting server at 0.0.0.0:8080...
```

**终端 3 - Vue 前端：**
```bash
cd role-play-vue
npm install
npm run dev
# 输出: Local: http://localhost:5173/
```

### 步骤 4：访问应用

打开浏览器访问：
```
http://localhost:5173
```

🎉 完成！你现在可以开始使用应用了。

---

## 详细安装步骤

### 1. 安装 Go

#### Windows

1. 下载 Go：https://golang.org/dl/
2. 运行安装程序
3. 验证安装：
   ```bash
   go version
   ```

#### macOS

```bash
# 使用 Homebrew
brew install go

# 验证
go version
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt-get install golang-go

# 验证
go version
```

### 2. 安装 Python

#### Windows

1. 下载 Python：https://www.python.org/downloads/
2. 运行安装程序（勾选 "Add Python to PATH"）
3. 验证安装：
   ```bash
   python --version
   ```

#### macOS

```bash
# 使用 Homebrew
brew install python3

# 验证
python3 --version
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# 验证
python3 --version
```

### 3. 安装 Node.js

#### Windows

1. 下载 Node.js：https://nodejs.org/
2. 运行安装程序
3. 验证安装：
   ```bash
   node --version
   npm --version
   ```

#### macOS

```bash
# 使用 Homebrew
brew install node

# 验证
node --version
npm --version
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt-get install nodejs npm

# 验证
node --version
npm --version
```

### 4. 克隆项目

```bash
git clone https://github.com/yourusername/ai-role-play.git
cd ai-role-play
```

### 5. 配置环境变量

```bash
# 复制模板
cp .env.example .env

# 编辑 .env 文件，添加你的 API Key
```

**需要配置的变量：**

```env
# 至少配置一个 LLM 的 API Key
OPENAI_API_KEY=sk-your-key-here
# 或
ZHIPU_API_KEY=your-key-here
# 或
SILICONFLOW_API_KEY=sk-your-key-here
```

### 6. 安装依赖

#### Go 依赖

```bash
cd server-go
go mod tidy
cd ..
```

#### Python 依赖

```bash
cd server-python
pip install -r requirements.txt
cd ..
```

#### Node.js 依赖

```bash
cd role-play-vue
npm install
npm run dev
# 输出: Local: http://localhost:5173/
```

### 8. 访问应用

打开浏览器：
```
http://localhost:5173
```

---

## 验证安装

### 检查 Go 服务

```bash
# 测试 API
curl http://localhost:8080/roles

# 预期输出:
# {"roles":[{"id":1,"name":"🧙‍♂️ 智慧导师",...}]}
```

### 检查 Python 服务

```bash
cd server-python
python grpc/test_grpc_connection.py

# 预期输出:
# Successfully connected to gRPC server
# Available roles: [...]
```

### 检查 Web 前端

在浏览器中访问：
```
http://localhost:5173
```

应该看到：
- ✅ 首页（"AI虚拟角色" 标题）
- ✅ "进入" 按钮
- ✅ 功能卡片

---

## 常见问题

### Q: 启动时出现 "port already in use" 错误

**A:** 某个端口已被占用。解决方案：

```bash
# 查找占用端口的进程
# Windows
netstat -ano | findstr :8080

# Linux/Mac
lsof -i :8080

# 杀死进程或使用不同的端口
```

### Q: "API Key 无效" 错误

**A:** 检查：
1. API Key 是否正确复制
2. 是否在 `.env` 文件中设置
3. API 配额是否充足
4. 网络连接是否正常

### Q: "无法连接到 gRPC 服务" 错误

**A:** 确保：
1. Python 服务已启动：`python grpc/server.py`
2. 端口 50051 未被占用
3. 防火墙未阻止连接

### Q: "npm install 失败"

**A:** 尝试：
```bash
# 清除缓存
npm cache clean --force

# 重新安装
npm install

# 或使用 yarn
npm install -g yarn
yarn install
```

### Q: "Go mod tidy 失败"

**A:** 尝试：
```bash
# 删除 go.sum
rm go.sum

# 重新下载依赖
go mod tidy

# 或设置代理
go env -w GOPROXY=https://goproxy.cn,direct
go mod tidy
```

### Q: "Python 依赖安装失败"

**A:** 尝试：
```bash
# 升级 pip
python -m pip install --upgrade pip

# 使用清华源
pip install -r requirements.txt -i https://pypi.tsinghua.edu.cn/simple

# 或使用阿里源
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

---

## 下一步

### 1. 探索应用

- 访问首页
- 查看角色列表
- 与 AI 角色聊天
- 重置对话

### 2. 阅读文档

- [项目 README](./README.md) - 项目概述
- [Go 服务文档](./server-go/README.md) - 后端 API
- [Python 服务文档](./server-python/README.md) - AI 服务
- [Vue 前端文档](./role-play-vue/README.md) - 前端开发

### 3. 开始开发

- [贡献指南](./CONTRIBUTING.md) - 如何贡献代码
- 修改角色配置
- 添加新功能
- 优化性能

### 4. 部署应用

- Docker 容器化
- 云平台部署（AWS、Azure、Google Cloud）
- 移动端打包（Android APP）

---

## 获取帮助

### 遇到问题？

1. 📖 查看 [常见问题](#常见问题)
2. 🔍 搜索 [GitHub Issues](https://github.com/yourusername/ai-role-play/issues)
3. 💬 创建新 Issue
4. 📧 发送邮件给维护者

### 有想法？

- 🌟 给项目 Star
- 🍴 Fork 项目
- 📝 提交 Pull Request
- 💡 提出功能建议

---

## 快速命令参考

```bash
# ⚠️ 启动顺序很重要：Python → Go → Vue

# 1. 启动 Python gRPC 服务（必须先启动！）
cd server-python && python grpc/server.py &

# 2. 启动 Go 后端服务
cd ../server-go && go run main.go &

# 3. 启动 Vue 前端
cd ../role-play-vue && npm run dev &

# 停止所有服务
# Windows: Ctrl+C in each terminal
# Linux/Mac: pkill -f "python grpc/server.py" && pkill -f "go run main.go"

# 查看日志
tail -f server-python/logs/app.log
tail -f server-go/logs/app.log

# 测试 API
curl http://localhost:8080/roles
curl http://localhost:8080/roles/1

# 测试 gRPC 连接
cd server-python && python grpc/test_grpc_connection.py

# 重新安装依赖
go mod tidy
pip install -r requirements.txt --force-reinstall
npm install --force
```

---

## 下一步资源

- [Go 学习资源](https://golang.org/doc/)
- [Python 学习资源](https://docs.python.org/)
- [Vue 3 学习资源](https://v3.vuejs.org/)
- [gRPC 学习资源](https://grpc.io/docs/)

---

祝你使用愉快！如有任何问题，欢迎提出 Issue。🚀
