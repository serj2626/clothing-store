<script setup lang="ts"></script>
<template>
  <div class="auth-login-page">
    <div class="container auth-login-page__container">
      <h1 class="auth-login-page__title">Вход в аккаунт</h1>
      <AuthFormLogin />
    </div>
  </div>
</template>

<style scoped lang="scss">
.auth-login-page {
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
