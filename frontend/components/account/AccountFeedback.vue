<script setup lang="ts"></script>

<template>
  <div class="account-form-feedback">
    <p class="account-form-feedback__title">Форма обратной связи</p>

    <form class="account-form-feedback__form" @submit.prevent="$emit('submit')">
      <div class="account-form-feedback__form-group">
        <label for="login-email">Имя</label>
        <BaseInput
          :animate="false"
          radius="8px"
          type="text"
          placeholder="Ваше имя "
        />
      </div>

      <div class="account-form-feedback__form-group">
        <label for="login-password">Телефон</label>
        <BaseInput
          :animate="false"
          radius="8px"
          type="text"
          placeholder="8-888-888-88-88"
        />
      </div>
      <div class="account-form-feedback__form-group">
        <textarea
          class="account-form-feedback__form-group-textarea"
          placeholder="Ваше сообщение"
        />
      </div>
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
    color: $txt;
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
        font-family: $ff_second;
        font-size: 14px;
        color: $txt;
        font-weight: 500;
      }
      &-textarea {
        resize: vertical;
        margin-top: 8px;
        width: 100%;
        max-height: 200px;
        height: 100px;
        border-radius: 8px;
        border: 1px solid $txt;
        padding-block: 16px;
        padding-left: 20px;
      }
    }
  }
}
</style>
