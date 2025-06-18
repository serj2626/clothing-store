<script setup lang="ts">
const currentStep = ref(1);
</script>
<template>
  <div class="auth-page">
    <div class="container auth-page__container">
      <div class="auth-page__logo">
        <h1 class="auth-page__logo-text">ClothCrash</h1>
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
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  height: 100%;
  padding: 20px;
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
  .auth-page__container {
    padding: 30px;
  }
}

@media (max-width: $mobile) {
  .auth-page__container {
    padding: 20px;
  }
}
</style>
