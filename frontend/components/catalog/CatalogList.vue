<script setup lang="ts">
import type { IProduct } from "~/types";

defineProps<{ products: IProduct[] }>();
</script>
<template>
  <div class="catalog-list">
    <ProductCard
      v-for="product in products"
      :id="product.id"
      :key="product.id"
      :sku="product.sku"
      :price="product.price"
      :category="product.category"
      :title="product.title"
      :variants="product.variants"
      :avatar="product.avatar"
      :count_likes="product.count_likes"
      :count_reviews="product.count_reviews"
      :is_active="product.is_active"
      :total_count="product.total_count"
      :brand="product.brand"
      :images="product?.avatar"
      :liked="product.liked"
    />
  </div>
</template>
<style lang="scss">
.catalog-list {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 15px;
  align-items: stretch;

  @include mediaTablet {
    grid-template-columns: repeat(2, 1fr);
  }

  @include mediaLaptop {
    grid-template-columns: repeat(3, 1fr);
  }

  @include mediaDesktop {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>
