<script setup lang="ts"></script>
<template>
  <div class="base-form-subscribe">
    <div class="container">
      <h2 class="base-form-subscribe__title">Узнайте первым о новинках</h2>
      <form class="base-form-subscribe__form">
        <BaseInput radius="5px" type="email" placeholder="Введите ваш email" />
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
          <NuxtLink class="base-form-subscribe__form-text-link" to="/policy">условиями конфиденциальности.</NuxtLink>
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
    color: #252525;
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
      color: #252525;
      font-weight: 200;

      &-link {
        color: blue;
      }
    }
  }
}
</style>
