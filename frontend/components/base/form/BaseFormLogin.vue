<script lang="ts" setup>
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const emit = defineEmits(["close"]);

function closeFormLogin() {
  const form = document.querySelector(".base-form-login");
  form?.classList.add("base-form-login_close");
  setTimeout(() => {
    emit("close");
  }, 100);
}

function handleKeydown(e: KeyboardEvent) {
  if (e.key === "Escape") {
    closeFormLogin();
  }
}

interface FormField {
  value: string | boolean;
  error: string;
  required: boolean;
}

interface IFormData {
  [key: string]: FormField;
}

function onVerify(token: string) {
  formData.recaptcha.value = token;
  console.log("Получен токен reCAPTCHA:", token);
}

const formData = reactive<IFormData>({
  email: {
    value: "",
    error: "",
    required: true,
  },
  password: {
    value: "",
    error: "",
    required: true,
  },
  remember: {
    value: false,
    error: "",
    required: false,
  },
  recaptcha: {
    value: "",
    error: "",
    required: true,
  },
});

const error = ref("");

const login = async () => {
  console.log("formData", formData);
  // clearFormAuth(formData)
  // try {
  //   const { data, error: loginError } = await useFetch<{ token: string }>(
  //     '/api/login',
  //     {
  //       method: 'POST',
  //       body: {
  //         email: formData?.email.value,
  //         password: formData?.password.value,
  //       },
  //     }
  //   );

  //   if (loginError.value) {
  //     error.value = loginError.value.message;
  //     alert(error.value);
  //     return;
  //   }

  //   const token = data.value?.token;
  //   if (!token) return;

  //   // Логика "Запомнить меня"
  //   if (formData.remember.value) {
  //     localStorage.setItem('auth_token', token); // сохраняем навсегда
  //   } else {
  //     sessionStorage.setItem('auth_token', token); // до закрытия вкладки
  //   }

  //   navigateTo('/');
  // } catch (e) {
  //   error.value = 'Ошибка входа';
  // }
};

onMounted(() => {
  const form = document.querySelector(".base-form-login");
  form?.classList.add("base-form-login_open");
  document.addEventListener("keydown", handleKeydown);
});
onBeforeUnmount(() => {
  document.removeEventListener("keydown", handleKeydown);
});
</script>
<template>
  <div class="base-form-login">
    <div class="base-form-login__wraper">
      <div class="base-form-login__wraper-top">
        <form @submit.prevent.stop class="base-form-login__wraper-top-form">
          <BaseInputWithIcon
            v-model:input-value="formData.email.value"
            :error="formData.email.error"
            type="email"
            placeholder="Email"
            :icon="HeroIcons.MAIL"
          />
          <BaseInputWithIcon
            v-model:input-value="formData.password.value"
            :error="formData.password.error"
            type="password"
            placeholder="Не менее 8 символов"
            :icon="HeroIcons.PASSWORD"
          />
          <BaseRecaptcha @verify="onVerify" />
          <BaseButton
            type="submit"
            class="base-form-login__wraper-top-form-btn"
            size="md"
            color="red"
            label="Войти"
            @click="login"
          />
          <BaseInputCheckbox
            v-model:agree-value="formData.remember.value"
            label="Запомнить меня"
          />
        </form>
      </div>
      <BaseButtonCLose
        top="10px"
        right="10px"
        :size="22"
        color="$bg_footer"
        @click="closeFormLogin"
      />
    </div>
  </div>
</template>
<style lang="scss" scoped>
.base-form-login {
  position: absolute;
  z-index: 101;
  top: 57px;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 10px;
  box-shadow: 0 0 10px 10px rgba(0, 0, 0, 0.158);
  min-width: 330px;
  background-color: $txt_white;

  &__wraper {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 50px 25px 25px;
    color: $txt;

    @include modal_arrow(50%, 4px);

    &-top {
      &-form {
        display: flex;
        flex-direction: column;
        gap: 12px;
        &-recaptcha {
          display: flex;
          justify-content: center; // центрируем по горизонтали
          margin-block: 10px; // отступ снизу

          // задаём фиксированный размер (пример)
          width: 100%;
          height: 78px; // стандартная высота reCAPTCHA

          // если внутри есть iframe — ограничиваем его размер
          iframe {
            width: 100% !important;
            height: 100% !important;
            border-radius: 8px; // если нужно скругление
            box-shadow: 0 0 6px rgba(0, 0, 0, 0.15);
          }
        }
        &-btn {
          width: 100%;
          font-weight: 600;
          line-height: 125%;
        }
      }
    }
  }
}
@keyframes show-login {
  from {
    scale: 0.5;
    opacity: 0.8;
  }
  to {
    scale: 1;
    opacity: 1;
  }
}

@keyframes close-login {
  0% {
    transform: translate(-50%, 0);
    box-shadow: 0 0 20px rgb(240, 241, 241);
    scale: 1;
  }

  100% {
    box-shadow: 20px 15px 151px 125px rgba(255, 255, 255, 0.294);
    scale: 0.1;
    transform: translate(-100%);
  }
}
</style>
