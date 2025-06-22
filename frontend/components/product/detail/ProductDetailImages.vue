<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation } from "swiper/modules";
import type { Swiper as SwiperType } from "swiper/types";
import type { IProductImage } from "~/types";

const swiperInstance = ref<SwiperType | null>(null);
const realIndex = ref(0);

const onSwiper = (swiper: SwiperType) => {
  swiperInstance.value = swiper;
};

const onSlideChange = (swiper: SwiperType) => {
  realIndex.value = swiper.realIndex;
};

const goTo = (index: number) => {
  swiperInstance.value?.slideToLoop(index);
};

const props = defineProps<{
  images: IProductImage[];
}>();

const currentImg = computed(() => props.images[realIndex.value]?.image);
</script>

<template>
  <div class="swiper-container">
    <!-- Thumbnail Swiper -->
<Swiper
  :modules="[Navigation]"
  :slides-per-view="5"
  :space-between="5"
  direction="vertical"
  :loop="true"
  :free-mode="true"
  class="thumbnail-swiper"
  @swiper="onSwiper"
  @slide-change="onSlideChange"
>
      <SwiperSlide
        v-for="(image, index) in images"
        :key="image.id"
        class="thumbnail-slide"
        @click="goTo(index)"
      >
        <img
          :src="image.image"
          :alt="`Thumbnail ${index + 1}`"
          width="80"
          height="80"
          class="thumbnail-image"
          :class="{ 'active-thumbnail': realIndex === index }"
        />
      </SwiperSlide>
    </Swiper>

    <!-- Main Image Display -->
    <div class="main-image-container">
      <NuxtImg
        :src="currentImg"
        format="webp"
        loading="lazy"
        width="600"
        height="600"
        class="main-image"
      />
    </div>
  </div>
</template>

<style scoped>
.swiper-container {
  max-height: 600px;
  display: grid;
  grid-template-columns: minmax(100px, 200px) 1fr;
  gap: 10px;
}

.thumbnail-swiper {
  height: 100%;
}

.thumbnail-slide {
  cursor: pointer;
  margin-bottom: 10px;
  opacity: 0.6;
  transition: opacity 0.3s ease;
}

.thumbnail-slide:hover,
.active-thumbnail {
  opacity: 1;
}

.thumbnail-image {
  width: 100%;
  height: 80px;
  object-fit: cover;
  border: 1px solid #eee;
  border-radius: 4px;
}

.main-image-container {
  position: relative;
  height: 100%;
}

.main-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
