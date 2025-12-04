<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { AvailableSizes } from "~/types";

defineProps<{
  sizes: AvailableSizes[];
}>();

const showSizes = ref<boolean>(true);

const toogleSizes = () => {
  showSizes.value = !showSizes.value;
};
</script>
<template>
  <BaseAccordion :is-open="showSizes" @update:is-open="toogleSizes">
    <template #summary>
      <div class="filter-sizes">
        <span class="filter-sizes__title">Цвет</span>
        <button style="flex-shrink: 0" class="filter-sizes__btn">
          <Icon
            style="color: #e0bea2"
            :name="HeroIcons.DOWN"
            class="filter-sizes__btn-icon"
          />
        </button>
      </div>
    </template>
    <template #content>
      <ul>
        <li v-for="size in sizes" :key="size.title">
          {{ size.title }}
        </li>
      </ul>
    </template>
  </BaseAccordion>
</template>
<style scoped lang="scss">
.filter-sizes {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}
.filter-sizes__title {
}
.filter-sizes__btn {
}
.filter-sizes__btn-icon {
  font-size: 18px;
}

:deep(.accordion) {
  width: fit-content;
}
</style>
