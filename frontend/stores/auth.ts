// stores/auth.store.ts
import { defineStore } from 'pinia'
import { useCookie } from '#app'

interface User {
  id: string
  name: string
  email: string
}

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const token = useCookie<string | null>('auth_token')
  const isAuthenticated = computed(() => !!token.value)

  // Инициализация при загрузке
  const initialize = () => {
    if (token.value && !user.value) {
      // Здесь можно добавить запрос для проверки токена
      // или декодировать JWT, если он содержит данные пользователя
      try {
        // Пример: если токен содержит данные пользователя
        // const payload = JSON.parse(atob(token.value.split('.')[1]))
        // user.value = payload.user
      } catch (e) {
        console.error('Failed to parse token', e)
        logout()
      }
    }
  }

  const login = async (credentials: { email: string; password: string }) => {
    try {
      // Здесь должна быть ваша реальная логика авторизации
      // Например, запрос к API:
      // const { data } = await useFetch('/api/auth/login', {
      //   method: 'POST',
      //   body: credentials
      // })
      
      // Заглушка для демонстрации:
      const response = {
        user: {
          id: '1',
          name: 'Тестовый Пользователь',
          email: credentials.email
        },
        token: 'fake-jwt-token'
      }

      user.value = response.user
      token.value = response.token
      
      return true
    } catch (error) {
      console.error('Login error:', error)
      return false
    }
  }

  const register = async (userData: { name: string; email: string; password: string }) => {
    try {
      // Здесь должна быть ваша реальная логика регистрации
      // const { data } = await useFetch('/api/auth/register', {
      //   method: 'POST',
      //   body: userData
      // })
      
      // Заглушка для демонстрации:
      const response = {
        user: {
          id: '1',
          name: userData.name,
          email: userData.email
        },
        token: 'fake-jwt-token'
      }

      user.value = response.user
      token.value = response.token
      
      return true
    } catch (error) {
      console.error('Registration error:', error)
      return false
    }
  }

  const logout = () => {
    user.value = null
    token.value = null
  }

  // Вызываем инициализацию при создании хранилища
  initialize()

  return {
    user,
    token,
    isAuthenticated,
    login,
    register,
    logout,
    initialize
  }
})