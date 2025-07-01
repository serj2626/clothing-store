<script setup lang="ts">
import { api } from "~/api";
const loading = ref(false);

const { login } = useAuth();

const modalsStore = useModalsStore();
const { $api } = useNuxtApp();
interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface ISubscribeResponse {
  access: string;
  refresh?: string;
}

interface FeedbackForm {
  email: FormField<string>;
  password: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  email: { value: "", error: "", required: true },
  password: { value: "", error: "", required: true },
});

// async function submit() {
//   try {
//     await $api<ISubscribeResponse>(api.users.login, {
//       method: "POST",
//       body: {
//         email: formData.email.value,
//         password: formData.password.value,
//       },
//     });
//     modalsStore.openModal("success");
//     clearForm(formData);
//   } catch (e) {
//     console.log("error", e);
//   }
// }

async function submit() {
  console.log("formData", formData);
  try {
    await login({
      strategy: "local",
      body: {
        email: formData.email.value,
        password: formData.password.value,
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
  <form class="auth-form-login" @submit.prevent="submit">
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

    <div class="auth-form-login__footer">
      <span class="auth-form-login__footer-text">Ещё нет аккаунта?</span>
      <NuxtLink to="/auth/register" class="auth-form-login__footer-link">
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
    font-size: 12px;
    color: $accent !important;
    text-decoration: none;
    transition: $default_transition;

    &:hover {
      text-decoration: underline;
    }
  }
  &__footer {
    &-text {
      color: $txt;
    }
    &-link {
      color: $accent-dark;
      text-decoration: none;
      font-weight: 600;
      transition: $default_transition;

      &:hover {
        text-decoration: underline;
      }
    }
  }
}
</style>
