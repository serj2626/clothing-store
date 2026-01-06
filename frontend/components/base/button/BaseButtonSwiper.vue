<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";

defineProps<{
  type: "prev" | "next";
}>();

const emit = defineEmits<{
  (e: "goPrev"): void;
  (e: "goNext"): void;
}>();
</script>

<template>
  <button
    class="base-button-swiper"
    :aria-label="type === 'prev' ? 'Предыдущий слайд' : 'Следующий слайд'"
    @click="type === 'prev' ? emit('goPrev') : emit('goNext')"
  >
    <Icon
      :name="
        type === 'prev'
          ? HeroIcons.ARROW_LEFT_SOLID
          : HeroIcons.ARROW_RIGHT_SOLID
      "
      class="base-button-swiper__icon"
    />
  </button>
</template>
<style scoped lang="scss">
.base-button-swiper {
  cursor: pointer;
  padding: 8px 12px;
  background-color: $accent-dark;
  color: $white;
  border-radius: $btn_small_radius;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: $accent;
  }

  &__icon {
    width: 22px;
    height: 22px;
  }
}
</style>
