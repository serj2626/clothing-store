<script setup lang="ts">
import { productDetailPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { ILink } from "~/components/base/BaseBreadCrumbs.vue";

const { id } = useRoute().params;
const productId = Array.isArray(id) ? id[0] : id;

const storeDetail = useProductDetailStore();
const { product, loading, reviews, images, variants } =
  storeToRefs(storeDetail);

// Получаем продукт
// await callOnce("product-detail-page-product", () =>
//   storeDetail.fetchProduct(productId)
// );


watchEffect( async () => {
  await storeDetail.fetchProduct(productId);
})

// Получаем первую страницу отзывов
await useAsyncData("product-detail-page-product-reviews", () =>
  storeDetail.fetchAllReviews(1, 5, productId)
);

const currentPage = computed<ILink>(() => ({
  title: product.value?.title ?? "Товар",
  url: `/product/${product.value?.id}`,
}));

const allImages = computed(() => {
  return [
    ...images.value,
    { id: images.value.length + 1, image: product.value?.avatar },
  ];
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
        <NuxtImg
          v-if="images.length === 0"
          :src="product.avatar"
          format="webp"
          lazy="loading"
        />
        <ProductDetailImages v-else :images="allImages" />
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
    gap: 50px;
  }
}
</style>
