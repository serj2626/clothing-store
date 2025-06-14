<script setup lang="ts">
import { api } from "~/api";
const { $api } = useNuxtApp();

const modalsStore = useModalsStore();

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface ISubscribeResponse {
  message: string;
  status: string;
}

interface FeedbackForm {
  email: FormField<string>;
  phone: FormField<string>;
  password: FormField<string>;
  passwordConfirm: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  email: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  password: { value: "", error: "", required: true },
  passwordConfirm: { value: "", error: "", required: true },
});

async function submit() {
  try {
    const res = await $api<ISubscribeResponse>(api.users.register, {
      method: "POST",
      body: {
        email: formData.email.value,
        phone: formData.phone.value,
        password: formData.password.value,
        password2: formData.passwordConfirm.value,
      },
    });
    modalsStore.openModal("success");
    clearForm(formData);
  } catch (e) {
    console.log("error", e);
  }
}
</script>
<template>
  <form class="auth-form-register" @submit.prevent="submit">
    <div class="auth-form-register__form-group">
      <label for="register-email">Email</label>
      <BaseInput
        v-model:input-value="formData.email.value"
        radius="8px"
        type="email"
        placeholder="your@email.com"
      />
    </div>
    <div class="auth-form-register__form-group">
      <label for="register-name">Телефон</label>
      <BaseInput
        v-model:input-value="formData.phone.value"
        radius="8px"
        type="text"
        placeholder="Ваш номер телефона"
      />
    </div>
    <div class="auth-form-register__form-group">
      <label for="register-password">Пароль</label>
      <BaseInput
        v-model:input-value="formData.password.value"
        radius="8px"
        type="password"
        placeholder="••••••••"
      />
    </div>

    <div class="auth-form-register__form-group">
      <label for="register-confirm">Подтвердите пароль</label>

      <BaseInput
        v-model:input-value="formData.passwordConfirm.value"
        radius="8px"
        type="password"
        placeholder="••••••••"
      />
    </div>

    <BaseButton
      class="account-form-feedback__form-submit"
      label="Зарегистрироваться"
      size="lg"
      radius="8px"
      style="width: 100%"
    />
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
