<script lang="ts" setup>
interface IBaseButton {
  size?: "xs" | "sm" | "md" | "lg";
  icon: string;
  label: string;
  disabled?: boolean;
  radius?: string;
  color?: string;
}

const {
  color = "#d38f56",
  size = "md",
  radius = "10px",
  label,
} = defineProps<IBaseButton>();
</script>

<template>
  <button
    :class="[
      'base-button-with-icon',
      `base-button-with-icon__${size}`,
      { 'base-button-with-icon_disabled': disabled },
    ]"
  >
    <Icon class="base-button-with-icon__icon" :name="icon" size="18" />
    {{ label }}
  </button>
</template>
<style scoped lang="scss">
.base-button-with-icon {
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
}
</style>
