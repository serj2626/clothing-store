<script setup lang="ts">
import { products } from "~/assets/data/products.data";

const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Избранное", url: "/favorite" },
];
</script>
<template>
  <div class="favorite-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <div class="favorite-page__content">
        <h2 class="favorite-page__content-title">Избранное</h2>
        <div class="favorite-page__content-list">
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
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.favorite-page {
  &__content {
    &-title {
      font-size: 20px;
      margin-block: 30px;
    }
    &-list {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 15px;
      margin-bottom: 100px;
    }
  }
}
</style>
