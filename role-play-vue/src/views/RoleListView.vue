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
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.header-section {
  text-align: center;
  margin-bottom: 3rem;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  color: #333;
}

.page-subtitle {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 2rem;
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
}

.roles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 2rem;
}
</style>