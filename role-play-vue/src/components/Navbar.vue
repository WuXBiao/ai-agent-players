<template>
  <nav class="navbar">
    <div class="nav-brand">
      <h2>AI角色扮演</h2>
    </div>
    <ul class="nav-menu">
      <li class="nav-item">
        <router-link to="/" class="nav-link" active-class="active">首页</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/roles" class="nav-link" active-class="active">角色列表</router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
.navbar {
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand h2 {
  color: #667eea;
  font-weight: 700;
}

.nav-menu {
  display: flex;
  list-style: none;
}

.nav-item {
  margin-left: 2rem;
}

.nav-link {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: color 0.3s ease;
  padding: 0.5rem 1rem;
  border-radius: 20px;
}

.nav-link:hover {
  color: #667eea;
}

.nav-link.active {
  background-color: #667eea;
  color: white;
}
</style>