<script setup lang="ts">
import { api } from "~/api";
const { $api } = useNuxtApp();

const modalsStore = useModalsStore();
let captchaInstance = null;

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface ISubscribeResponse {
  msg: string;
  status: string;
}

interface FeedbackForm {
  email: FormField<string>;
  captcha: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  email: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
});

function clearForm() {
  formData.email.value = "";
  formData.email.error = "";
}

async function submit() {
  console.log("formData", formData);
  if (!validateForm()) return;

  try {
    const res: ISubscribeResponse = await $api(api.contacts.subscription, {
      method: "POST",
      body: {
        email: formData.email.value,
        "g-recaptcha-response": formData.captcha.value,
      },
    });

    console.log("Успешная отправка", res.msg, res.status);
    modalsStore.openModal("success");
    clearForm();
  } catch (e) {
    console.error("Ошибка отправки формы", e);
    formData.captcha.error = "Ошибка проверки капчи. Попробуйте еще раз.";
    if (captchaInstance?.reset) {
      captchaInstance.reset();
    }
  }
}

function validateForm() {
  let isValid = true;

  if (formData.email.required && !formData.email.value) {
    formData.email.error = "Поле обязательно для заполнения";
    isValid = false;
  } else if (!/^\S+@\S+\.\S+$/.test(formData.email.value)) {
    formData.email.error = "Введите корректный email";
    isValid = false;
  } else {
    formData.email.error = "";
  }

  if (formData.captcha.required && !formData.captcha.value) {
    formData.captcha.error =
      formData.captcha.error || "Необходимо пройти проверку";
    isValid = false;
  } else {
    formData.captcha.error = "";
  }

  return isValid;
}

function captchaHandler(val, eventName) {
  if (eventName === "success") {
    formData.captcha.value = val;
    formData.captcha.error = "";
  } else if (eventName === "error" || eventName === "expired") {
    formData.captcha.value = "";
    formData.captcha.error = "Необходимо пройти антиспам проверку";
  } else if (eventName === "inited") {
    captchaInstance = val;
  }
}
</script>
<template>
  <div class="base-form-subscribe">
    <div class="container">
      <h2 class="base-form-subscribe__title">Узнайте первым о новинках</h2>
      <form class="base-form-subscribe__form" @submit.prevent="submit">
        <BaseInput
          v-model:input-value="formData.email.value"
          :error="formData.email.error"
          radius="5px"
          type="email"
          placeholder="Введите ваш email"
        />
        <BaseCaptchaVisible
          :error="formData.captcha.error"
          @success="(val) => captchaHandler(val, 'success')"
          @error="(err) => captchaHandler(err, 'error')"
          @expired="() => captchaHandler(null, 'expired')"
          @inited="(val) => captchaHandler(val, 'inited')"
        />
        <BaseButton
          class="base-form-subscribe__form-btn"
          color="#e0bea2"
          radius="5px"
          size="lg"
          label="Подписаться"
        />
        <p class="base-form-subscribe__form-text">
          Нажимая на кнопку «Подписаться», я соглашаюсь на обработку моих
          персональных данных и ознакомлен(а) с
          <NuxtLink class="base-form-subscribe__form-text-link" to="/policy"
            >условиями конфиденциальности.</NuxtLink
          >
        </p>
      </form>
    </div>
  </div>
</template>
<style scoped lang="scss">
.base-form-subscribe {
  margin-block: 100px;

  &__title {
    text-align: center;
    color: var(--color-section-title);
    font-size: 36px;
    font-weight: 300;
    margin-bottom: 50px;
  }

  &__form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    max-width: 600px;
    width: 100%;
    margin: 0 auto;

    &-input {
      padding-block: 16px;
      border-radius: 5px;
      border: 1px solid #252525;
      color: #252525;
      opacity: 0.5;
      width: 100%;

      &::placeholder {
        text-align: center;
      }
    }

    &-btn {
      padding-block: 16px;
      border-radius: 5px;
      border: none;
      background-color: #e0bea2;
      color: #fff;
      cursor: pointer;
      width: 100%;
    }

    &-text {
      text-align: center;
      font-size: 16px;
      color: var(--color-text);
      font-weight: 200;

      &-link {
        color: rgb(91, 91, 247);
      }
    }
  }
}
</style>
