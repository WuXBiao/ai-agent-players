<template>
  <div class="message-bubble" :class="{ 'user-message': isUser, 'loading': message.loading }">
    <div class="message-content">
      <p v-if="message.loading" class="loading-text">
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
      </p>
      <p v-else>{{ message.content }}</p>
      <div class="message-timestamp">{{ message.timestamp }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MessageBubble',
  props: {
    message: {
      type: Object,
      required: true
    },
    isUser: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped>
.message-bubble {
  display: flex;
  margin-bottom: 1.5rem;
  max-width: 75%;
}

.message-bubble:not(.user-message) {
  align-self: flex-start;
  justify-content: flex-start;
}

.user-message {
  align-self: flex-end;
  justify-content: flex-end;
  margin-left: auto;
}

.message-content {
  padding: 1rem 1.5rem;
  border-radius: 18px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: relative;
  word-wrap: break-word;
  word-break: break-word;
}

.message-bubble:not(.user-message) .message-content {
  background: #f0f0f0;
  color: #333;
  border-bottom-left-radius: 4px;
}

.user-message .message-content {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-bottom-right-radius: 4px;
}

.message-content p {
  margin: 0 0 0.5rem 0;
  line-height: 1.6;
  font-size: 0.95rem;
}

.message-content p:last-child {
  margin-bottom: 0;
}

.message-timestamp {
  font-size: 0.75rem;
  opacity: 0.7;
  text-align: right;
  margin-top: 0.3rem;
}

.user-message .message-timestamp {
  color: rgba(255, 255, 255, 0.7);
}

.message-bubble:not(.user-message) .message-timestamp {
  color: #999;
}

/* 加载动画样式 */
.loading-text {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  margin: 0 !important;
}

.dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #999;
  animation: bounce 1.4s infinite ease-in-out both;
}

.dot:nth-child(1) {
  animation-delay: -0.32s;
}

.dot:nth-child(2) {
  animation-delay: -0.16s;
}

@keyframes bounce {
  0%, 80%, 100% {
    opacity: 0.5;
    transform: scale(0.8);
  }
  40% {
    opacity: 1;
    transform: scale(1);
  }
}
</style>