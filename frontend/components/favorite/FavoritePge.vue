<script setup lang="ts">
import { favoritePageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import { products } from "~/assets/data/products.data";
</script>
<template>
  <div class="favorite-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="favoritePageBreadcrumbs" />
      <div class="favorite-page__content">
        <h2 class="favorite-page__content-title">Избранное</h2>
        <div class="favorite-page__content-list">
          <ProductCard
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
