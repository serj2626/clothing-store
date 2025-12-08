<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Autoplay } from "swiper/modules";
import "swiper/css";
import type { IBrand } from "~/types";
import { NuxtImg } from "#components";
import { api } from "~/api";

const { $api } = useNuxtApp();
const { data: brandsRaw } = await useAsyncData<IBrand[]>("home-brands", () =>
  $api(api.brands.list)
);

// Дублируем слайды для плавного loop
const brands = computed(() => [...(brandsRaw.value ?? []), ...(brandsRaw.value ?? [])]);
</script>

<template>
  <div class="brand-swiper">
    <h2 class="brand-swiper__title">Наши бренды</h2>

    <Swiper
      :modules="[Autoplay]"
      :slides-per-view="10"
      :space-between="30"
      :speed="50000"

      :free-mode="true"
      :loop="true"
      class="brand-swiper__slider"
    >
      <SwiperSlide
        v-for="brand in brands"
        :key="brand.id + '-' + Math.random()"
        class="brand-swiper__slide"
      >
        <NuxtImg
          :src="getPhoto(brand.image)"
          :alt="brand.name"
          format="webp"
          class="brand-swiper__img"
          loading="lazy"
        />
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<style scoped lang="scss">
.brand-swiper {
  width: 100%;
  padding: 20px 0;
  overflow: hidden;

  &__title {
    text-align: center;
    font-size: 36px;
    font-weight: 300;
    margin-bottom: 50px;
    color: var(--color-section-title);

    &::after {
      content: "";
      display: block;
      width: 80px;
      height: 2px;
      background: #e0bea2;
      margin: 20px auto 0;
    }
  }

  &__slider {
    .swiper-wrapper {
      display: flex;
      align-items: center;
    }
  }

  &__slide {
    flex-shrink: 0;
    width: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  &__img {
    width: 100%;
    object-fit: contain;
    display: block;
  }
}
</style>
