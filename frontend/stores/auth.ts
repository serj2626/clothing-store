import { defineStore } from 'pinia';
import { useAuth } from '@nuxt-alt/auth';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as any, // Можно типизировать под вашу модель пользователя
    isAuthenticated: false,
  }),
  actions: {
    // Инициализация состояния из useAuth()
    async init() {
      const { user, status } = useAuth();
      this.user = user.value;
      this.isAuthenticated = status.value === 'authenticated';
    },

    // Логин с обработкой ошибок
    async login(credentials: { username: string; password: string }) {
      const { login } = useAuth();
      try {
        await login('jwt', credentials);
        await this.init(); // Обновляем состояние
        return true;
      } catch (error) {
        console.error('Login error:', error);
        return false;
      }
    },

    // Выход
    async logout() {
      const { logout } = useAuth();
      await logout('jwt');
      this.user = null;
      this.isAuthenticated = false;
    },

    // Проверка роли (пример)
    hasRole(role: string) {
      return this.user?.roles?.includes(role);
    },
  },
});