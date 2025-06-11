<script lang="ts" setup>
import { HeroIcons } from '~/assets/icons/types/hero-icons';
const emit = defineEmits(['close']);

const isVisible = ref(true);

// Закрытие с анимацией
const closeModal = () => {
  isVisible.value = false;
  setTimeout(() => emit('close'), 300);
};
</script>

<template>
  <div class="search-modal">
    <!-- Оверлей -->
    <div class="search-modal__overlay" @click="closeModal" />

    <!-- Контейнер модалки -->
    <div
      class="search-modal__container"
      :class="{ 'search-modal__container--hidden': !isVisible }"
    >
      <button class="search-modal__close" @click="closeModal">
        <Icon :name="HeroIcons.CLOSE" size="26" class="search-modal__close-icon" />
      </button>

      <div class="search-modal__content">
        <h2 class="search-modal__title">Поиск</h2>

        <div class="search-modal__input-wrapper">
          <BaseInputWithIcon
            type="search"
            placeholder="Введите запрос..."
            :icon="HeroIcons.SEARCH"
            class="search-modal__input"
            autofocus
          />
        </div>

        <div class="search-modal__hints">
          <span class="hint">Попробуйте: </span>
          <button class="hint-tag">Клиенты</button>
          <button class="hint-tag">Платежи</button>
          <button class="hint-tag">Отчеты</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from {
    transform: translate(-50%, -40%);
    opacity: 0;
  }
  to {
    transform: translate(-50%, -50%);
    opacity: 1;
  }
}

@keyframes slideDown {
  from {
    transform: translate(-50%, -50%);
    opacity: 1;
  }
  to {
    transform: translate(-50%, -40%);
    opacity: 0;
  }
}

.search-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 9999;

  &__overlay {
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
    animation: fadeIn 0.3s ease-out;
  }

  &__container {
    position: absolute;
    top: 50%;
    left: 50%;
    width: min(90%, 755px);
    background: white;
    border-radius: 16px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    overflow: hidden;
    animation: slideUp 0.4s cubic-bezier(0.22, 1, 0.36, 1);
    transform: translate(-50%, -50%);
    transition: all 0.3s ease;

    &--hidden {
      animation: slideDown 0.3s ease forwards;
    }
  }

  &__close {
    position: absolute;
    top: 20px;
    right: 20px;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: transparent;
    transition: all 0.2s ease;
    z-index: 10;

    &:hover {
      background: rgba(0, 0, 0, 0.05);
      transform: rotate(90deg);
    }

    &-icon {
      color: #4b5563;
      transition: transform 0.2s ease;
    }
  }

  &__content {
    padding: 40px;
  }

  &__title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 24px;
    text-align: center;
  }

  &__input-wrapper {
    position: relative;
    margin-bottom: 32px;

    &:deep(.base-input-icon__input) {
      padding: 16px 20px;
      font-size: 1rem;
      border: 2px solid #e5e7eb;
      border-radius: 12px;
      transition: all 0.3s ease;

      &:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
      }
    }

    &:deep(.base-input-icon__icon) {
      right: 20px;
      color: #9ca3af;
    }
  }

  &__hints {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;

    .hint {
      color: #6b7280;
      font-size: 0.875rem;
    }

    .hint-tag {
      padding: 6px 12px;
      background: #f3f4f6;
      border-radius: 8px;
      color: #4b5563;
      font-size: 0.875rem;
      transition: all 0.2s ease;

      &:hover {
        background: #e5e7eb;
        transform: translateY(-1px);
      }
    }
  }
}
</style>
