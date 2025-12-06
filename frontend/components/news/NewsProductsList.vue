<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Pagination, Autoplay } from "swiper/modules";
import type { Swiper as SwiperType } from "swiper";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

import type { IProduct } from "~/types";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

defineProps<{ products: IProduct[] }>();

// ссылка на инстанс swiper
const swiperInstance = ref<SwiperType | null>(null);

// актуальный индекс
const currentSlideIndex = ref(0);

// вызывается когда swiper инициализирован
const onSwiper = (swiper: SwiperType) => {
  swiperInstance.value = swiper;
};

// вызывается на смене слайда
const onSlideChange = () => {
  currentSlideIndex.value = swiperInstance.value?.activeIndex || 0;
};

// методы управления
const goNext = () => swiperInstance.value?.slideNext();
const goPrev = () => swiperInstance.value?.slidePrev();
</script>

<template>
  <div class="swiper-container">
    <div class="swiper-container__header">
      <h1 class="swiper-container__header-title">Новые коллекции</h1>
      <!-- кастомные кнопки -->
      <div class="swiper-container__header-buttons">
        <button class="swiper-prev" @click="goPrev">
          <Icon :name="HeroIcons.ARROW_LEFT_SOLID" class="swiper-prev--icon" />
        </button>
        <button class="swiper-next" @click="goNext">
          <Icon :name="HeroIcons.ARROW_RIGHT_SOLID" class="swiper-next--icon" />
        </button>
      </div>
    </div>
    <!-- swiper -->
    <Swiper
      class="swiper-wrapper"
      :modules="[Pagination, Navigation, Autoplay]"
      :autoplay="{ delay: 3000, disableOnInteraction: true }"
      :slides-per-view="4"
      :space-between="20"
      :loop="true"
      :pagination="{ el: '.swiper-pagination', clickable: true }"
      :navigation="{ nextEl: '.swiper-next', prevEl: '.swiper-prev' }"
      :breakpoints="{
        320: { slidesPerView: 1, spaceBetween: 10 },
        640: { slidesPerView: 2, spaceBetween: 15 },
        768: { slidesPerView: 3, spaceBetween: 20 },
        1024: { slidesPerView: 4, spaceBetween: 20 },
      }"
      @slide-change="onSlideChange"
      @swiper="onSwiper"
    >
      <SwiperSlide
        v-for="product in products"
        :key="product.id"
        class="swiper-slide"
      >
        <ProductCard v-bind="product" />
      </SwiperSlide>
    </Swiper>

    <!-- кастомная пагинация -->
    <div class="swiper-pagination" />
  </div>
</template>

<style scoped lang="scss">
.swiper-container {
  position: relative;

  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-block: 30px;

    &-title {
      font-size: 22px;
      font-weight: 700;
      color: var(--color-section-title);
      margin: 0;
    }

    &-buttons {
      display: flex;
      gap: 10px;

      .swiper-prev,
      .swiper-next {
        cursor: pointer;
        padding: 8px 12px;
        background-color: $accent-dark;
        color: #fff;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: background-color 0.3s ease;

        &:hover {
          background-color: $accent;
        }

        &--icon {
          width: 22px;
          height: 22px;
        }
      }
    }
  }
}

.swiper-pagination {
  position: relative;
  text-align: center;
  margin-top: 32px;

  &:deep(.swiper-pagination-bullet) {
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background: #333;
    margin: 0 5px;
    opacity: 0.4;
  }

  &:deep(.swiper-pagination-bullet-active) {
    background: #e0bea2;
    opacity: 1;
  }
}
</style>
