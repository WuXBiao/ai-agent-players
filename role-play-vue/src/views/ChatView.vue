<template>
  <div class="chat-container">
    <Navbar />
    
    <!-- 角色信息头部 -->
    <div class="chat-header" v-if="roleStore.currentRole">
      <div class="role-info">
        <h2>{{ roleStore.currentRole.name }}</h2>
        <p>{{ roleStore.currentRole.description }}</p>
      </div>
      <button class="back-button" @click="goBack">返回角色列表</button>
    </div>
    
    <!-- 加载状态 -->
    <div class="loading-spinner" v-if="roleStore.loading">
      加载中...
    </div>
    
    <!-- 错误信息 -->
    <div class="error-message" v-else-if="roleStore.error">
      {{ roleStore.error }}
    </div>
    
    <!-- 聊天区域 -->
    <div class="chat-area" v-else-if="roleStore.currentRole">
      <div class="messages-container" ref="messagesContainer">
        <MessageBubble
          v-for="message in chatStore.messages"
          :key="message.id"
          :message="message"
          :is-user="message.is_user"
        />
      </div>
      
      <ChatInput
        @send="sendMessage"
        :loading="chatStore.loading"
      />
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
    
    onMounted(async () => {
      // 获取角色信息
      await roleStore.fetchRoleById(props.roleId)
      
      // 获取聊天历史
      if (roleStore.currentRole) {
        await chatStore.fetchChatHistory(props.roleId)
      }
    })
    
    // 监听消息变化，自动滚动到底部
    watch(() => chatStore.messages, () => {
      nextTick(() => {
        if (messagesContainer.value) {
          messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
        }
      })
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
    
    return {
      roleStore,
      chatStore,
      messagesContainer,
      sendMessage,
      goBack
    }
  }
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: #f0f2f5;
}

.chat-header {
  background: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

.role-info h2 {
  margin: 0 0 0.5rem 0;
  color: #333;
  font-size: 1.5rem;
}

.role-info p {
  margin: 0;
  color: #666;
  font-size: 1rem;
}

.back-button {
  background: #f0f2f5;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.3s ease;
}

.back-button:hover {
  background: #e4e6e9;
}

.loading-spinner {
  text-align: center;
  font-size: 1.2rem;
  padding: 2rem;
  color: #667eea;
}

.error-message {
  text-align: center;
  font-size: 1.2rem;
  padding: 2rem;
  color: #e74c3c;
  background-color: #fdf2f2;
  border-radius: 10px;
  border: 1px solid #f5c6cb;
  margin: 1rem;
}

.chat-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.messages-container {
  flex: 1;
  overflow-y: auto;
  padding: 1rem 2rem;
  display: flex;
  flex-direction: column;
}

.messages-container::-webkit-scrollbar {
  width: 6px;
}

.messages-container::-webkit-scrollbar-track {
  background: #f1f1f1;
}

.messages-container::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 3px;
}

.messages-container::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}
</style>