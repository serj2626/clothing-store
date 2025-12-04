<script setup lang="ts">
import type { AvailableColors } from "~/types";

defineProps<{
  colors: AvailableColors[];
}>();
</script>

<template>
  <FilterContent title="Цвет">
    <ul class="filter-colors">
      <li
        v-for="value in colors"
        :key="value.title"
        class="filter-colors__item"
      >
        {{ value.title }}
      </li>
    </ul>
  </FilterContent>
</template>
<style scoped lang="scss">
.filter-colors {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: max-content;

  &__item {
    cursor: pointer;
    padding: 5px 40px;
    font-size: 15px;
    transition: all 0.3s ease-in-out;

    &:hover {
      background-color: $accent;
    }
  }
}
</style>
