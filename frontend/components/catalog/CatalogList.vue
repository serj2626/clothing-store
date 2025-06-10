<script setup lang="ts">
import type { IproductsResponse } from "~/types";
defineProps<{ products: IproductsResponse[] }>();
</script>
<template>
  <div class="catalog-list">
    <ProductCard
      v-for="product in products"
      :id="product.id"
      :key="product.id"
      :title="product.title"
      :price="product.price"
      :variants="product.variants"
      :avatar="product.avatar"
      :count_likes="product.count_likes"
      :count_reviews="product.count_reviews"
      :is_active="product.is_active"
    />
  </div>

  <!-- {{ products.slice(0,1) }} -->
</template>
<style scoped lang="scss">
.catalog-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}
</style>
