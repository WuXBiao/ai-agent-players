import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RoleListView from '../views/RoleListView.vue'
import ChatView from '../views/ChatView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/roles',
      name: 'roles',
      component: RoleListView
    },
    {
      path: '/chat/:roleId',
      name: 'chat',
      component: ChatView,
      props: true
    }
  ]
})

export default router