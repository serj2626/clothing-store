<script setup lang="ts">
import { productDetailPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { ILink } from "~/components/base/BaseBreadCrumbs.vue";

const { id } = useRoute().params;
const productId = Array.isArray(id) ? id[0] : id;
// const isLoading = ref(false);
// const error = ref<string | null>(null);
const storeDetail = useProductDetailStore();
const { product, loading, reviews, images, variants } =
  storeToRefs(storeDetail);

// Получаем продукт
await useAsyncData("product-detail-page-product", () =>
  storeDetail.fetchProduct(productId)
);

// Получаем первую страницу отзывов
await useAsyncData("product-detail-page-product-reviews", () =>
  storeDetail.fetchAllReviews(1, 5, productId)
);

const currentPage = computed<ILink>(() => ({
  title: product.value?.title ?? "Товар",
  url: `/product/${product.value?.id}`,
}));

const allImages = computed(() => {
  if (images.value) {
    return [
      ...images.value,
      { id: images.value.length + 1, image: product.value?.avatar },
    ];
  }
  return product.value?.avatar;
});
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
        <ProductDetailImages v-if="images" :images="images" />
        <ProductDetailInfo v-if="product" :product="product" />
      </div>
      <ProductDetailComments v-if="reviews" :reviews />
    </div>
  </div>
  <!-- <pre>
    {{ allImages }}
  </pre> -->
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
