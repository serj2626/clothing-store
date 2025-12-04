<script setup lang="ts">
import type { AvailableColors, AvailableSizes } from "~/types";
defineProps<{
  colors: AvailableColors[];
  sizes: AvailableSizes[];
}>();
</script>
<template>
  <div class="catalog-filters">
    <FilterSizes :sizes="sizes || []" />
    <FilterColors :colors="colors || []" />
    <FilterRange />
    <FilterOrdering />
  </div>
</template>
<style scoped lang="scss">
.catalog-filters {
  display: flex;
  align-items: center;
  gap: 25px;
}
</style>
