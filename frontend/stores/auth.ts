// stores/auth.store.ts
import { defineStore } from "pinia";

interface IUser {
  id: string;
  name: string;
  email: string;
}

interface IAuthToken {
  access: string;
  refresh: string;
}
export const useAuthStore = defineStore("auth", () => {
  const user = ref<IUser | null>(null);
  const accessToken = useCookie<string | null>("access_token");
  const refreshToken = useCookie<string | null>("refresh_token");

  const isAuthenticated = computed(() => !!accessToken.value);

  const login = async (username: string, password: string) => {
    try {
      const { access, refresh } = await $fetch<IAuthToken>("/api/token/", {
        method: "POST",
        body: { username, password },
      });

      accessToken.value = access;
      refreshToken.value = refresh;

      // Получим данные пользователя (если есть такой endpoint)
      const userData = await $fetch<IUser>("/api/user/", {
        headers: {
          Authorization: `Bearer ${access}`,
        },
      });

      user.value = userData;
    } catch {
      throw new Error("Ошибка авторизации");
    }
  };

  const logout = () => {
    accessToken.value = null;
    refreshToken.value = null;
    user.value = null;
  };

  return {
    user,
    isAuthenticated,
    login,
    logout,
  };
});
