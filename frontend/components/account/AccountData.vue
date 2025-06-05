<script setup lang="ts"></script>
<template>
  <div class="account-data">
    <form class="account-data__form">
      <div class="account-data__form-personal">
        <p class="account-data__form-personal-title">Персональные данные:</p>
        <div class="account-data__form-personal-list">
          <input
            type="text"
            placeholder="Имя"
            class="account-data__form-personal-list-name"
          />
          <input
            type="text"
            placeholder="Фамилия"
            class="account-data__form-personal-list-surname"
          />
          <input
            type="text"
            placeholder="example@mail.ru"
            class="account-data__form-personal-list-mail"
          />
          <input
            type="text"
            placeholder="8-999-999-99-99"
            class="account-data__form-personal-list-phone"
          />
        </div>
      </div>
      <div class="account-data__form-address">
        <p class="account-data__form-address-title">Адрес доставки:</p>
        <div class="account-data__form-address-list">
          <input
            type="text"
            placeholder="City"
            class="account-data__form-address-list-city"
          />
          <input
            type="text"
            placeholder="Street"
            class="account-data__form-address-list-street"
          />
        </div>
      </div>
      <button class="account-data__form-submit">ОБНОВИТЬ ИНФОРМАЦИЮ</button>
    </form>
  </div>
</template>
<style scoped lang="scss">
.account-data {
  &__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    &-submit{
        background-color: $accent;
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

input {
  padding-block: 16px;
  padding-left: 19px;
  box-sizing: border-box;
  border: 0.5px solid $txt;

  &::placeholder {
    font-weight: 200;
  }
}
</style>
