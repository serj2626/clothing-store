<script setup lang="ts">
import { productDetailPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { ILink } from "~/components/base/BaseBreadCrumbs.vue";

const { id } = useRoute().params;
const productId = Array.isArray(id) ? id[0] : id;

const store = useProductDetailStore();
const { product, loading, reviews } = storeToRefs(store);

onMounted(() => {
  store.fetchProduct(productId);
});

onUnmounted(() => {
  store.clearDataByProductStore();
});

const currentPage = computed<ILink>(() => ({
  title: product.value?.title ?? "Товар",
  url: `/product/${product.value?.id}`,
}));
</script>

<template>
  <div class="product-detail-page">
    <div class="container">
      <BaseBreadCrumbs
        :breadcrumbs="productDetailPageBreadcrumbs"
        :current-page="currentPage"
      />
      <div v-if="loading">Загрузка...</div>
      <div v-else class="product-detail-page__content">
        <ProductDetailImages v-if="product" :product="product" />
        <ProductDetailInfo v-if="product" :product="product" />
      </div>
      <ProductDetailComments v-if="reviews" :reviews />
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
