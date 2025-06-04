<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";

defineProps<{
  placeholder: string;
  options: string[];
}>();

const isOpen = ref(false);
const root = ref<HTMLElement | null>(null);

const toggleDropdown = () => {
  isOpen.value = !isOpen.value;
};

const handleClickOutside = (event: MouseEvent) => {
  console.log("event.target", event.target);
  if (root.value && !root.value.contains(event.target as Node)) {
    isOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener("click", handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener("click", handleClickOutside);
});
</script>

<template>
  <div class="base-input-select" ref="root">
    <button
      class="base-input-select__value"
      :class="{ 'base-input-select__value_open': isOpen }"
      @click="toggleDropdown"
    >
      <span class="base-input-select__value-text">{{ placeholder }}</span>
      <Icon
        class="base-input-select__value-icon"
        :class="{ 'base-input-select__value-icon-close': isOpen }"
        :name="HeroIcons.DOWN"
        size="20"
      />
    </button>
    <ul v-if="isOpen" class="base-input-select__list">
      <li
        v-for="item in options"
        :key="item"
        class="base-input-select__list-item"
        @click="isOpen = false"
      >
        <span class="base-input-select__list-item-text">
          {{ item }}
        </span>
      </li>
    </ul>
  </div>
</template>

<style scoped lang="scss">
.base-input-select {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;

  &__value {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 15px;
    border: 1px solid #888d8e44;
    border-radius: $btn_radius;
    cursor: pointer;
    background-color: white;
    margin-top: 20px;
    transform: all 0.3s ease-in-out;

    &_open {
      border-color: $teal;
    }

    &-text {
      font-size: 14px;
    }
    &-icon {
      transition: rotate 0.3s ease-in-out;
      &-close {
        rotate: 180deg;
      }
    }
  }

  &__list {
    position: absolute;
    left: 0;
    right: 0;
    top: 100%;
    margin-top: 5px;
    z-index: 100;
    background-color: white;
    border: 1px solid $bg_footer;
    border-radius: $btn_radius;
    display: flex;
    flex-direction: column;
    gap: 7px;
    max-height: 300px;
    overflow-y: auto;
  }

  &__list-item {
    cursor: pointer;
    padding: 5px 10px;
    border-radius: 5px;
    color: $txt;

    &-text {
      padding: 15px;
    }

    &:hover {
      background-color: $teal;
      color: $txt_white;
    }
  }
}
</style>
