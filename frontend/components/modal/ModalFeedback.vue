<script lang="ts" setup>
import { api } from "~/api";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const { $api } = useNuxtApp();
const modalsStore = useModalsStore();

const close = ref(false);
const errorRef = ref("");

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface FeedbackForm {
  name: FormField<string>;
  email: FormField<string>;
  comment: FormField<string>;
  image: FormField<File | null>;
  recaptcha: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  name: { value: "", error: "", required: true },
  email: { value: "", error: "", required: true },
  comment: { value: "", error: "", required: true },
  image: { value: null, error: "", required: false },
  recaptcha: { value: "", error: "", required: true },
});

function handleAnimationEnd(e: AnimationEvent) {
  if (close.value && e.animationName.includes("close")) {
    modalsStore.closeModal("feedback");
  }
}

function onVerify(token: string) {
  formData.recaptcha.value = token;
}

const submitForm = () => {
  if (validateForm(formData)) return;
  console.log("formData", formData);

  const payload = new FormData();
  payload.append("name", formData.name.value);
  payload.append("email", formData.email.value);
  payload.append("message", formData.comment.value);
  if (formData.image.value) {
    payload.append("image", formData.image.value);
  }
  payload.append("recaptcha", formData.recaptcha.value);

  $api(api.contacts.feedback, {
    method: "POST",
    body: payload,
  })
    .then((response) => {
      console.log("Успешный ответ:", response);
      modalsStore.closeModal("feedback");
      modalsStore.openModal("success", {
        title: "Спасибо за ваш отзыв",
      });
    })
    .catch((error) => {
      errorRef.value = "Ошибка при отправке формы. Попробуйте позже.";
      console.error("Ошибка:", error);
    });
};
</script>
<template>
  <div
    id="modal-feedback"
    class="modal-feedback"
    :class="{ 'modal-feedback_close': close }"
    @animationend="handleAnimationEnd"
  >
    <div class="modal-feedback__wraper">
      <div class="modal-feedback__wraper-top">
        <p class="modal-feedback__wraper-top-title">Ждем ваши вопросы</p>
      </div>
      <form class="modal-feedback__wraper-form" @submit.prevent.stop>
        <div class="modal-feedback__wraper-form-name">
          <BaseInput
            class="modal-feedback__wraper-form-input"
            placeholder="Имя"
            v-model:input-value="formData.name.value"
            v-model:error="formData.name.error"
          />
        </div>
        <div class="modal-feedback__wraper-form-email">
          <BaseInput
            class="modal-feedback__wraper-form-input"
            placeholder="Почта"
            v-model:input-value="formData.email.value"
            v-model:error="formData.email.error"
          />
        </div>
        <div class="modal-feedback__wraper-form-textarea">
          <BaseInputTextArea
            placeholder="Введите ваш вопрос"
            v-model:input-value="formData.comment.value"
            v-model:error="formData.comment.error"
          />
        </div>
        <div class="modal-feedback__wraper-bottom">
          <div class="modal-feedback__wraper-bottom-file">
            <BaseInputFile
              class="modal-feedback__wraper-bottom-input"
              v-model:input-file="formData.image.value"
              v-model:error="formData.image.error"
            />
          </div>
          <BaseRecaptcha @verify="onVerify" />
          <button
            title="Отправить"
            class="modal-feedback__wraper-bottom-send"
            @click="submitForm"
          >
            <Icon
              class="modal-feedback__wraper-bottom-send-icon"
              size="36"
              :name="HeroIcons.SEND"
            />
          </button>
        </div>
      </form>

      <BaseButtonCLose
        top="10px"
        right="10px"
        :size="26"
        color="$bg_footer"
        @click="close = true"
      />
    </div>
  </div>
</template>
<style lang="scss" scoped>
%border-bottom {
  border-bottom: 1px solid #ffffff75;
}

.modal-feedback {
  position: fixed;
  bottom: 0;
  right: 0;
  z-index: 130;
  border-radius: 6px 6px 0 0;
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.24);
  background: linear-gradient(to right top, #15a7c8, #7a98e2);
  max-width: 500px;
  width: 100%;

  box-shadow: 0 0 30px rgba(253, 253, 253, 0.416);
  overflow: auto;
  animation: open-chat 0.4s ease-out forwards;

  display: flex;
  flex-direction: column;
  justify-content: space-between;

  &_close {
    animation: close-chat 0.3s ease-in forwards;
  }

  &__wraper {
    position: relative;
    color: $txt_white;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;

    &-top {
      padding-block: 20px;

      @extend %border-bottom;

      &-title {
        padding-inline: 15px;

        @include mediaTablet {
          padding-inline: 24px;
        }

        @include mediaLaptop {
          padding-inline: 34px;
        }
      }
    }

    &-form {
      padding: 10px 15px;
      display: flex;
      flex-direction: column;
      gap: 25px;

      @include mediaTablet {
        padding: 20px 24px;
      }

      @include mediaLaptop {
        padding: 20px 34px;
      }

      &:deep(.base-input) {
        width: 100%;
        color: $txt_white;
        justify-content: center;

        &:focus {
          outline: 1px solid transparent;
        }
      }

      &:deep(.base-input__placeholder) {
        width: 100%;
        color: $txt_white;
      }

      &:deep(.base-input__input) {
        &:focus {
          outline: none;
          border: none;
        }
      }

      &-name {
        @extend %border-bottom;
      }

      &-email {
        @extend %border-bottom;
      }

      &-file {
        // @extend %border-bottom;
      }

      &-textarea {
        // @extend %border-bottom;
      }
    }

    &-bottom {
      position: relative;
      padding-block: 10px 30px;
      display: flex;
      flex-direction: column;
      gap: 10px;

      &-recaptcha {
        display: flex;
        justify-content: start; // центрируем по горизонтали
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

      &-send {
        position: relative;
        margin-top: 10px;
        margin-inline: auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: $teal;
        border-radius: 50%;
        width: 90px;
        height: 90px;
        box-shadow: 5px 5px 20px #fff;
        transition: all $default_ease;

        & * {
          rotate: 90deg;
        }

        @include mediaLaptop {
          width: 100px;
          height: 100px;
        }

        &:active {
          scale: 0.8;
        }

        &::before {
          content: "";
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          background-color: $txt_white;
          border-radius: 50%;
          transform: scale(0);
          transition: transform $default_ease;
        }

        &:hover {
          color: $teal;
        }

        &:hover::before {
          transform: scale(1);
        }
      }
    }

    &-close {
      @include btn_close_form;
      color: $txt_white;
    }
  }
}

@keyframes open-chat {
  from {
    transform: translateX(100%);
    opacity: 0;
  }

  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes close-chat {
  from {
    transform: translateX(0);
    opacity: 1;
  }

  to {
    transform: translateX(100%);
    opacity: 0;
  }
}
</style>
