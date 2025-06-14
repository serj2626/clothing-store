<script setup lang="ts">
import { api } from "~/api";
import { productDetailPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { IProduct } from "~/types";

const { id } = useRoute().params;
const productId = Array.isArray(id) ? id[0] : id;

const { $api } = useNuxtApp();

const { data: product, pending } = await useAsyncData<IProduct>(
  "product-detail-page",
  () => $api(api.products.detail(productId))
);
</script>

<template>
  <div class="product-detail-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="productDetailPageBreadcrumbs" />
      <div class="product-detail-page__content">
        <ProductDetailImages v-if="product" :product="product" />
        <ProductDetailInfo />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.product-detail-page {
  &__content {
    margin-block: 100px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
  }
}
</style>
