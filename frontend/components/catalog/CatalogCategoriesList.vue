<script setup lang="ts">
import type { ICatalogResponse } from '~/types';

defineProps<{
  categories: ICatalogResponse[];
}>();
</script>
<template>
  <ul class="catalog-categories__list">
    <li
      v-for="value in categories"
      :key="value.id"
      :class="[
        'catalog-categories__list-item',
      ]"
      :style="{ paddingLeft: value.indent }"
    >
      <span v-if="value.has_children">
        {{ value.name }}
      </span>
    </li>
  </ul>
</template>
<style scoped lang="scss"></style>
