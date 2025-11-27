# AI Role Play App Go Server

基于 go-zero 框架的 AI 角色扮演应用后端服务。

## 项目结构

```
ai-role-play-app-go-server/
├── etc/                   # 配置文件
├── internal/              # 内部代码
│   ├── config/            # 配置定义
│   ├── handler/           # 请求处理器
│   ├── logic/             # 业务逻辑
│   ├── svc/               # 服务上下文
│   └── types/             # 类型定义
├── go.mod                 # Go 模块定义
├── go.sum                 # Go 依赖校验和
├── main.go                # 程序入口
└── roleplay.api           # API 定义文件
```

## 快速开始

1. 确保已安装 Go 1.24.6
2. 下载依赖包：
   ```bash
   go mod tidy
   ```

3. 启动服务：
   ```bash
   go run main.go
   ```

   或者指定配置文件：
   ```bash
   go run main.go -f etc/roleplay-api.yaml
   ```

4. 服务默认运行在 `http://localhost:8080`

## API 接口

- `GET /roles` - 获取角色列表
- `GET /roles/:id` - 获取角色详情
- `POST /messages` - 发送消息
- `GET /messages/:role_id` - 获取对话历史

## 配置说明

配置文件位于 `etc/roleplay-api.yaml`：

```yaml
Name: ai-role-play-app-go-server  # 服务名称
Host: 0.0.0.0                     # 监听地址
Port: 8080                        # 监听端口
Timeout: 30000                    # 超时时间(毫秒)

# AI服务配置
AiService:
  ApiKey: "${AI_API_KEY}"         # AI服务API密钥(从环境变量读取)
  Model: "gpt-4"                  # 使用的模型
  Timeout: 60000                  # AI请求超时时间(毫秒)

# 数据库配置
DataSource:
  Host: "localhost"               # 数据库主机
  Port: 3306                      # 数据库端口
  Database: "roleplay"            # 数据库名
  Username: "root"                # 用户名
  Password: "${DB_PASSWORD}"      # 密码(从环境变量读取)
```

## 开发指南

### 添加新的 API 接口

1. 修改 `roleplay.api` 文件定义新的接口
2. 运行以下命令生成代码：
   ```bash
   goctl api go -api roleplay.api -dir .
   ```
3. 在对应的 logic 文件中实现业务逻辑

### 项目生成命令

该项目使用 go-zero 的 api 模式生成：
```bash
goctl api new roleplay
```

然后手动调整了目录结构和模块名称。