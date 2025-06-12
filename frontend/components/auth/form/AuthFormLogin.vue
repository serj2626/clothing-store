<script setup lang="ts">
defineProps<{
  isLoading: boolean;
  loginError: string;
}>();

const emit = defineEmits(["submit"]);


const loginData = reactive({
  email: "",
  password: "",
});
</script>
<template>
  <form class="auth-form-login" @submit.prevent="emit('submit')">
    <div class="auth-form-login__form-group">
      <label for="login-email">Email</label>
      <BaseInput type="email" placeholder="your@email.com" />
    </div>

    <div class="auth-form-login__form-group">
      <label for="login-password">Пароль</label>

      <BaseInput type="password" placeholder="••••••••" />
      <NuxtLink to="/forgot-password" class="auth-form-login__forgot-password">
        Забыли пароль?
      </NuxtLink>
    </div>

    <button
      type="submit"
      class="auth-form-login__auth-btn"
      :disabled="isLoading"
    >
      <span v-if="!isLoading">Войти</span>
      <span v-else class="auth-form-login__loader"></span>
    </button>

    <div v-if="loginError" class="auth-form-login__error-message">
      {{ loginError }}
    </div>
  </form>
</template>
<style lang="scss">
.auth-form-login {
  display: flex;
  flex-direction: column;
  gap: 20px;

  &__loader {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 2px solid $white;
    border-radius: 50%;
    border-top-color: transparent;
    animation: spin 0.8s linear infinite;
  }
  &__error-message {
    padding: 12px;
    background-color: rgba($error, 0.1);
    border-radius: $btn_radius;
    color: $error;
    font-family: $ff_second;
    font-size: 14px;
    text-align: center;
  }

  &__form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;

    label {
      font-family: $ff_second;
      font-size: 14px;
      color: $txt;
      font-weight: 500;
    }
  }

  &__forgot-password {
    align-self: flex-end;
    font-family: $ff_second;
    font-size: 12px;
    color: rgba($txt, 0.6);
    text-decoration: none;
    transition: color $default_transition;

    &:hover {
      color: $accent-dark;
    }
  }

  &__auth-btn {
    padding: 16px;
    background-color: $accent;
    color: $white;
    border: none;
    border-radius: $btn_radius;
    font-family: $ff_second;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color $default_transition,
      box-shadow $default_transition;

    &:hover {
      background-color: $accent-dark;
      box-shadow: $btn-accent-hover-shadow;
    }

    &:active {
      background-color: $btn-accent-active;
    }

    &:disabled {
      background-color: rgba($accent, 0.7);
      cursor: not-allowed;
    }
  }
}
</style>
