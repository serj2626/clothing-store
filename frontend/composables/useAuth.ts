export const useAuth = () => {
  const config = useRuntimeConfig();
  const accessToken = ref<string | null>(null);
  const isAuthenticated = ref(false);

  interface ITokenResponse {
    access: string;
    refresh: string;
  }

  // Функция для входа
  const login = async (credentials: { email: string; password: string }) => {
    try {
      const { data, error } = await useFetch<ITokenResponse>(
        "/api/v1/users/token/",
        {
          method: "POST",
          body: credentials,
          credentials: "include",
        }
      );

      if (error.value) throw error.value;

      accessToken.value = data.value?.access ?? null;
      isAuthenticated.value = true;

      return data.value;
    } catch (error) {
      console.error("Ошибка входа:", error);
      throw error;
    }
  };

  // Функция для обновления токена
  const refreshToken = async () => {
    try {
      const { data, error } = await useFetch<ITokenResponse>(
        "/api/v1/users/token/refresh/",
        {
          method: "POST",
          credentials: "include",
        }
      );

      if (error.value) throw error.value;

      accessToken.value = data.value?.access ?? null;
      return data.value;
    } catch (error) {
      await logout();
      throw error;
    }
  };

  // Функция выхода
  const logout = async () => {
    try {
      await useFetch("/api/v1/users/logout/", {
        method: "POST",
        credentials: "include",
      });
    } finally {
      accessToken.value = null;
      isAuthenticated.value = false;
      await navigateTo("/login");
    }
  };

  // Проверка аутентификации
  const checkAuth = async () => {
    if (!accessToken.value) {
      try {
        await refreshToken();
        isAuthenticated.value = true;
      } catch {
        isAuthenticated.value = false;
      }
    }
    return isAuthenticated.value;
  };

  return {
    accessToken,
    isAuthenticated,
    login,
    logout,
    refreshToken,
    checkAuth,
  };
};
