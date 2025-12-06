<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";

defineProps<{ title: string }>();

const showContent = ref(false);
const wrapperRef = ref<HTMLElement | null>(null);

// Переключение
const toggle = () => {
  showContent.value = !showContent.value;
};

// Клик вне компонента
const handleClickOutside = (event: MouseEvent) => {
  const target = event.target as Node;

  // если клик вне контейнера — закрываем
  if (wrapperRef.value && !wrapperRef.value.contains(target)) {
    showContent.value = false;
  }
};

onMounted(() => {
  // ВАЖНО: ставим capture = true
  // тогда событие ловится ДО stopPropagation
  window.addEventListener("click", handleClickOutside, true);
});

onBeforeUnmount(() => {
  // обязательно убираем с тем же capture
  window.removeEventListener("click", handleClickOutside, true);
});
</script>

<template>
  <div ref="wrapperRef" class="filter-content">
    <div class="filter-content__header">
      <span class="filter-content__header-title">
        {{ title || "Без названия" }}
      </span>

      <button class="filter-content__header-btn" @click="toggle">
        <Icon
          style="color: #e0bea2"
          :name="HeroIcons.UP"
          class="filter-content__header-btn-icon"
          :class="{ 'filter-content__header-btn-icon--active': !showContent }"
        />
      </button>
    </div>

    <Transition name="fade">
      <div v-show="showContent" class="filter-content__list">
        <slot />
      </div>
    </Transition>
  </div>
</template>

<style scoped lang="scss">
.filter-content {
  position: relative;

  &__header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;

    &-title {
      font-weight: 600;
    }

    &-btn {
      background: transparent;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;

      &-icon {
        font-size: 18px;
        transition: 0.3s ease;
        &--active {
          transform: rotate(180deg);
        }
      }
    }
  }

  &__list {
    position: absolute;
    top: 50px;
    left: 0;
    background: $white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    z-index: 100;
    max-height: 260px;
    overflow-y: auto;
    border-radius: 8px;
  }
}

/* Анимация */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
