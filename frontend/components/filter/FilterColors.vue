<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { AvailableColors } from "~/types";

defineProps<{
  colors: AvailableColors[];
}>();

const showColors = ref<boolean>(true);

const toogleColors = () => {
  showColors.value = !showColors.value;
};
</script>
<template>
  <BaseAccordion :is-open="showColors" @update:is-open="toogleColors">
    <template #summary>
      <div class="filter-colors">
        <span class="filter-colors__title">Цвет</span>
        <button style="flex-shrink: 0" class="filter-colors__btn">
          <Icon
            style="color: #e0bea2"
            :name="HeroIcons.DOWN"
            class="filter-colors__btn-icon"
          />
        </button>
      </div>
    </template>
    <template #content>
      <ul>
        <li v-for="color in colors" :key="color.slug">
          {{ color.title }}
        </li>
      </ul>
    </template>
  </BaseAccordion>
</template>
<style scoped lang="scss">
.filter-colors {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}
.filter-colors__title {
}
.filter-colors__btn {
}
.filter-colors__btn-icon {
  font-size: 18px;
}

:deep(.accordion) {
  width: fit-content;
}
</style>
