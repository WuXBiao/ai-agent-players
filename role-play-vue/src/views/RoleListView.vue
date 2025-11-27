<template>
  <div class="roles-container">
    <Navbar />
    
    <div class="header-section">
      <h1 class="page-title">角色列表</h1>
      <p class="page-subtitle">选择一个角色开始对话</p>
    </div>
    
    <div class="loading-spinner" v-if="roleStore.loading">
      加载中...
    </div>
    
    <div class="error-message" v-else-if="roleStore.error">
      {{ roleStore.error }}
    </div>
    
    <div class="roles-grid" v-else>
      <RoleCard
        v-for="role in roleStore.roles"
        :key="role.id"
        :role="role"
      />
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue'
import { useRoleStore } from '@/stores/roleStore'
import Navbar from '@/components/Navbar.vue'
import RoleCard from '@/components/RoleCard.vue'

export default {
  name: 'RoleListView',
  components: {
    Navbar,
    RoleCard
  },
  setup() {
    const roleStore = useRoleStore()
    
    onMounted(() => {
      roleStore.fetchRoles()
    })
    
    return {
      roleStore
    }
  }
}
</script>

<style scoped>
.roles-container {
  min-height: 100vh;
  background: #0a0e27;
  padding: 1.5rem 1rem;
  position: relative;
}

.roles-container::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(0deg, transparent 24%, rgba(102, 126, 234, 0.05) 25%, rgba(102, 126, 234, 0.05) 26%, transparent 27%, transparent 74%, rgba(102, 126, 234, 0.05) 75%, rgba(102, 126, 234, 0.05) 76%, transparent 77%, transparent),
    linear-gradient(90deg, transparent 24%, rgba(102, 126, 234, 0.05) 25%, rgba(102, 126, 234, 0.05) 26%, transparent 27%, transparent 74%, rgba(102, 126, 234, 0.05) 75%, rgba(102, 126, 234, 0.05) 76%, transparent 77%, transparent);
  background-size: 50px 50px;
  pointer-events: none;
  z-index: 1;
}

.header-section {
  text-align: center;
  margin-bottom: 2rem;
  color: white;
  position: relative;
  z-index: 10;
}

.page-title {
  font-size: 2rem;
  font-weight: 900;
  margin-bottom: 0.5rem;
  letter-spacing: 2px;
  background: linear-gradient(135deg, #00d4ff 0%, #667eea 50%, #ff00ff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page-subtitle {
  font-size: 0.9rem;
  color: rgba(102, 126, 234, 0.8);
  margin-bottom: 1rem;
  font-weight: 400;
  letter-spacing: 1px;
}

.loading-spinner {
  text-align: center;
  font-size: 1rem;
  padding: 2rem;
  color: #00d4ff;
  position: relative;
  z-index: 10;
}

.error-message {
  text-align: center;
  font-size: 1rem;
  padding: 1.5rem;
  color: #ff6b6b;
  background-color: rgba(15, 23, 42, 0.8);
  border-radius: 0;
  border: 1px solid rgba(255, 107, 107, 0.3);
  max-width: 600px;
  margin: 0 auto;
  position: relative;
  z-index: 10;
}

.roles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 10;
}
</style>