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
    <div class="loading-spinner" v-if="roleStore.loading || chatStore.loading">
      加载中...
    </div>
    
    <!-- 错误信息 -->
    <div class="error-message" v-else-if="roleStore.error || chatStore.error">
      {{ roleStore.error || chatStore.error }}
    </div>
    
    <!-- 聊天区域 -->
    <div class="chat-area" v-else-if="roleStore.currentRole">
      <div class="messages-container" ref="messagesContainer">
        <MessageBubble
          v-for="message in chatStore.messages"
          :key="message.id"
          :message="message"
          :is-user="message.role_id !== roleStore.currentRole.id"
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
      // 发送用户消息
      await chatStore.sendMessage(props.roleId, content)
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