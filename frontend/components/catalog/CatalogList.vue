<script setup lang="ts">
import { products } from '~/assets/data/products.data';
</script>
<template>
  <div class="catalog-list">
    <ProductsCard
      v-for="product in products"
      :id="product.id"
      :key="product.id"
      :title="product.title"
      :price="product.price"
      :sizes="product.sizes"
      :colors="product.colors"
      :image="product.image"
    />
  </div>
</template>
<style scoped lang="scss">
.catalog-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}
</style>
