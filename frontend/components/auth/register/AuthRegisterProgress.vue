<script setup lang="ts">
defineProps<{
  currentStep: number;
}>();
const emit = defineEmits(["update:currentStep"]);
</script>
<template>
  <div class="auth-register-progress">
    <div
      class="auth-register-progress__step"
      :class="{
        active: currentStep === 1 || currentStep === 2,
        completed: currentStep > 1,
      }"
      @click="emit('update:currentStep', 1)"
    >
      <span class="auth-register-progress__step-number">1</span>
      <span class="auth-register-progress__step-label">Контактные данные</span>
    </div>
    <div class="auth-register-progress__step-line"></div>
    <div
      class="auth-register-progress__step"
      :class="{ active: currentStep === 2, completed: currentStep > 2 }"
      @click="emit('update:currentStep', 2)"
    >
      <span class="auth-register-progress__step-number">2</span>
      <span class="auth-register-progress__step-label">Личные данные</span>
    </div>
  </div>
</template>
<style scoped lang="scss">
.auth-register-progress {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 30px;
  position: relative;

  &__step {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
    z-index: 1;

    .active &-number {
      background-color: $accent;
      color: $white;
    }
    .active &-label {
      color: $accent;
    }
    .completed &-line {
      background-color: $accent;
    }

    &-number {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background-color: #e0e0e0;
      color: $txt;
      display: flex;
      justify-content: center;
      align-items: center;
      font-weight: 500;
      transition: $default_transition;
    }
    &-label {
      margin-top: 8px;
      font-size: 14px;
      color: $txt;
      transition: $default_transition;
    }
    &-line {
      position: absolute;
      top: 18px;
      left: 25%;
      right: 25%;
      height: 2px;
      background-color: #e0e0e0;
      z-index: 0;
    }
  }
}
</style>
