import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

export const useUsersStore = defineStore("users", () => {
  const token = useStorage("token", "");
  const user = ref(null);

  const isLoggedIn = computed(() => !!token.value);

  interface ITokenResponse {
    token: string;
    user: any;
  }

  function setAuth(data: ITokenResponse) {
    token.value = data.token;
    user.value = data.user;
  }

  function logout() {
    token.value = "";
    user.value = null;
  }

  return { token, user, isLoggedIn, setAuth, logout };
});
