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
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  padding: 1rem;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.input-form {
  display: flex;
  gap: 1rem;
}

.message-input {
  flex: 1;
  padding: 0.8rem 1.2rem;
  border: 2px solid #e1e5e9;
  border-radius: 25px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s ease;
}

.message-input:focus {
  border-color: #667eea;
}

.message-input:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.send-button {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 25px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 80px;
}

.send-button:hover:not(:disabled) {
  transform: scale(1.05);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.send-button:disabled {
  background: #ccc;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}
</style>