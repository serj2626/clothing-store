<script setup lang="ts">
defineProps<{
  isLoginForm: boolean;
}>();

const emit = defineEmits(["toggleForm"]);
</script>
<template>
  <div class="auth-tabs">
    <button
      class="auth-tabs__btn"
      :class="{ 'auth-tabs__btn_active': isLoginForm }"
      @click="emit('toggleForm', true)"
    >
      Вход
    </button>
    <button
      class="auth-tabs__btn"
      :class="{ 'auth-tabs__btn_active': !isLoginForm }"
      @click="emit('toggleForm', false)"
    >
      Регистрация
    </button>
  </div>
</template>
<style scoped lang="scss">
.auth-tabs {
  display: flex;
  margin-bottom: 30px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);

  &__btn {
    flex: 1;
    padding: 12px;
    font-family: $ff_second;
    font-size: 16px;
    font-weight: 500;
    background: none;
    border: none;
    cursor: pointer;
    position: relative;
    color: rgba($txt, 0.6);
    transition: color $default_transition;

    &_active {
      color: $txt;
      font-weight: 600;

      &::after {
        content: "";
        position: absolute;
        bottom: -1px;
        left: 0;
        width: 100%;
        height: 2px;
        background-color: $accent;
        border-radius: 2px 2px 0 0;
      }
    }
  }
}
</style>
