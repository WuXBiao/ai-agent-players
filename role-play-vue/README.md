# AI 角色扮演 Vue 前端项目

这是一个基于 Vue 3 的前端项目，用于与 AI 角色扮演后端服务进行交互。

## 项目特性

- 使用 Vue 3 Composition API
- 基于 Vite 构建工具
- 使用 Pinia 进行状态管理
- 响应式设计和现代化 UI
- 与 Go 后端服务通过 RESTful API 通信

## 技术栈

- Vue 3
- Vite
- Pinia
- Vue Router
- Axios
- CSS3 (含渐变、动画等效果)

## 项目结构

```
src/
├── assets/          # 静态资源
├── components/      # 公共组件
├── views/           # 页面视图
├── router/          # 路由配置
├── stores/          # 状态管理
├── services/        # API 服务
├── styles/          # 样式文件
├── App.vue          # 根组件
└── main.js          # 入口文件
```

## 安装和运行

1. 安装依赖：
   ```bash
   npm install
   ```

2. 启动开发服务器：
   ```bash
   npm run dev
   ```

3. 构建生产版本：
   ```bash
   npm run build
   ```

4. 预览生产构建：
   ```bash
   npm run preview
   ```

## API 接口

项目通过 Vite 代理与后端服务通信：

- 角色相关接口: `/api/roles`
- 消息相关接口: `/api/messages`

## 开发指南

### 添加新组件

1. 在 `src/components/` 目录下创建新的 Vue 组件
2. 在需要使用的页面中导入并注册组件

### 添加新页面

1. 在 `src/views/` 目录下创建新的页面组件
2. 在 `src/router/index.js` 中添加路由配置

### 修改 API 接口

1. 更新 `src/services/roleService.js` 中的 API 调用
2. 如需要，更新相应的 store 和组件

## 注意事项

- 确保后端服务在 `http://localhost:8080` 上运行
- 开发服务器默认运行在 `http://localhost:3000`