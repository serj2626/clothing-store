<script setup lang="ts">
interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface FeedbackForm {
  firstName: FormField<string>;
  lastName: FormField<string>;
  email: FormField<string>;
  phone: FormField<string>;
  city: FormField<string>;
  street: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  firstName: { value: "", error: "", required: true },
  lastName: { value: "", error: "", required: true },
  email: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  city: { value: "", error: "", required: true },
  street: { value: "", error: "", required: true },
});
</script>
<template>
  <div class="account-data">
    <form class="account-data__form">
      <div class="account-data__form-personal">
        <p class="account-data__form-personal-title">Персональные данные:</p>
        <div class="account-data__form-personal-list">
          <BaseInput
            v-model:input-value="formData.firstName.value"
            v-model:error="formData.firstName.error"
            type="text"
            placeholder="Имя"
          />
          <BaseInput
            v-model:input-value="formData.lastName.value"
            v-model:error="formData.lastName.error"
            type="text"
            placeholder="Фамилия"
          />
          <BaseInput
            v-model:input-value="formData.email.value"
            v-model:error="formData.email.error"
            type="email"
            placeholder="example@mail.ru"
          />
          <BaseInput
            v-model:input-value="formData.phone.value"
            v-model:error="formData.phone.error"
            type="tel"
            placeholder="8-888-888-88-88"
          />
        </div>
      </div>
      <div class="account-data__form-address">
        <p class="account-data__form-address-title">Адрес доставки:</p>
        <div class="account-data__form-address-list">
          <BaseInput
            v-model:input-value="formData.city.value"
            v-model:error="formData.city.error"
            type="text"
            placeholder="City"
          />
          <BaseInput
            v-model:input-value="formData.street.value"
            v-model:error="formData.street.error"
            type="text"
            placeholder="Street"
          />
        </div>
      </div>
      <BaseButton
        class="account-data__form-submit"
        label="ОБНОВИТЬ ИНФОРМАЦИЮ"
        size="lg"
        radius="0"
        color="#e0bea2"
      />
    </form>
  </div>
</template>
<style scoped lang="scss">
.account-data {
  &__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    &-submit {
      display: block;
      width: 100%;
      color: $white;
      padding-block: 16px;
    }
    &-personal {
      &-title {
        margin-bottom: 20px;
      }
      &-list {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
      }
    }
    &-address {
      &-title {
        margin-bottom: 20px;
      }
      &-list {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
      }
    }
    margin-bottom: 20px;
  }
}

// input {
//   padding-block: 16px;
//   padding-left: 19px;
//   box-sizing: border-box;
//   border: 0.5px solid $txt;

//   &::placeholder {
//     font-weight: 200;
//   }
// }
</style>
