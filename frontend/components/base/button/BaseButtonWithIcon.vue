<script lang="ts" setup>
interface IButton {
  size: "xs" | "sm" | "md" | "lg";
  color?: "red" | "green" | "gray" | "blue" | "white";
  view?: "outline" | "fill";
  label: string;
  icon?: string;
  disabled?: boolean;
}

defineProps<IButton>();
</script>

<template>
  <div
    :class="[
      'base-button-with-icon',
      `base-button-with-icon__${color}`,
      { 'base-button-with-icon_disabled': disabled },
    ]"
  >
    <span
      class="base-button-with-icon__title"
      :class="`base-button-with-icon__title_${size}`"
      >{{ label }}</span
    >
    <Icon v-if="icon" size="30" :name="icon" />
  </div>
</template>
<style scoped lang="scss">
.base-button-with-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;
  padding-inline: 10px;

  border-radius: $btn_radius;
  border: 1px solid transparent;
  // transition: all $fast_ease;
  width: fit-content;

  cursor: pointer;

  &:hover {
    opacity: 0.8;
  }
  &:active {
    scale: 0.96;
  }

  &__red {
    background-color: $error;
    color: $white;
    box-shadow: 0 0 10px rgb(255, 252, 252);
  }
  &__green {
    background-color: green;
    color: $white;
  }
  &__gray {
    background-color: rgba(255, 255, 255, 0.12);
    color: $white;
  }
  &__blue {
    background-color: blue;
    color: $white;
  }
  &__white {
    background-color: white;
    color: #5c6a70;
    border: 1px solid #5c6a704f;
    box-shadow: 0 5px 12px rgba(69, 80, 84, 0.317);
  }

  &__title {
    &_xs {
      padding-block: 6px;
    }

    &_sm {
      padding-block: 6px;
    }

    &_md {
      padding-block: 8px;
    }

    &_lg {
      padding-block: 16px;
    }
  }
}
</style>
