export const useAuth = () => {
  const config = useRuntimeConfig();
  const userStore = useUsersStore();
  const router = useRouter();

  const login = async (email: string, password: string) => {
    const res = await $fetch(`${config.public.apiBase}/auth/login/`, {
      method: 'POST',
      body: { email, password },
    });
    userStore.setAuth(res);
    router.push('/');
  };

  const register = async (email: string, password: string) => {
    const res = await $fetch(`${config.public.apiBase}/auth/register/`, {
      method: 'POST',
      body: { email, password },
    });
    userStore.setAuth(res);
    router.push('/');
  };

  const socialLogin = (provider: 'vk' | 'yandex') => {
    window.location.href = `${config.public.apiBase}/auth/${provider}/login`;
  };

  return { login, register, socialLogin };
};
