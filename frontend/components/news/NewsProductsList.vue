<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Pagination, Autoplay } from "swiper/modules";

import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

import type { IProduct } from "~/types";


defineProps<{ products: IProduct[] }>();

const prevEl = ref<HTMLElement | null>(null);
const nextEl = ref<HTMLElement | null>(null);
const paginationRef = ref<HTMLElement | null>(null);
const swiperInstance = ref<any>(null);
const currentSlideIndex = ref(0);

const onSwiper = (swiper: any) => {
  swiperInstance.value = swiper;
};

const onSlideChange = () => {
  currentSlideIndex.value = swiperInstance.value?.activeIndex || 0;
};
</script>
<template>
  <div class="swiper-container">
    <div class="swiper-navigation">
      <button ref="prevEl" class="swiper-button prev">‹</button>
      <button ref="nextEl" class="swiper-button next">›</button>
    </div>

    <Swiper
      v-if="prevEl && nextEl && paginationRef"
      class="swiper-wrapper"
      :modules="[Pagination, Navigation, Autoplay]"
      :autoplay="{ delay: 3000, disableOnInteraction: false }"
      :slides-per-view="4"
      :space-between="20"
      :loop="true"
      :pagination="{ el: paginationRef, clickable: true }"
      :navigation="{ prevEl, nextEl }"
      :breakpoints="{
        320: {
          slidesPerView: 1,
          spaceBetween: 10,
        },
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
        1024: {
          slidesPerView: 4,
          spaceBetween: 20,
        },
      }"
      @slide-change="onSlideChange"
      @swiper="onSwiper"
    >
      <SwiperSlide
        v-for="product in products || []"
        :key="product.id"
        class="swiper-slide"
      >
        <ProductCard v-bind="product" />
      </SwiperSlide>
    </Swiper>

    <div ref="paginationRef" class="swiper-pagination" />
  </div>
</template>
<style scoped lang="scss">
.swiper-container {
  position: relative;
}

.swiper-wrapper {
  border-radius: 10px;
}

.swiper-pagination {
  position: relative;
  text-align: center;
  margin-top: 12px;
  z-index: 5;

  &:deep(.swiper-pagination-bullet) {
    width: 10px;
    height: 10px;
    display: inline-block;
    border-radius: 50%;
    background: $txt;
    margin: 0 5px;
    cursor: pointer;
    opacity: 1;
    transition: opacity 0.3s ease;
  }

  &:deep(.swiper-pagination-bullet-active) {
    opacity: 1;
    background: #e0bea2;
  }
}

.swiper-navigation {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  z-index: 10;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transform: translateY(-50%);
  padding: 0 10px;

  .swiper-button {
    background: #e0bea2;
    border: none;
    font-size: 28px;
    font-weight: bold;
    color: $white;
    border-radius: 50%;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: all 0.3s ease;

    &:hover {
      background: #d38f56;
      color: #fff;
      transform: scale(1.1);
    }

    &:active {
      transform: scale(0.95);
    }

    &.prev {
      margin-left: 0;
    }

    &.next {
      margin-right: 0;
    }
  }
}
</style>
