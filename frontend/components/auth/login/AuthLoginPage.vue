<script setup lang="ts"></script>
<template>
  <div class="auth-page">
    <div class="container auth-page__container">
      <h1 class="auth-page__title">Вход в аккаунт</h1>
      <AuthFormLogin />
    </div>
  </div>
</template>

<style scoped lang="scss">
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
  &__container {
    width: 100%;
    max-width: 450px;
    background: $white;
    padding: 40px;
    border-radius: $btn_radius;
    box-shadow: 0 4px 20px rgba($black, 0.1);
  }
  &__title {
    font-size: 28px;
    color: $txt;
    text-align: center;
    margin-bottom: 30px;
  }
}
</style>
