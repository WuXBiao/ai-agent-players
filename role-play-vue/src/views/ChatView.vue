<template>
  <div class="chat-layout">
    <!-- 左侧边栏 -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <button class="new-chat-btn" @click="startNewChat">
          <span class="icon">↻</span>
          重置对话
        </button>
      </div>
      
      <div class="sidebar-content">
        <div class="chat-history">
          <div class="history-item active">
            <span class="history-title">{{ roleStore.currentRole?.name || '聊天' }}</span>
          </div>
        </div>
      </div>
      
      <div class="sidebar-footer">
        <button class="sidebar-btn" @click="goBack">
          <span class="icon">←</span>
          返回角色列表
        </button>
      </div>
    </aside>
    
    <!-- 主聊天区域 -->
    <div class="main-container">
      <!-- 顶部导航 -->
      <header class="top-header" v-if="roleStore.currentRole">
        <div class="header-content">
          <h1 class="role-name">{{ roleStore.currentRole.name }}</h1>
          <p class="role-desc">{{ roleStore.currentRole.description }}</p>
        </div>
        <div class="header-actions">
          <button class="action-btn">⋯</button>
        </div>
      </header>
      
      <!-- 聊天消息区域 -->
      <div class="chat-main" ref="messagesContainer">
        <!-- 加载状态 -->
        <div class="loading-state" v-if="roleStore.loading">
          <div class="spinner"></div>
          <p>加载中...</p>
        </div>
        
        <!-- 错误信息 -->
        <div class="error-state" v-else-if="roleStore.error">
          <p>{{ roleStore.error }}</p>
        </div>
        
        <!-- 空状态 -->
        <div class="empty-state" v-else-if="chatStore.messages.length === 0">
          <div class="empty-icon">💬</div>
          <p class="empty-text">开始与 {{ roleStore.currentRole?.name }} 对话</p>
          <p class="empty-hint">{{ roleStore.currentRole?.description }}</p>
        </div>
        
        <!-- 消息列表 -->
        <div class="messages-list" v-else>
          <MessageBubble
            v-for="message in chatStore.messages"
            :key="message.id"
            :message="message"
            :is-user="message.is_user"
          />
        </div>
      </div>
      
      <!-- 底部输入区域 -->
      <div class="chat-footer">
        <ChatInput
          @send="sendMessage"
          :loading="chatStore.loading"
        />
        <p class="footer-hint">{{ roleStore.currentRole?.name }} 可能会犯错。请核实重要信息。</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useRoleStore } from '@/stores/roleStore'
import { useChatStore } from '@/stores/roleStore'
import Navbar from '@/components/Navbar.vue'
import MessageBubble from '@/components/MessageBubble.vue'
import ChatInput from '@/components/ChatInput.vue'

export default {
  name: 'ChatView',
  components: {
    Navbar,
    MessageBubble,
    ChatInput
  },
  props: {
    roleId: {
      type: [String, Number],
      required: true
    }
  },
  setup(props) {
    const route = useRoute()
    const router = useRouter()
    const roleStore = useRoleStore()
    const chatStore = useChatStore()
    const messagesContainer = ref(null)
    
    // 滚动到底部的函数
    const scrollToBottom = () => {
      nextTick(() => {
        if (messagesContainer.value) {
          const container = messagesContainer.value
          setTimeout(() => {
            container.scrollTop = container.scrollHeight
          }, 0)
        }
      })
    }
    
    onMounted(async () => {
      // 获取角色信息
      await roleStore.fetchRoleById(props.roleId)
      
      // 获取聊天历史
      if (roleStore.currentRole) {
        await chatStore.fetchChatHistory(props.roleId)
        // 初始化时滚动到底部
        scrollToBottom()
      }
    })
    
    // 监听消息变化，自动滚动到底部
    watch(() => chatStore.messages, () => {
      scrollToBottom()
    }, { deep: true })
    
    const sendMessage = async (content) => {
      // 先添加用户消息到列表
      const userMessage = {
        id: Date.now(),
        role_id: parseInt(props.roleId),
        content: content,
        timestamp: new Date().toLocaleString('zh-CN'),
        is_user: true
      }
      chatStore.messages.push(userMessage)
      
      // 添加加载中的 AI 消息占位符
      const loadingMessage = {
        id: Date.now() + 1,
        role_id: parseInt(props.roleId),
        content: '思考中...',
        timestamp: new Date().toLocaleString('zh-CN'),
        is_user: false,
        loading: true
      }
      chatStore.messages.push(loadingMessage)
      
      // 异步发送消息获取 AI 回复（不等待）
      try {
        const response = await chatStore.sendMessage(props.roleId, content)
        // 替换加载中的消息
        const index = chatStore.messages.findIndex(msg => msg.id === loadingMessage.id)
        if (index !== -1) {
          // 如果 response 已经被添加到列表中，则删除加载消息
          // 否则替换加载消息
          if (response?.id && chatStore.messages.some(msg => msg.id === response.id)) {
            // 删除加载消息
            chatStore.messages.splice(index, 1)
          } else {
            // 替换加载消息
            chatStore.messages[index] = {
              id: loadingMessage.id,
              role_id: parseInt(props.roleId),
              content: response?.content || '抱歉，暂时无法回复',
              timestamp: new Date().toLocaleString('zh-CN'),
              is_user: false
            }
          }
        }
      } catch (error) {
        // 错误时替换为错误消息
        const index = chatStore.messages.findIndex(msg => msg.id === loadingMessage.id)
        if (index !== -1) {
          chatStore.messages[index] = {
            id: loadingMessage.id,
            role_id: parseInt(props.roleId),
            content: '抱歉，发生了错误，请重试',
            timestamp: new Date().toLocaleString('zh-CN'),
            is_user: false
          }
        }
      }
    }
    
    const goBack = () => {
      router.push('/roles')
    }
    
    const startNewChat = () => {
      chatStore.messages = []
    }
    
    return {
      roleStore,
      chatStore,
      messagesContainer,
      sendMessage,
      goBack,
      startNewChat
    }
  }
}
</script>

<style scoped>
  .chat-layout {
    display: flex;
    height: 100vh;
    background: white;
  }

  /* 左侧边栏 */
  .sidebar {
    width: 260px;
    background: #fff;
    border-right: 1px solid #e5e5e5;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    padding: 1rem 0;
  }

  .sidebar-header {
    padding: 0 1rem 1rem;
  }

  .new-chat-btn {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    background: white;
    color: #333;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }

  .new-chat-btn:hover {
    background: #f3f4f6;
    border-color: #9ca3af;
  }

  .sidebar-content {
    flex: 1;
    overflow-y: auto;
    padding: 0 0.5rem;
  }

  .chat-history {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .history-item {
    padding: 0.75rem 1rem;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    color: #666;
    font-size: 0.9rem;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .history-item:hover {
    background: #f3f4f6;
  }

  .history-item.active {
    background: #e5e7eb;
    color: #333;
    font-weight: 600;
  }

  .sidebar-footer {
    padding: 1rem;
    border-top: 1px solid #e5e5e5;
  }

  .sidebar-btn {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    background: white;
    color: #333;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }

  .sidebar-btn:hover {
    background: #f3f4f6;
  }

  /* 主容器 */
  .main-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: white;
  }

  /* 顶部导航 */
  .top-header {
    padding: 1rem 2rem;
    border-bottom: 1px solid #e5e5e5;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: white;
  }

  .header-content {
    flex: 1;
  }

  .role-name {
    margin: 0;
    font-size: 1.1rem;
    font-weight: 700;
    color: #333;
  }

  .role-desc {
    margin: 0.3rem 0 0;
    font-size: 0.85rem;
    color: #999;
  }

  .action-btn {
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
    color: #666;
    transition: color 0.3s ease;
    padding: 0.5rem;
  }

  .action-btn:hover {
    color: #333;
  }

  /* 聊天主区域 */
  .chat-main {
    flex: 1;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 2rem;
    width: 100%;
  }

  .chat-main::-webkit-scrollbar {
    width: 8px;
  }

  .chat-main::-webkit-scrollbar-track {
    background: transparent;
  }

  .chat-main::-webkit-scrollbar-thumb {
    background: #d1d5db;
    border-radius: 4px;
  }

  .chat-main::-webkit-scrollbar-thumb:hover {
    background: #9ca3af;
  }

  .loading-state,
  .error-state,
  .empty-state {
    text-align: center;
    color: #666;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 300px;
  }

  .spinner {
    width: 40px;
    height: 40px;
    border: 3px solid #e5e5e5;
    border-top-color: #667eea;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin: 0 auto 1rem;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  .empty-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
  }

  .empty-text {
    font-size: 1.2rem;
    font-weight: 600;
    color: #333;
    margin-bottom: 0.5rem;
  }

  .empty-hint {
    font-size: 0.9rem;
    color: #999;
  }

  .messages-list {
    width: 100%;
    max-width: 800px;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  /* 底部输入区域 */
  .chat-footer {
    padding: 1.5rem 2rem;
    border-top: 1px solid #e5e5e5;
    background: white;
  }

  .footer-hint {
    text-align: center;
    font-size: 0.75rem;
    color: #999;
    margin-top: 0.75rem;
  }
</style>