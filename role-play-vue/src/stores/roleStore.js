import { defineStore } from 'pinia'
import { roleService, chatService } from '@/services/roleService'

export const useRoleStore = defineStore('role', {
  state: () => ({
    roles: [],
    currentRole: null,
    loading: false,
    error: null
  }),

  getters: {
    getRoleById: (state) => (id) => {
      return state.roles.find(role => role.id === parseInt(id))
    }
  },

  actions: {
    async fetchRoles() {
      this.loading = true
      this.error = null
      try {
        const roles = await roleService.getRoles()
        this.roles = roles
      } catch (error) {
        this.error = error.message
        console.error('Failed to fetch roles:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchRoleById(id) {
      this.loading = true
      this.error = null
      try {
        const role = await roleService.getRoleById(id)
        this.currentRole = role
        return role
      } catch (error) {
        this.error = error.message
        console.error('Failed to fetch role:', error)
      } finally {
        this.loading = false
      }
    }
  }
})

export const useChatStore = defineStore('chat', {
  state: () => ({
    messages: [],
    loading: false,
    error: null
  }),

  actions: {
    async sendMessage(roleId, content) {
      this.loading = true
      this.error = null
      try {
        const message = await chatService.sendMessage(roleId, content)
        this.messages.push(message)
        return message
      } catch (error) {
        this.error = error.message
        console.error('Failed to send message:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchChatHistory(roleId) {
      this.loading = true
      this.error = null
      try {
        const messages = await chatService.getChatHistory(roleId)
        this.messages = messages
      } catch (error) {
        this.error = error.message
        console.error('Failed to fetch chat history:', error)
      } finally {
        this.loading = false
      }
    },

    clearMessages() {
      this.messages = []
    }
  }
})