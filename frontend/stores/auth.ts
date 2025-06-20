import { defineStore } from "pinia";

interface User {
  id: number;
  username: string;
  email: string;
}

interface Tokens {
  access: string;
  refresh: string;
}

export const useAuthStore = defineStore("auth", () => {
  const user = ref<User | null>(null);
  const accessToken = ref<string | null>(null);
  const isAuthenticated = computed(() => !!accessToken.value);

  // Функция логина
  async function login(credentials: { username: string; password: string }) {
    try {
      const data = await $fetch<Tokens & { user: User }>("/auth/login/", {
        method: "POST",
        body: credentials,
      });

      // Для случая, если используем не cookies, а localStorage
      accessToken.value = data.access;
      user.value = data.user;

      return data;
    } catch (error) {
      logout();
      throw error;
    }
  }

  // Функция обновления токена
  async function refreshToken() {
    try {
      const data = await $fetch<Tokens>("/auth/refresh/", {
        method: "POST",
      });

      accessToken.value = data.access;
      return data;
    } catch (error) {
      logout();
      throw error;
    }
  }

  // Функция логаута
  async function logout() {
    try {
      await $fetch("/auth/logout/", { method: "POST" });
    } finally {
      accessToken.value = null;
      user.value = null;
    }
  }

  // Проверка аутентификации при старте
  async function init() {
    try {
      if (accessToken.value) {
        await fetchUser();
      }
    } catch {
      logout();
    }
  }

  // Получение данных пользователя
  async function fetchUser() {
    user.value = await $fetch<User>("/auth/user/");
  }

  return {
    user,
    accessToken,
    isAuthenticated,
    login,
    logout,
    refreshToken,
    fetchUser,
    init,
  };
});
