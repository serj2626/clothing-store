<script setup lang="ts"></script>
<template>
  <div class="auth-social">
    <p class="auth-social__title">Или войдите через</p>
    <div class="auth-social__buttons">
      <button class="auth-social__buttons-btn google">
        <Icon name="logos:google-icon" size="20" />
        Google
      </button>
      <button class="auth-social__buttons-btn vk">
        <Icon name="logos:vk" size="20" />
        VK
      </button>
    </div>
  </div>
</template>
<style scoped lang="scss">
.auth-social {
  margin-top: 30px;
  text-align: center;

  &__title {
    font-family: $ff_second;
    font-size: 14px;
    color: rgba($txt, 0.6);
    margin-bottom: 16px;
    position: relative;

    &::before,
    &::after {
      content: "";
      position: absolute;
      top: 50%;
      width: 30%;
      height: 1px;
      background-color: rgba(0, 0, 0, 0.1);
    }

    &::before {
      left: 0;
    }

    &::after {
      right: 0;
    }
  }
  &__buttons {
    display: flex;
    gap: 12px;
    justify-content: center;

    &-btn {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 12px 20px;
      border-radius: $btn_radius;
      font-family: $ff_second;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      border: 1px solid rgba(0, 0, 0, 0.1);
      background-color: $white;
      transition: background-color $default_transition,
        transform $default_transition;

      &:hover {
        transform: translateY(-2px);
      }

      &.google {
        color: #4285f4;
      }

      &.vk {
        color: #0077ff;
      }
    }
  }
}
</style>
