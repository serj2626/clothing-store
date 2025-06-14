<script setup lang="ts">
const authStore = useAuthStore();
const router = useRouter();

const isLoginForm = ref(true);
const isLoading = ref(false);
const loginError = ref("");
const registerError = ref("");

const loginData = reactive({
  email: "",
  password: "",
});

const toggleForm = (showLogin: boolean) => {
  isLoginForm.value = showLogin;
  loginError.value = "";
  registerError.value = "";
};

const validateRegister = () => {
  if (registerData.password !== registerData.confirmPassword) {
    registerError.value = "Пароли не совпадают";
    return false;
  }
  if (registerData.password.length < 6) {
    registerError.value = "Пароль должен содержать минимум 6 символов";
    return false;
  }
  return true;
};

// const handleLogin = async () => {
//   try {
//     isLoading.value = true;
//     loginError.value = "";
//     const success = await authStore.login(loginData);

//     if (success) {
//       await router.push("/account");
//     } else {
//       loginError.value = "Неверный email или пароль";
//     }
//   } catch (error) {
//     loginError.value = "Произошла ошибка при входе";
//     console.error("Login error:", error);
//   } finally {
//     isLoading.value = false;
//   }
// };

const handleRegister = async () => {
  if (!validateRegister()) return;

  try {
    isLoading.value = true;
    registerError.value = "";
    const success = await authStore.register({
      name: registerData.name,
      email: registerData.email,
      password: registerData.password,
    });

    if (success) {
      await router.push("/account");
    } else {
      registerError.value = "Ошибка при регистрации";
    }
  } catch (error) {
    registerError.value = "Произошла ошибка при регистрации";
    console.error("Registration error:", error);
  } finally {
    isLoading.value = false;
  }
};
</script>
<template>
  <div class="auth-page">
    <div class="auth-page__container">
      <div class="auth-page__auth-logo">
        <h4 class="auth-page__auth-logo-title">ClothCrash</h4>
      </div>

      <AuthTabs :is-login-form @toggle-form="toggleForm" />

      <AuthFormLogin v-if="isLoginForm" />

      <AuthFormRegister v-else />

      <AuthSocial />
    </div>
  </div>
</template>
<style scoped lang="scss">
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;

  &__container {
    width: 100%;
    max-width: 480px;
    background-color: $white;
    border-radius: $btn_radius;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    padding: 40px;
    animation: fadeIn $default_transition;
  }
  &__auth-logo {
    text-align: center;
    margin-bottom: 30px;

    &-title {
      font-family: $ff_title;
      font-size: 32px;
      color: $accent-dark;
      margin: 0;
    }
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: $tablet) {
  .auth-container {
    padding: 30px 20px;
  }

  .social-buttons {
    flex-direction: column;
  }
}
</style>
