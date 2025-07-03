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
      :category="product.category"
      :title="product.title"
      :price="product.price"
      :variants="product.variants"
      :avatar="product.avatar"
      :count_likes="product.count_likes"
      :count_reviews="product.count_reviews"
      :is_active="product.is_active"
      :currency="product.currency"
      :total_count="product.total_count"
      :brand="product.brand"
      :images="product?.images"
      :liked="product.liked"
    />
  </div>
</template>
<style lang="scss">
.catalog-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
  align-items: stretch;

  // &:has(.card:hover) {
  //   .card {
  //     opacity: 0.8;
  //     transform: none;
  //     transition: all 0.6s ease;
  //   }

  //   .card:hover {
  //     opacity: 1;
  //     transform: translateY(-10px);
  //   }
  // }

  @media (max-width: $tablet) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (max-width: $mobile) {
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>
