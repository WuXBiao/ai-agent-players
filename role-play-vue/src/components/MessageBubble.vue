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
  margin-bottom: 0.8rem;
  max-width: 80%;
  animation: scaleIn 0.3s ease-out;
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
  padding: 0.6rem 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  position: relative;
  word-wrap: break-word;
  word-break: break-word;
}

.message-bubble:not(.user-message) .message-content {
  background: #f0f0f0;
  color: #333;
  border: none;
  border-bottom-left-radius: 2px;
}

.user-message .message-content {
  background: #e5e7eb;
  color: #333;
  border: none;
  border-bottom-right-radius: 2px;
}

.message-content p {
  margin: 0 0 0.2rem 0;
  line-height: 1.4;
  font-size: 0.85rem;
}

.message-content p:last-child {
  margin-bottom: 0;
}

.message-timestamp {
  font-size: 0.65rem;
  opacity: 0.6;
  text-align: right;
  margin-top: 0.2rem;
  color: rgba(102, 126, 234, 0.6);
}

.user-message .message-timestamp {
  color: rgba(0, 212, 255, 0.5);
}

.message-bubble:not(.user-message) .message-timestamp {
  color: rgba(102, 126, 234, 0.6);
}

/* 加载动画样式 */
.loading-text {
  display: flex;
  align-items: center;
  gap: 0.2rem;
  margin: 0 !important;
}

.dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: #00d4ff;
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