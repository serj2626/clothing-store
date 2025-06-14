<script lang="ts" setup>
import { HeroIcons } from "~/assets/icons/types/hero-icons";
const {
  size = 20,
  top = "0",
  right = "0",
  color= 'black'
} = defineProps<{
  size?: number;
  top?: string;
  right?: string;
  color?: string
}>();
</script>
<template>
  <button class="base-button-close">
    <Icon
      :size="size"
      class="base-button-close__icon"
      :name="HeroIcons.CLOSE"
    />
  </button>
</template>

<style scoped lang="scss">
.base-button-close {
  position: absolute;
  top: v-bind(top);
  right: v-bind(right);
  cursor: pointer;
  transition: all 0.3s ease-in;
  color: v-bind(color);

  &:hover {
    scale: 1.1;
  }
}
</style>