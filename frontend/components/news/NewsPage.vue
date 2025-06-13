<script setup lang="ts">
import { api } from "~/api";
import { newsPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { IProduct } from "~/types";
const { $api } = useNuxtApp();

const { data: productNewsCollection } = await useAsyncData(
  "news-page-products-last-list",
  () => $api<IProduct[]>(api.products.last)
);
</script>
<template>
  <div class="news-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="newsPageBreadcrumbs" />
      <div class="news-page__content">
        <h2 class="news-page__content-title">Новые коллекции</h2>
        <div class="news-page__content-list">
          <ProductCard
            v-for="product in productNewsCollection"
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
          />
        </div>
      </div>
      <BaseFormSubscribe />
    </div>
  </div>
</template>
<style scoped lang="scss">
.news-page {
  &__content {
    &-title {
      @include title_page;
    }
    &-list {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
      margin-bottom: 100px;
    }
  }
}
</style>
