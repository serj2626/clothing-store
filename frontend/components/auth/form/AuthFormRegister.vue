<script setup lang="ts">
defineProps<{
  isLoading: boolean;
  registerError: string;
}>();

const emit = defineEmits(["submit"]);

const registerData = reactive({
  name: "",
  email: "",
  password: "",
  confirmPassword: "",
});
</script>
<template>
  <form class="auth-form-register" @submit.prevent="emit('submit')">
    <div class="auth-form-register__form-group">
      <label for="register-name">Имя</label>
      <BaseInput
        v-model="registerData.name"
        radius="8px"
        type="text"
        placeholder="Ваше имя"
      />
    </div>

    <div class="auth-form-register__form-group">
      <label for="register-email">Email</label>
      <BaseInput
        v-model="registerData.email"
        radius="8px"
        type="email"
        placeholder="your@email.com"
      />
    </div>

    <div class="auth-form-register__form-group">
      <label for="register-password">Пароль</label>
      <BaseInput
        v-model="registerData.password"
        radius="8px"
        type="password"
        placeholder="••••••••"
      />
    </div>

    <div class="auth-form-register__form-group">
      <label for="register-confirm">Подтвердите пароль</label>

      <BaseInput
        v-model="registerData.confirmPassword"
        radius="8px"
        type="password"
        placeholder="••••••••"
      />
    </div>

    <button
      type="submit"
      class="auth-form-register__auth-btn"
      :disabled="isLoading"
    >
      <span v-if="!isLoading">Зарегистрироваться</span>
      <span v-else class="auth-form-register__loader"></span>
    </button>

    <div v-if="registerError" class="auth-form-register__error-message">
      {{ registerError }}
    </div>
  </form>
</template>
<style scoped lang="scss">
.auth-form-register {
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
