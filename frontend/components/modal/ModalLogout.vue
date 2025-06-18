<script setup lang="ts">
const modalsStore = useModalsStore();
const { logout } = useAuth();

const isLoggingOut = ref(false);

const handleLogout = async () => {
  isLoggingOut.value = true;
  await logout();
  modalsStore.closeModal('logout');
  navigateTo('/');
};
</script>

<template>
  <div class="modal-logout" @click.self="modalsStore.closeModal('logout')">
    <div class="modal-logout__content">
      <div class="modal-logout__icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none">
          <path d="M17 16L21 12M21 12L17 8M21 12H7M13 16V17C13 18.6569 11.6569 20 10 20H6C4.34315 20 3 18.6569 3 17V7C3 5.34315 4.34315 4 6 4H10C11.6569 4 13 5.34315 13 7V8" 
                stroke="currentColor" 
                stroke-width="2" 
                stroke-linecap="round" 
                stroke-linejoin="round"/>
        </svg>
      </div>
      
      <h3 class="modal-logout__title">Точно выйти?</h3>
      <p class="modal-logout__subtitle">Ваша корзина будет сохранена</p>
      
      <div class="modal-logout__actions">
        <button 
          class="modal-logout__btn modal-logout__btn--cancel"
          @click="modalsStore.closeModal('logout')"
          :disabled="isLoggingOut"
        >
          <span>Остаться</span>
        </button>
        
        <button 
          class="modal-logout__btn modal-logout__btn--confirm"
          @click="handleLogout"
          :disabled="isLoggingOut"
        >
          <span v-if="!isLoggingOut">Да, выйти</span>
          <div v-else class="modal-logout__loader">
            <div class="loader-dot"></div>
            <div class="loader-dot"></div>
            <div class="loader-dot"></div>
          </div>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-logout {
//   position: fixed;
//   top: 0;
//   left: 0;
//   right: 0;
//   bottom: 0;
//   background: rgba($black, 0.6);
//   backdrop-filter: blur(8px);
//   display: flex;
//   justify-content: center;
//   align-items: center;
//   z-index: 9999;
//   padding: 20px;
//   opacity: 0;
//   animation: fadeIn 0.3s $default_cubic forwards;

  &__content {
    background: $white;
    padding: 40px;
    border-radius: calc($btn_radius * 1.5);
    max-width: 420px;
    width: 100%;
    text-align: center;
    box-shadow: 0 20px 40px rgba($black, 0.2);
    transform: translateY(20px);
    animation: slideUp 0.4s $default_cubic forwards 0.1s;
    position: relative;
    overflow: hidden;
    
    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, $accent 0%, $accent-dark 100%);
    }
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
    font-family: $ff_title;
    color: $txt;
    margin-bottom: 12px;
    font-size: 24px;
    font-weight: 700;
    line-height: 1.3;
  }

  &__subtitle {
    font-family: $ff_second;
    color: rgba($txt, 0.7);
    margin-bottom: 28px;
    font-size: 16px;
    line-height: 1.5;
  }

  &__actions {
    display: flex;
    gap: 16px;
    justify-content: center;

    @media (max-width: $mobile) {
      flex-direction: column-reverse;
      gap: 12px;
    }
  }

  &__btn {
    position: relative;
    padding: 14px 28px;
    border-radius: $btn_radius;
    font-family: $ff_second;
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

    &--cancel {
      background: transparent;
      color: $txt;
      border: 2px solid rgba($txt, 0.2);
      
      &:hover:not(:disabled) {
        border-color: $txt;
        box-shadow: 0 4px 12px rgba($txt, 0.1);
      }
    }

    &--confirm {
      background: linear-gradient(135deg, $accent 0%, $accent-dark 100%);
      color: $white;
      box-shadow: 0 4px 12px rgba($accent-dark, 0.3);
      
      &:hover:not(:disabled) {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba($accent-dark, 0.4);
      }
      
      &:active:not(:disabled) {
        transform: translateY(0);
      }
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
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from { transform: translateY(20px); }
  to { transform: translateY(0); }
}

@keyframes bounce {
  0%, 80%, 100% { 
    transform: scale(0.6);
    opacity: 0.5;
  }
  40% { 
    transform: scale(1);
    opacity: 1;
  }
}
</style>