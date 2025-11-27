<template>
  <nav class="navbar">
    <div class="nav-brand">
      <h2>AI虚拟角色</h2>
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
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 20px rgba(102, 126, 234, 0.2);
  padding: 1.2rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand h2 {
  color: white;
  font-weight: 900;
  font-size: 1.5rem;
  margin: 0;
  letter-spacing: -0.5px;
}

.nav-menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-item {
  margin-left: 2.5rem;
}

.nav-link {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 600;
  transition: all 0.3s ease;
  padding: 0.6rem 1.2rem;
  border-radius: 25px;
  font-size: 0.95rem;
  letter-spacing: 0.3px;
}

.nav-link:hover {
  color: white;
  background-color: rgba(255, 255, 255, 0.15);
}

.nav-link.active {
  background-color: rgba(255, 255, 255, 0.25);
  color: white;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}
</style>