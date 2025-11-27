<template>
  <div class="message-bubble" :class="{ 'user-message': isUser }">
    <div class="message-content">
      <p>{{ message.content }}</p>
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
  margin-bottom: 1rem;
  max-width: 80%;
}

.message-bubble:not(.user-message) {
  align-self: flex-start;
}

.user-message {
  align-self: flex-end;
  margin-left: auto;
}

.message-content {
  padding: 1rem 1.5rem;
  border-radius: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: relative;
}

.message-bubble:not(.user-message) .message-content {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  border-bottom-left-radius: 5px;
}

.user-message .message-content {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-bottom-right-radius: 5px;
}

.message-content p {
  margin: 0 0 0.5rem 0;
  line-height: 1.5;
}

.message-timestamp {
  font-size: 0.7rem;
  opacity: 0.8;
  text-align: right;
}

.user-message .message-timestamp {
  color: rgba(255, 255, 255, 0.8);
}

.message-bubble:not(.user-message) .message-timestamp {
  color: #999;
}
</style>