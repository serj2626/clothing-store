<script setup lang="ts">
import type { AvailableSizes } from "~/types";

defineProps<{
  sizes: AvailableSizes[];
}>();
</script>

<template>
  <FilterContent title="Размер">
    <ul class="filter-sizes">
      <li v-for="size in sizes" :key="size.title" class="filter-sizes__item">
        {{ size.title }}
      </li>
    </ul>
  </FilterContent>
</template>
<style scoped lang="scss">
.filter-sizes {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
  width: max-content;
  &__item {
    width: 100%;
    cursor: pointer;
    font-size: 15px;
    padding: 5px 25px;
    transition: all 0.3s ease-in-out;

    &:hover {
      background-color: $accent;
    }
  }
}
</style>
