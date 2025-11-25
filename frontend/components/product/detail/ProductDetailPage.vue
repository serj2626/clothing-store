<script setup lang="ts">
import { productDetailPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import { api } from "~/api";
import type { IProduct } from "~/types";

const { $api } = useNuxtApp();
const { id } = useRoute().params;
const productId = Array.isArray(id) ? id[0] : id;

const storeDetail = useProductDetailStore();
const { reviews, images, variants } = storeToRefs(storeDetail);

const { data: productData } = await useAsyncData<IProduct>(
  `product-detail-page-${productId}`,
  () => $api(api.products.detail(productId)),
  {
    watch: [() => productId],
  }
);
const currentPage = computed(() => ({
  title: productData.value?.title ?? "Товар",
  url: `/product/${productData.value?.id}`,
}));

const activeImg = ref<string | null>(null);

// Все изображения: основное + варианты
const allImages = computed(() => {
  const mainImage = productData.value?.avatar
    ? {
        id: "main",
        image: productData.value.avatar,
      }
    : null;

  const variantImages =
    productData.value?.variants?.map((variant) => ({
      id: variant.id,
      image: variant.image,
    })) || [];

  return mainImage ? [mainImage, ...variantImages] : variantImages;
});

// Активное изображение
const currentImg = computed(() => {
  return activeImg.value || productData.value?.avatar;
});

// // Устанавливаем первое изображение активным при загрузке
// watchEffect(() => {
//   if (allImages.value.length > 0 && !activeImg.value) {
//     activeImg.value = allImages.value[0].image;
//   }
// });

function setNewImage(image: string) {
  activeImg.value = image;
}
</script>

<template>
  <div class="product-detail-page">
    <div class="container">
      <BaseBreadCrumbs
        :breadcrumbs="productDetailPageBreadcrumbs"
        :current-page="currentPage"
      />
      <div class="product-detail-page__content">
        <ProductDetailImages
          :all-images="allImages"
          :current-img="currentImg ?? ''"
          @check-new-image="setNewImage"
        />
        <ProductDetailInfo
          v-if="productData"
          :product="productData"
          :variants="productData.variants"
        />
      </div>
      <CommentList :reviews="reviews" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.product-detail-page {
  &__content {
    margin-block: 50px;
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 10px;
    align-items: start;

    @media (max-width: 1024px) {
      grid-template-columns: 1fr;
      gap: 40px;
    }

    // &-images {
    //   display: grid;
    //   grid-template-columns: 150px 1fr;
    //   height: 650px;

    //   // @media (max-width: 768px) {
    //   //   grid-template-columns: 80px 1fr;
    //   //   height: 500px;
    //   // }

    //   // @media (max-width: 480px) {
    //   //   grid-template-columns: 1fr;
    //   //   grid-template-rows: auto 1fr;
    //   //   height: auto;
    //   //   gap: 15px;
    //   // }

    //   // Контейнер для миниатюр
    //   &-thumbnails {
    //     display: flex;
    //     flex-direction: column;
    //     gap: 12px;
    //     height: 100%;
    //     overflow-y: auto;
    //     padding-right: 8px;

    //     // Кастомный скроллбар
    //     &::-webkit-scrollbar {
    //       width: 4px;
    //     }

    //     &::-webkit-scrollbar-track {
    //       background: #f1f1f1;
    //       border-radius: 2px;
    //     }

    //     &::-webkit-scrollbar-thumb {
    //       background: $accent-dark;
    //       border-radius: 2px;

    //       &:hover {
    //         background: #794545;
    //       }
    //     }

    //     @media (max-width: 480px) {
    //       flex-direction: row;
    //       height: 80px;
    //       overflow-x: auto;
    //       overflow-y: hidden;
    //       padding-right: 0;
    //       padding-bottom: 8px;
    //     }
    //   }

    //   // Контейнер для основного изображения
    //   &-main {
    //     height: 100%;
    //     // display: flex;
    //     // align-items: center;
    //     // justify-content: center;

    //     .main-image {
    //       width: 100%;
    //       height: 100%;
    //       background-size: contain;
    //       background-position: center;
    //       background-repeat: no-repeat;
    //       border-radius: 12px;
    //       transition: all 0.3s ease;
    //     }
    //   }
    // }
  }
}

// Стили для миниатюр
// .thumbnail-item {
//   width: 100%;
//   aspect-ratio: 1;
//   border-radius: 8px;
//   overflow: hidden;
//   cursor: pointer;
//   border: 2px solid transparent;
//   transition: all 0.2s ease;
//   flex-shrink: 0;

//   &:hover {
//     border-color: $accent-dark;
//   }

//   &.active {
//     border-color: $accent-dark;
//     box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
//   }

//   .thumbnail-img {
//     width: 100%;
//     height: 100%;
//     object-fit: cover;
//     border-radius: 6px;
//   }

//   @media (max-width: 480px) {
//     width: 70px;
//     height: 70px;
//   }
// }
</style>
