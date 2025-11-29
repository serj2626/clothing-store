<script lang="ts" setup>
interface IBaseButton {
  size?: "xs" | "sm" | "md" | "lg";
  color?: string;
  label: string;
  disabled?: boolean;
  radius?: string;
  outline?: boolean;
}

const {
  color = "#d38f56",
  size = "md",
  radius = "10px",
  label,
  outline = false,
} = defineProps<IBaseButton>();
</script>

<template>
  <button
    :disabled="disabled"
    :class="[
      'base-button',
      { 'base-button_outline': outline },
      `base-button__${size}`,
      { 'base-button_disabled': disabled },
    ]"
  >
    {{ label }}
  </button>
</template>
<style scoped lang="scss">
.base-button {
  background-color: v-bind(color);
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;
  color: white;

  user-select: none;
  border-radius: v-bind(radius);
  border: 1px solid transparent;
  transition: all 0.3 ease-in-out;
  width: fit-content;

  cursor: pointer;

  &_outline {
    background-color: transparent;
    border: 1px solid v-bind(color);
    color: v-bind(color);
    transition: all 0.3s ease-in-out;
    &:hover {
      background-color: v-bind(color);
      color: white;
    }
  }

  &:hover {
    opacity: 0.8;
  }

  &__xs {
    padding: 6px 9px;
  }

  &__sm {
    padding: 6px 12px;
  }

  &__md {
    padding: 8px 16px;
  }

  &__lg {
    padding: 16px 28px;
  }
  &_disabled {
    opacity: 0.5;
    pointer-events: none;
  }
}
</style>
