<script setup lang="ts">
import BaseButton from "../base/button/BaseButton.vue";

const modalsStore = useModalsStore();
const { logout } = useAuth();

const isLoggingOut = ref(false);

const handleLogout = async () => {
  isLoggingOut.value = true;
  await logout();
  modalsStore.closeModal("logout");
  navigateTo("/");
};
</script>

<template>
  <div class="modal-logout__content">
    <div class="modal-logout__icon">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none">
        <path
          d="M17 16L21 12M21 12L17 8M21 12H7M13 16V17C13 18.6569 11.6569 20 10 20H6C4.34315 20 3 18.6569 3 17V7C3 5.34315 4.34315 4 6 4H10C11.6569 4 13 5.34315 13 7V8"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </div>

    <h3 class="modal-logout__title">Точно выйти?</h3>
    <p class="modal-logout__subtitle">Ваша корзина будет сохранена</p>

    <div class="modal-logout__actions">
      <BaseButton
        label="Остаться"
        :outline="true"
        @click="modalsStore.closeModal('logout')"
      />
      <BaseButton label="Да, выйти" @click="modalsStore.closeModal('logout')" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-logout {
  &__content {
    background: $white;
    padding: 40px;
    border-radius: calc($btn_radius * 1.5);
    max-width: 420px;
    width: 100%;
    // text-align: center;
    box-shadow: 0 20px 40px rgba($black, 0.2);
    // transform: translateY(20px);
    // animation: slideUp 0.4s $default_cubic forwards 0.1s;
    position: absolute;
    overflow: hidden;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  &__icon {
    width: 80px;
    height: 80px;
    margin: 0 auto 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba($accent, 0.1);
    border-radius: 50%;
    color: $accent-dark;
    padding: 16px;
    box-shadow: 0 4px 12px rgba($accent, 0.15);
  }

  &__title {
    text-align: center;
    color: $txt;
    margin-bottom: 12px;
    font-size: 24px;
    font-weight: 700;
    line-height: 1.3;
  }

  &__subtitle {
    text-align: center;
    color: rgba($txt, 0.7);
    margin-bottom: 28px;
    font-size: 16px;
    line-height: 1.5;
  }

  &__actions {
    display: flex;
    gap: 16px;
    justify-content: center;
  }

  &__btn {
    position: relative;
    padding: 14px 28px;
    border-radius: $btn_radius;
    font-weight: 600;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.4s $default_cubic;
    overflow: hidden;
    border: none;
    min-width: 140px;
    display: flex;
    align-items: center;
    justify-content: center;

    &:disabled {
      opacity: 0.8;
      cursor: not-allowed;
      transform: none !important;
    }
  }

  &__loader {
    display: flex;
    gap: 6px;
    align-items: center;
    justify-content: center;
  }

  .loader-dot {
    width: 8px;
    height: 8px;
    background-color: currentColor;
    border-radius: 50%;
    animation: bounce 1.4s infinite ease-in-out;

    &:nth-child(2) {
      animation-delay: 0.2s;
    }

    &:nth-child(3) {
      animation-delay: 0.4s;
    }
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    transform: translateY(20px);
  }
  to {
    transform: translateY(0);
  }
}

@keyframes bounce {
  0%,
  80%,
  100% {
    transform: scale(0.6);
    opacity: 0.5;
  }
  40% {
    transform: scale(1);
    opacity: 1;
  }
}
</style>
