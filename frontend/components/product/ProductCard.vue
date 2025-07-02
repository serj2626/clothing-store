<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IProduct } from "~/types";

const props = defineProps<IProduct>();

const allColors = computed(() => {
  const colors = props.variants.map((item) => {
    return item.color;
  });
  return colors;
});
// const allSizes = computed(() => {
//   const sizes = props.variants.map((item) => {
//     return item.size;
//   });
//   return sizes;
// });

function sliceTitle(title: string) {
  return title.length > 26 ? `${title.slice(0, 26)}.....` : title;
}
</script>
<template>
  <NuxtLink :to="`/products/${id}`">
    <article class="products-card">
      <div class="products-card__image">
        <button class="products-card__image-icon">
          <Icon :name="HeroIcons.HEART_SOLID" size="24" />
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
        <div class="products-card__info-title">{{ sliceTitle(title) }}</div>
        <div class="products-card__info-price">
          {{ formatNumberCustom(+price) }} {{ currency }}
        </div>
        <div v-if="total_count" class="products-card__info-colors">
          <ProductColor
            v-for="color in allColors"
            :key="color"
            :color="color"
          />
        </div>
        <div v-else class="products-card__info-total">Нет в наличии</div>
        <div v-if="brand" class="products-card__info-brand-yes">
          {{ brand.name }}
        </div>
        <div v-else class="products-card__info-brand-no">Без ТМ</div>
      </div>
    </article>
  </NuxtLink>
</template>
<style scoped lang="scss">
.products-card {
  overflow: hidden;
  border-radius: $btn_radius;
  box-shadow: var(--shadow-product-card);
  height: 100%;
  display: flex;
  flex-direction: column;

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
    height: 300px;
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
      object-fit: contain; // Масштабирует изображение, сохраняя пропорции
      object-position: center; // Центрирует изображение
    }
  }
}
</style>
