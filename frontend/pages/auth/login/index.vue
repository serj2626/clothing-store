<script setup lang="ts">
const email = ref("");
const password = ref("");
const error = ref("");
const loading = ref(false);

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface ISubscribeResponse {
  access: string;
  refresh: string;
}

interface FeedbackForm {
  email: FormField<string>;
  password: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  email: { value: "", error: "", required: true },
  password: { value: "", error: "", required: true },
});

const handleLogin = async () => {
  try {
    loading.value = true;
    error.value = "";

    // Здесь будет вызов API Django для авторизации
    // const { data, error: apiError } = await useFetch('/api/auth/login/', {
    //   method: 'POST',
    //   body: {
    //     email: email.value,
    //     password: password.value
    //   }
    // })

    // Временная имитация успешного входа
    setTimeout(() => {
      loading.value = false;
      navigateTo("/account");
    }, 1000);
  } catch (err) {
    error.value = "Неверный email или пароль";
    loading.value = false;
  }
};
</script>
<template>
  <div class="auth-page">
    <div class="auth-container">
      <h1 class="auth-title">Вход в аккаунт</h1>

      <form class="auth-form" @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">Email</label>
          <BaseInput
            v-model:input-value="formData.email.value"
            radius="8px"
            type="email"
            placeholder="your@email.com"
          />
        </div>

        <div class="form-group">
          <label for="password">Пароль</label>

          <BaseInput
            v-model:input-value="formData.password.value"
            radius="8px"
            type="password"
            placeholder="••••••••"
          />
          <NuxtLink to="/auth/forgot-password" class="forgot-password">
            Забыли пароль?
          </NuxtLink>
        </div>

        <div v-if="error" class="error-message">
          {{ error }}
        </div>

        <BaseButton label="Войти" size="lg" radius="8px" style="width: 100%" />
      </form>

      <div class="auth-footer">
        <span>Ещё нет аккаунта?</span>
        <NuxtLink to="/auth/register" class="auth-link">
          Зарегистрироваться
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: $white;
  padding: 20px;
}

.auth-container {
  width: 100%;
  max-width: 450px;
  background: $white;
  padding: 40px;
  border-radius: $btn_radius;
  box-shadow: 0 4px 20px rgba($black, 0.1);
}

.auth-title {
  font-family: $ff_title;
  font-size: 28px;
  color: $txt;
  text-align: center;
  margin-bottom: 30px;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;

  label {
    font-family: $ff_second;
    font-size: 14px;
    color: $txt;
    font-weight: 500;
  }

  input {
    padding: 12px 16px;
    border: 1px solid rgba($txt, 0.2);
    border-radius: $btn_radius;
    font-family: $ff_main;
    font-size: 16px;
    transition: $default_transition;

    &:focus {
      outline: none;
      border-color: $accent;
      box-shadow: 0 0 0 2px rgba($accent, 0.2);
    }
  }
}

.forgot-password {
  align-self: flex-end;
  font-family: $ff_second;
  font-size: 12px;
  color: $accent-dark;
  text-decoration: none;
  transition: $default_transition;

  &:hover {
    text-decoration: underline;
  }
}

.auth-button {
  padding: 14px;
  background-color: $accent;
  color: $white;
  border: none;
  border-radius: $btn_radius;
  font-family: $ff_title;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: $default_transition;

  &:hover {
    background-color: $accent-dark;
    box-shadow: $btn-accent-hover-shadow;
  }

  &:active {
    background-color: $btn-accent-active;
  }

  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
}

.auth-footer {
  margin-top: 20px;
  text-align: center;
  font-family: $ff_second;
  font-size: 14px;
  color: $txt;

  span {
    margin-right: 5px;
  }
}

.auth-link {
  color: $accent-dark;
  text-decoration: none;
  font-weight: 600;
  transition: $default_transition;

  &:hover {
    text-decoration: underline;
  }
}

.error-message {
  color: $error;
  font-family: $ff_second;
  font-size: 14px;
  text-align: center;
  margin-bottom: 10px;
}

@media (max-width: $tablet) {
  .auth-container {
    padding: 30px 20px;
  }

  .auth-title {
    font-size: 24px;
  }
}
</style>
