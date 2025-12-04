<script setup lang="ts">
import { api } from "~/api";
import type { IBrand } from "~/types";
const { $api } = useNuxtApp();

const { data: brands } = await useAsyncData<IBrand[]>("home-brands", () =>
  $api(api.brands.list)
);
</script>
<template>
  <div class="brand-marquee">
    <div class="brand-marquee__track">
      <ul class="brand-marquee__list">
        <li v-for="brand in brands" :key="brand.id" class="brand-marquee__item">
          <NuxtImg
            :src="getMedia(brand.image ?? '')"
            :alt="brand.name"
            format="webp"
            loading="lazy"
            class="brand-marquee__img"
          />
        </li>
      </ul>

      <ul class="brand-marquee__list">
        <li
          v-for="brand in brands"
          :key="'copy-' + brand.id"
          class="brand-marquee__item"
        >
          <NuxtImg
            :src="getMedia(brand.image ?? '')"
            :alt="brand.name"
            format="webp"
            loading="lazy"
            class="brand-marquee__img"
          />
        </li>
      </ul>
    </div>
  </div>
</template>
<style scoped lang="scss">
.brand-marquee {
  overflow: hidden;
  width: 100%;
  padding: 20px 0;
}

.brand-marquee__track {
  display: flex;
  width: fit-content;
  animation: marquee 30s linear infinite;

  &:hover {
    animation-play-state: paused;
  }
}

.brand-marquee__list {
  display: flex;
  gap: 30px;
}

.brand-marquee__item {
  width: 150px;
  flex-shrink: 0;
}

.brand-marquee__img {
  width: 100%;
  object-fit: contain;
  height: auto;
  display: block;
}

@keyframes marquee {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}
</style>
