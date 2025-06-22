export const useAuthStore = defineStore("auth", () => {
  interface IUser {
    id: number;
    email: string;
    first_name: string;
    last_name: string;
  }

  const user = ref<IUser | null>(null);
  const accessToken = ref<string | null>(null);

  const setAccessToken = (token: string) => {
    accessToken.value = token;
  };

  const clearTokens = () => {
    accessToken.value = null;
  };

  return { accessToken, setAccessToken, clearTokens };
});
