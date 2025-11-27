import apiClient from './api'

export const roleService = {
  // 获取角色列表
  async getRoles() {
    try {
      const response = await apiClient.get('/roles')
      return response.roles
    } catch (error) {
      throw new Error(`Failed to fetch roles: ${error.message}`)
    }
  },

  // 获取角色详情
  async getRoleById(id) {
    try {
      const response = await apiClient.get(`/roles/${id}`)
      return response.role
    } catch (error) {
      throw new Error(`Failed to fetch role: ${error.message}`)
    }
  }
}

export const chatService = {
  // 发送消息
  async sendMessage(roleId, content) {
    try {
      const response = await apiClient.post('/messages', {
        role_id: roleId,
        content: content
      })
      return response.message
    } catch (error) {
      throw new Error(`Failed to send message: ${error.message}`)
    }
  },

  // 获取对话历史
  async getChatHistory(roleId) {
    try {
      const response = await apiClient.get(`/messages/${roleId}`)
      return response.messages
    } catch (error) {
      throw new Error(`Failed to fetch chat history: ${error.message}`)
    }
  }
}