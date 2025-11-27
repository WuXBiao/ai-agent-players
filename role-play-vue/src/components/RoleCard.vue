<template>
  <div class="role-card">
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
      <button 
        class="chat-button" 
        @click="handleSelectRole"
        :disabled="isLoading"
      >
        {{ isLoading ? '设置中...' : '开始对话' }}
      </button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRoleStore } from '@/stores/roleStore'
import { useRouter } from 'vue-router'

export default {
  name: 'RoleCard',
  props: {
    role: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const roleStore = useRoleStore()
    const router = useRouter()
    const isLoading = ref(false)

    const handleSelectRole = async () => {
      try {
        isLoading.value = true
        // 设置角色
        await roleStore.setRole(props.role.name)
        // 设置成功后跳转到聊天页面
        router.push(`/chat/${props.role.id}`)
      } catch (error) {
        console.error('Failed to select role:', error)
      } finally {
        isLoading.value = false
      }
    }

    return {
      handleSelectRole,
      isLoading
    }
  }
}
</script>

<style scoped>
@keyframes borderGlow {
  0%, 100% { box-shadow: inset 0 0 10px rgba(0, 212, 255, 0.1), 0 0 10px rgba(0, 212, 255, 0.1); }
  50% { box-shadow: inset 0 0 20px rgba(0, 212, 255, 0.2), 0 0 20px rgba(0, 212, 255, 0.2); }
}

.role-card {
  background: rgba(15, 23, 42, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 0;
  padding: 1.2rem;
  box-shadow: 0 0 10px rgba(0, 212, 255, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
  border: 1px solid rgba(0, 212, 255, 0.2);
  overflow: hidden;
  position: relative;
}

.role-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #00d4ff, transparent);
  animation: scan 3s linear infinite;
}

@keyframes scan {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

.role-card:hover {
  border-color: #00d4ff;
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.3), inset 0 0 20px rgba(0, 212, 255, 0.05);
  transform: translateY(-3px);
}

.role-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.role-name {
  color: #00d4ff;
  font-size: 1.3rem;
  font-weight: 800;
  margin: 0;
  letter-spacing: 1px;
}

.role-id {
  background: transparent;
  color: #00d4ff;
  padding: 0.3rem 0.6rem;
  border-radius: 0;
  font-size: 0.75rem;
  font-weight: 700;
  min-width: 35px;
  text-align: center;
  border: 1px solid rgba(0, 212, 255, 0.4);
  letter-spacing: 1px;
}

.role-description p {
  color: rgba(102, 126, 234, 0.8);
  font-size: 0.85rem;
  line-height: 1.5;
  margin: 0 0 1rem 0;
  font-weight: 400;
}

.role-personality {
  margin-bottom: 1.2rem;
}

.personality-tag {
  background: transparent;
  color: #00d4ff;
  padding: 0.3rem 0.8rem;
  border-radius: 0;
  font-size: 0.75rem;
  font-weight: 600;
  border: 1px solid rgba(0, 212, 255, 0.3);
  letter-spacing: 0.5px;
}

.role-actions {
  text-align: center;
}

.chat-button {
  background: transparent;
  color: #00d4ff;
  border: 1px solid #00d4ff;
  padding: 0.6rem 1.2rem;
  border-radius: 0;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  letter-spacing: 1px;
  position: relative;
  overflow: hidden;
}

.chat-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(0, 212, 255, 0.1);
  transition: left 0.3s ease;
  z-index: -1;
}

.chat-button:hover:not(:disabled) {
  box-shadow: 0 0 15px rgba(0, 212, 255, 0.4), inset 0 0 15px rgba(0, 212, 255, 0.1);
}

.chat-button:hover:not(:disabled)::before {
  left: 100%;
}

.chat-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>