<script setup lang="ts">
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
  <form class="auth-form-login" @submit.prevent="handleLogin">
    <div class="auth-form-login__group">
      <label for="email">Email</label>
      <BaseInput
        v-model:input-value="formData.email.value"
        radius="8px"
        type="email"
        placeholder="your@email.com"
      />
    </div>

    <div class="auth-form-login__group">
      <label for="password">Пароль</label>

      <BaseInput
        v-model:input-value="formData.password.value"
        radius="8px"
        type="password"
        placeholder="••••••••"
      />
      <NuxtLink
        to="/auth/forgot-password"
        class="auth-form-login__forgot-password"
      >
        Забыли пароль?
      </NuxtLink>
    </div>
    <BaseButton label="Войти" size="lg" radius="8px" style="width: 100%" />

    <div class="auth-footer">
      <span>Ещё нет аккаунта?</span>
      <NuxtLink to="/auth/register" class="auth-form-login__link">
        Зарегистрироваться
      </NuxtLink>
    </div>
  </form>
</template>
<style scoped lang="scss">
.auth-form-login {
  display: flex;
  flex-direction: column;
  gap: 20px;
  &__group {
    @include form-group;
    label {
      font-family: $ff_second;
      font-size: 14px;
      color: $txt;
      font-weight: 500;
    }
  }
  &__forgot-passwor {
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
  &__link {
    color: $accent-dark;
    text-decoration: none;
    font-weight: 600;
    transition: $default_transition;

    &:hover {
      text-decoration: underline;
    }
  }
}
</style>
