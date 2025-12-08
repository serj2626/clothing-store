<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { ILastProduct } from "~/types";

defineProps<ILastProduct>();

function sliceTitle(title: string) {
  return title.length > 26 ? `${title.slice(0, 26)}.....` : title;
}
</script>
<template>
  <NuxtLink class="card" :to="`/products/${id}`">
    <article class="product-card">
      <div class="product-card__image">
        <button class="product-card__image-icon">
          <Icon :name="HeroIcons.HEART_SOLID" size="24" />
        </button>
        <div
          class="product-card__image-bg"
          style="width: 100%; height: 100%"
          :style="{
            backgroundImage: `url(${getPhoto(avatar)})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center top',
            backgroundRepeat: 'no-repeat',
          }"
        />
      </div>

      <div class="product-card__info">
        <div class="product-card__info-title">
          {{ sliceTitle(title) }}
        </div>
        <div class="product-card__info-brand-yes">
          {{ brand || "Без ТМ" }}
        </div>
      </div>
    </article>
  </NuxtLink>
</template>
<style scoped lang="scss">
.product-card {
  overflow: hidden;
  border-radius: $btn_radius;
  box-shadow: var(--shadow-product-card);
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: $bg;

  &__info {
    padding: 15px 30px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    align-items: center;
    flex-grow: 1;
    &-price {
      font-weight: 700;
      color: var(--color-text);
    }
    &-sizes {
      opacity: 0.5;
    }
    &-title {
      color: var(--color-text);
    }
    &-colors {
      display: flex;
      align-items: center;
      gap: 5px;
    }
    &-total {
      color: $error;
      font-weight: 600;
    }
    &-brand-yes {
      color: var(--color-text);
    }
    &-brand-no {
      color: var(--color-text);
    }
  }

  &__image {
    overflow: hidden;
    position: relative;
    width: 100%;
    height: 250px;
    display: block;

    @include mediaTablet {
      height: 400px;
    }

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
      object-fit: contain;
      object-position: center;
    }
  }
}
</style>
