<script setup lang="ts">
import { productDetailPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import { api } from "~/api";
import type { IProduct } from "~/types";
const { $api } = useNuxtApp();
const { id } = useRoute().params;
const productId = Array.isArray(id) ? id[0] : id;

const storeDetail = useProductDetailStore();
const { reviews, images, variants } = storeToRefs(storeDetail);

// watchEffect(async () => {
//   await storeDetail.fetchProduct(productId);
// });

const { data: productData } = await useAsyncData<IProduct>(
  `product-detail-page-${productId}`,
  () => $api(api.products.detail(productId)),
  {
    watch: [() => productId],
  }
);

// // Получаем отзывы
// await useAsyncData("product-detail-page-product-reviews", () =>
//   storeDetail.fetchAllReviews(1, 5, productId)
// );

const currentPage = computed(() => ({
  title: productData.value?.title ?? "Товар",
  url: `/product/${productData.value?.id}`,
}));

// const allImages = computed(() => {
//   return [
//     ...images.value,
//     { id: images.value.length + 1, image: product.value?.avatar },
//   ];
// });
</script>

<template>
  <div class="product-detail-page">
    <div class="container">
      <BaseBreadCrumbs
        :breadcrumbs="productDetailPageBreadcrumbs"
        :current-page="currentPage"
      />
      {{ variants }}
      <div class="product-detail-page__content">
        <NuxtImg
          :src="getMedia(productData?.avatar ?? '')"
          format="webp"
          lazy="loading"
        />
        <!-- <ProductDetailImages v-else :images="allImages" /> -->
        <ProductDetailInfo
          v-if="productData"
          :product="productData"
          :variants="productData.variants"
        />
      </div>
      <!-- <CommentList v-if="reviews" :reviews /> -->
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
