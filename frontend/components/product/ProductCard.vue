<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IproductsResponse } from "~/types";
defineProps<IproductsResponse>();
</script>
<template>
  <NuxtLink :to="`/products/${id}`">
    <article class="products-card">
      <div class="products-card__image">
        <button class="products-card__image-icon">
          <Icon :name="HeroIcons.HEART" size="24" />
        </button>
        <NuxtImg
          v-if="!avatar"
          format="webp"
          loading="lazy"
          class="products-card__image-item"
          src="favorites/one.png"
        />
        <NuxtImg
          v-else
          format="webp"
          loading="lazy"
          class="products-card__image-item"
          :src="avatar"
          :alt="title"
        />
      </div>

      <div class="products-card__info">
        <div class="products-card__info-title">{{ title }}</div>
        <div class="products-card__info-price">{{ price }}</div>
        <div class="products-card__info-sizes">{{ variants }}</div>
        <!-- <div class="products-card__info-colors">
          <ProductColor v-for="color in colors" :key="color" :color="color" />
        </div> -->
      </div>
    </article>
  </NuxtLink>
</template>
<style scoped lang="scss">
.products-card {
  &__info {
    padding-top: 15px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    align-items: center;
    &-price {
      font-weight: 700;
      color: $txt;
    }
    &-sizes {
      opacity: 0.5;
    }
    &-title {
      color: $txt;
    }
    &-colors {
      display: flex;
      align-items: center;
      gap: 5px;
    }
  }

  &__image {
    position: relative;
    width: 100%;
    height: 400px;
    display: block;

    &-icon {
      position: absolute;
      top: 0px;
      right: 0px;
      width: 50px;
      height: 50px;
      border-bottom-left-radius: 25px;
      background-color: $accent;
      display: flex;
      justify-content: center;
      align-items: center;
      color: $white;
    }

    &-item {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
  }
}
</style>
