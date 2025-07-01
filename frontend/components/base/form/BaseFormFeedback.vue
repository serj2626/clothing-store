<script setup lang="ts">
import { api } from "~/api";
const { $api } = useNuxtApp();

const modalsStore = useModalsStore();
let captchaInstance = null;

interface ISubscribeResponse {
  msg: string;
  status: string;
}

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface FeedbackForm {
  message: FormField<string>;
  name: FormField<string>;
  phone: FormField<string>;
  captcha: FormField<string>;
  agree: FormField<boolean>;
}

const formData = reactive<FeedbackForm>({
  name: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  message: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
  agree: { value: false, error: "", required: true },
});

async function submit() {
  if (validateForm(formData)) return;
  try {
    const res = await $api<ISubscribeResponse>(api.contacts.feedback, {
      method: "POST",
      body: {
        name: formData.name.value,
        phone: formData.phone.value,
        message: formData.message.value,
        agree: true,
      },
    });
    console.log("asdasdsad", res.msg, res.status);
    modalsStore.openModal("success");
    clearForm(formData);
  } catch (e) {
    console.log("error", e);
  }
}
</script>

<template>
  <div class="account-form-feedback">
    <p class="account-form-feedback__title">Форма обратной связи</p>

    <form class="account-form-feedback__form" @submit.prevent="submit">
      <div class="account-form-feedback__form-group">
        <label for="login-email">Имя</label>
        <BaseInput
          v-model:input-value="formData.name.value"
          type="text"
          placeholder="Ваше имя "
        />
      </div>

      <div class="account-form-feedback__form-group">
        <label for="login-password">Телефон</label>
        <BaseInput
          v-model:input-value="formData.phone.value"
          :animate="false"
          type="text"
          placeholder="8-888-888-88-88"
        />
      </div>
      <BaseInputTextArea
        v-model:input-value="formData.message.value"
        placeholder="Ваше сообщение"
      />
      <BaseInputCheckbox
        v-model:agree-value="formData.agree.value"
        label="Я даю согласие на обработку персональных данных"
      />

      <BaseButton
        class="account-form-feedback__form-submit"
        label="Отправить"
        size="lg"
        radius="8px"
        color="#e0bea2"
      />
    </form>
  </div>
</template>

<style scoped lang="scss">
.account-form-feedback {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 600px;
  width: 100%;
  margin-inline: auto;
  &__title {
    font-size: 24px;
    color: var(--color-section-title);
    font-weight: 500;
  }

  &__form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    &-submit {
      width: 100%;
      margin-top: 15px;
    }
    &-group {
      display: flex;
      flex-direction: column;
      gap: 8px;

      label {
        font-size: 14px;
        color: var(--color-text);
        font-weight: 500;
      }
    }
  }
}
</style>
