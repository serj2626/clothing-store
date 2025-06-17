<script setup lang="ts">
import { ref } from "vue";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Thumbs } from "swiper/modules";
import "swiper/css";
import "swiper/css/thumbs";
import type { IProductImage } from "~/types";

const thumbsSwiper = ref<any>(null);
const mainSwiper = ref<any>(null);

function setThumbsSwiper(swiper: any) {
  thumbsSwiper.value = swiper;
}

function setMainSwiper(swiper: any) {
  mainSwiper.value = swiper;
}

defineProps<{
  images: IProductImage[];
}>();
</script>

<template>
  <div 
    v-if="images?.length > 1" 
    class="gallery">
    <!-- Миниатюры (вертикальные) -->
    <Swiper
      class="gallery-thumbs"
      :direction="'vertical'"
      :space-between="10"
      :slides-per-view="4"
      :watch-slides-progress="true"
      :modules="[Thumbs]"
      @swiper="setThumbsSwiper"
    >
      <SwiperSlide v-for="item in images" :key="item.id">
        <NuxtImg
          v-if="item.image"
          :src="item.image"
          format="webp"
          loading="lazy"
          width="100"
          height="100"
        />
      </SwiperSlide>
    </Swiper>

    <!-- Основное изображение -->
    <Swiper
      class="gallery-top"
      :thumbs="{ swiper: thumbsSwiper }"
      :slides-per-view="1"
      :space-between="10"
      :modules="[Thumbs]"
      @swiper="setMainSwiper"
    >
      <SwiperSlide v-for="item in images" :key="item.id">
        <NuxtImg
          v-if="item.image"
          :src="item.image"
          format="webp"
          loading="lazy"
          width="600"
          height="600"
        />
      </SwiperSlide>
    </Swiper>
  </div>
  <NuxtImg
    v-else
    :src="images[0]"
    format="webp"
    loading="lazy"
    width="500"
    height="500"
  />
</template>

<style scoped lang="scss">
.gallery {
  display: flex;
  gap: 20px;
  height: 500px; /* Фиксированная высота контейнера */

  .gallery-thumbs {
    width: 100px;
    height: 100%;

    .swiper-slide {
      height: calc(25% - 10px); /* 4 слайда с учетом gap */
      cursor: pointer;
      opacity: 0.6;
      transition: opacity 0.3s ease;

      &.swiper-slide-thumb-active {
        opacity: 1;
      }

      img {
        width: 100%;
        height: 100%;
        border-radius: 6px;
        object-fit: cover;
      }
    }
  }

  .gallery-top {
    flex: 1;
    height: 100%;

    .swiper-slide {
      height: 100%;

      img {
        width: 100%;
        height: 100%;
        border-radius: 10px;
        object-fit: contain; /* или cover в зависимости от предпочтений */
      }
    }
  }
}

.no-images {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 300px;
  background-color: #f5f5f5;
  border-radius: 10px;
}
</style>
