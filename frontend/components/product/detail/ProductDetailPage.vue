<script setup lang="ts">
import { api } from "~/api";
import { productDetailPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { ILink } from "~/components/base/BaseBreadCrumbs.vue";
import type { IProduct } from "~/types";

const { id } = useRoute().params;
const productId = Array.isArray(id) ? id[0] : id;

const { $api } = useNuxtApp();

const {
  data: product,
  pending,
  error,
} = await useAsyncData<IProduct>("product-detail-page", () =>
  $api(api.products.detail(productId))
);
const currentPage: ILink = {
  title: product?.value?.title ? product?.value?.title : "Товар",
  url: `/product/${product?.value?.id}`,
};
</script>

<template>
  <div class="product-detail-page">
    <div class="container">
      <BaseBreadCrumbs
        :breadcrumbs="productDetailPageBreadcrumbs"
        :current-page="currentPage"
      />
      <div v-if="pending">Загрузка...</div>
      <div v-else-if="error">Ошибка: {{ error.message }}</div>
      <div v-else class="product-detail-page__content">
        <ProductDetailImages v-if="product" :product="product" />
        <ProductDetailInfo />
      </div>
      <ProductDetailComments />
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
