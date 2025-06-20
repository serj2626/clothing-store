<script setup lang="ts">
import { ref } from "vue";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Thumbs, FreeMode } from "swiper/modules";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/thumbs";
import "swiper/css/free-mode";
import type { IProductImage } from "~/types";

defineProps<{ images: IProductImage[] }>();

const thumbsSwiper = ref(null);

function onThumbsSwiper(swiperInstance: any) {
  thumbsSwiper.value = swiperInstance;
}
</script>

<template>
  <div class="gallery">
    <Swiper
      direction="vertical"
      :space-between="20"
      :slides-per-view="6"
      free-mode
      watch-slides-progress
      :modules="[FreeMode, Thumbs]"
      @swiper="onThumbsSwiper"
      class="thumbs"
    >
      <SwiperSlide v-for="(img, i) in images" :key="i">
        <img :src="img.image" alt="" />
      </SwiperSlide>
    </Swiper>

    <Swiper
      v-if="thumbsSwiper"
      :thumbs="{ swiper: thumbsSwiper }"
      :modules="[Thumbs]"
      class="main"
    >
      <SwiperSlide v-for="(img, i) in images" :key="i">
        <img :src="img.image" alt="" />
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<style scoped lang="scss">
.gallery {
  display: grid;
  grid-template-columns: 100px 1fr;
  gap: 20px;
  max-height: 600px;

  &.thumbs {
    height: 100%;
    overflow: hidden;

    .swiper {
      height: 100%;
    }

    img {
      width: 100%;
      height: auto;
      border-radius: 6px;
      object-fit: cover;
      cursor: pointer;
      transition: 0.3s;
    }

    .swiper-slide-thumb-active img {
      outline: 2px solid #000;
    }
  }

  &.main {
    height: 100%;

    .swiper {
      height: 100%;
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 6px;
    }
  }
}
</style>
