<template>
  <div class="role-card" @click="$emit('select', role)">
    <div class="role-header">
      <h3 class="role-name">{{ role.name }}</h3>
      <div class="role-id">#{{ role.id }}</div>
    </div>
    <div class="role-description">
      <p>{{ role.description }}</p>
    </div>
    <div class="role-personality">
      <span class="personality-tag">{{ role.personality }}</span>
    </div>
    <div class="role-actions">
      <button class="chat-button" @click.stop="$emit('chat', role.id)">
        开始对话
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RoleCard',
  props: {
    role: {
      type: Object,
      required: true
    }
  },
  emits: ['select', 'chat']
}
</script>

<style scoped>
.role-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  border-radius: 15px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.role-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.role-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.role-name {
  color: #333;
  font-size: 1.4rem;
  font-weight: 700;
  margin: 0;
}

.role-id {
  background-color: #667eea;
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
}

.role-description p {
  color: #666;
  font-size: 1rem;
  line-height: 1.5;
  margin: 0 0 1rem 0;
}

.role-personality {
  margin-bottom: 1.5rem;
}

.personality-tag {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
}

.role-actions {
  text-align: right;
}

.chat-button {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 25px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.chat-button:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}
</style>