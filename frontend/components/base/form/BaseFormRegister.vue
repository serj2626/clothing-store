<script lang="ts" setup>
const modalsStore = useModalsStore();
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const close = ref(false);

function handleAnimationEnd(e: AnimationEvent) {
  if (close.value && e.animationName.includes("close")) {
    modalsStore.closeModal("register");
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

const formData = reactive<IFormData>({
  name: {
    value: "",
    error: "",
    required: true,
  },
  email: {
    value: "",
    error: "",
    required: true,
  },
  phone: {
    value: "",
    error: "",
    required: true,
  },
  password: {
    value: "",
    error: "",
    required: true,
  },
});

const error = ref("");

const goToPolicy = () => {
  modalsStore.closeModal("register");
  navigateTo("/policy");
};

// function closeModal() {
//   const form = document.querySelector("#base-form-register");
//   setTimeout(() => {
//     form?.classList.add("base-form-register_close");
//     modalsStore.closeModal("register");
//   }, 200);
// }

function submitRegisterForm() {
  console.log("formdata", formData);
}
</script>
<template>
  <div
    id="base-form-register"
    class="base-form-register"
    :class="{ 'base-form-register_close': close }"
    @animationend="handleAnimationEnd"
  >
    <div class="base-form-register__wraper">
      <div class="base-form-register__wraper-top">
        <h3 class="base-form-register__wraper-top-title">
          Начните работу с АльфаСМС
        </h3>
        <p class="base-form-register__wraper-top-text">
          Создайте бесплатный аккаунт. Без банковской карты.
        </p>
      </div>
      <form @submit.prevent.stop class="base-form-register__wraper-form">
        <div class="base-form-register__wraper-form-block">
          <label class="base-form-register__wraper-form-block-label" for="name"
            >Имя</label
          >
          <BaseInput
            v-model:input-value="formData.name.value"
            :error="formData.name.error"
            type="text"
            class="base-form-register__wraper-form-block-input"
            placeholder="Иван Иванов"
          />
        </div>
        <div class="base-form-register__wraper-form-block">
          <label class="base-form-register__wraper-form-block-label" for="email"
            >Почта</label
          >
          <BaseInput
            v-model:input-value="formData.email.value"
            :error="formData.email.error"
            type="email"
            class="base-form-register__wraper-form-block-input"
            placeholder="example@ex.com"
          />
        </div>
        <div class="base-form-register__wraper-form-block">
          <label class="base-form-register__wraper-form-block-label" for="phone"
            >Телефон</label
          >
          <BaseInput
            v-model:input-value="formData.phone.value"
            :error="formData.phone.error"
            type="text"
            class="base-form-register__wraper-form-block-input"
            placeholder="8-999-999-99-99"
          />
        </div>
        <div class="base-form-register__wraper-form-block">
          <label
            class="base-form-register__wraper-form-block-label"
            for="password"
            >Пароль</label
          >
          <BaseInput
            v-model:input-value="formData.password.value"
            :error="formData.password.error"
            type="password"
            class="base-form-register__wraper-form-block-input"
            placeholder="Не менее 8 символов"
          />
        </div>
        <BaseRecaptcha />
        <BaseButton
          class="base-form-register__wraper-form-btn"
          size="lg"
          color="red"
          label="Регистрация"
          @click="submitRegisterForm"
        />
      </form>
      <!-- <div class="base-form-register__wraper-bottom">
        <p class="base-form-register__wraper-bottom-or">
          <span class="base-form-register__wraper-bottom-or-text"
            >или войти с помощью</span
          >
        </p>
        <div class="base-form-register__wraper-bottom-actions">
          <BaseButtonWithIcon
            class="base-form-register__wraper-bottom-actions-btn"
            size="md"
            color="blue"
            label="ВКонтакте"
            icon="social:vk"
          />
          <BaseButtonWithIcon
            class="base-form-register__wraper-bottom-actions-btn"
            size="md"
            color="white"
            label="Яндекс"
            icon="social:yandex"
          />
        </div>
        <p class="base-form-register__wraper-bottom-info">
          Используя AlfaSMS, вы принимаете наши
          <NuxtLink class="base-form-register__wraper-bottom-info-link"
            >Условия предоставления услуг</NuxtLink
          >
          и соглашаетесь с
          <NuxtLink
            @click="goToPolicy"
            class="base-form-register__wraper-bottom-info-link"
            >Политикой конфиденциальности
          </NuxtLink>
        </p>
      </div> -->
      <BaseButtonCLose
        top="20px"
        right="20px"
        :size="26"
        color="$bg_footer"
        @click="close = true"
      />
    </div>
  </div>
</template>
<style lang="scss" scoped>
.base-form-register {
  margin: 75px auto;

  background-color: $txt_white;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  max-width: 600px;
  width: 100%;

  animation: show-register 0.4s ease-out forwards;

  &_close {
    animation: close-register 0.3s ease-in forwards;
  }

  &__wraper {
    position: relative;
    padding: 20px;
    display: flex;
    flex-direction: column;

    @include mediaMobile {
      padding: 40px;
    }

    @include mediaTablet {
      padding: 50px;
    }

    &-top {
      padding-top: 20px;
      margin-bottom: 16px;

      @include mediaMobile {
        padding-top: 0;
      }

      &-title {
        font-size: 18px;
        margin-bottom: 4px;
        font-weight: 700;
        text-align: center;

        @include mediaTablet {
          font-size: 20px;
          text-align: start;
        }

        @include mediaLaptop {
          font-size: 28px;
        }
      }

      &-text {
        font-size: 14px;
        line-height: 142%;
        color: #5c6a70;
        text-align: center;

        @include mediaTablet {
          text-align: start;
        }
      }
    }

    &-form {
      display: flex;
      flex-direction: column;
      gap: 16px;

      &-block {
        display: flex;
        flex-direction: column;
        gap: 6px;

        &-label {
          font-size: 15px;
          font-weight: 500;
          line-height: 142%;
          color: $txt;
        }

        &-input {
          display: flex;
          flex-direction: column;
          justify-content: center;
          font-size: 15px;
          border: 1px solid #ced4da;
          line-height: 1.5;
          color: #212529;

          &::placeholder {
            color: #ced4da;
            padding: 0;
          }
        }
      }

      &-btn {
        width: 100%;
        padding: 10px 16px;
      }
    }

    &-bottom {
      &-or {
        margin-block: 35px;
        position: relative;
        width: 100%;
        border-bottom: 1px solid #ddd;
        line-height: 0;
        color: #5c6a70;

        @include mediaMobile {
          margin-block: 25px;
        }

        &-text {
          position: absolute;
          top: 50%;
          left: 50%;
          font-size: 12px;
          transform: translate(-50%, -50%);
          background-color: $txt_white;
          padding: 0 5px;

          @include mediaMobile {
            font-size: 15px;
            padding: 0 10px;
          }
        }
      }

      &-actions {
        display: flex;
        flex-direction: column;
        align-items: center;

        gap: 10px;
        margin-bottom: 20px;

        @include mediaMobile {
          flex-direction: row;
          justify-content: space-between;
        }

        &-btn {
          width: 100%;
        }
      }

      &-info {
        color: #5c6a70;
        font-size: 14px;
        text-align: center;
        padding-inline: 20px;

        @include mediaMobile {
          padding-inline: 40px;
        }

        @include mediaTablet {
          padding-inline: 50px;
        }

        &-link {
          color: $teal;
          cursor: pointer;
        }
      }
    }
  }
}

@keyframes show-register {
  0% {
    opacity: 0.5;
    transform: translateY(-100%);
  }

  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes close-register {
  0% {
    opacity: 1;
    transform: translateY(0);
  }

  100% {
    opacity: 0.5;
    transform: translateY(-100%);
  }
}
</style>
