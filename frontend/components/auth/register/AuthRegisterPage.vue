<script setup lang="ts">
const currentStep = ref(1);
</script>
<template>
  <div class="auth-register-page">
    <div class="container auth-register-page__container">
      <div class="auth-register-page__logo">
        <h1 class="auth-register-page__logo-text">ClothCrash</h1>
      </div>

      <AuthRegisterProgress
        :current-step="currentStep"
        @update:current-step="currentStep = $event"
      />

      <AuthFormRegister
        :current-step="currentStep"
        @update:current-step="currentStep = $event"
      />
    </div>
  </div>
</template>

<style lang="scss">
.auth-register-page {
  margin-block: 100px 50px;
  &__container {
    width: 100%;
    max-width: 500px;
    background-color: $white;
    border-radius: $btn_radius;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    padding: 40px;
  }
  &__logo {
    text-align: center;
    margin-bottom: 30px;
  }
  &__logo-text {
    font-family: $ff_title;
    font-size: 28px;
    color: $accent-dark;
    font-weight: 700;
  }
}

@media (max-width: $tablet) {
  .auth-register-page__container {
    padding: 30px;
  }
}

@media (max-width: $mobile) {
  .auth-register-page__container {
    padding: 20px;
  }
}
</style>
