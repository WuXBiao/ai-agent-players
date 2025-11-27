<template>
  <div class="chat-input-container">
    <form @submit.prevent="sendMessage" class="input-form">
      <input
        v-model="inputText"
        type="text"
        placeholder="输入消息..."
        class="message-input"
        :disabled="loading"
      />
      <button
        type="submit"
        class="send-button"
        :disabled="!inputText.trim() || loading"
      >
        {{ loading ? '发送中...' : '发送' }}
      </button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'ChatInput',
  props: {
    loading: {
      type: Boolean,
      default: false
    }
  },
  emits: ['send'],
  setup(props, { emit }) {
    const inputText = ref('')

    const sendMessage = () => {
      if (inputText.value.trim() && !props.loading) {
        emit('send', inputText.value.trim())
        inputText.value = ''
      }
    }

    return {
      inputText,
      sendMessage
    }
  }
}
</script>

<style scoped>
.chat-input-container {
  background: white;
  padding: 1.5rem 2rem;
  border-top: 1px solid #e5e5e5;
}

.input-form {
  display: flex;
  gap: 0.8rem;
  max-width: 800px;
  margin: 0 auto;
  width: 100%;
}

.message-input {
  flex: 1;
  padding: 0.9rem 1.2rem;
  border: 1px solid #d1d5db;
  border-radius: 24px;
  font-size: 0.9rem;
  outline: none;
  transition: all 0.3s ease;
  background: white;
  color: #333;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.message-input::placeholder {
  color: #999;
}

.message-input:focus {
  border-color: #9ca3af;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  background: white;
}

.message-input:disabled {
  background-color: #f9fafb;
  cursor: not-allowed;
  opacity: 0.6;
  border-color: #e5e7eb;
}

.send-button {
  background: #667eea;
  color: white;
  border: none;
  padding: 0.9rem 1.2rem;
  border-radius: 24px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 60px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.send-button:hover:not(:disabled) {
  background: #5568d3;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.send-button:active:not(:disabled) {
  transform: scale(0.98);
}

.send-button:disabled {
  background: #d1d5db;
  color: #9ca3af;
  cursor: not-allowed;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
</style>