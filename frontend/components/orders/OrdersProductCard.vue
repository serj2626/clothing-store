<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
</script>
<template>
  <div class="orders-product-card">
    <div class="orders-product-card__product">
      <div class="orders-product-card__product-image">
        <NuxtImg
          width="95"
          height="auto"
          format="webp"
          src="/favorites/one.png"
        />
      </div>
      <div class="orders-product-card__product-info">
        <p class="orders-product-card__product-info-article">арт. 1589956</p>
        <p class="orders-product-card__product-info-title">Кремовое пальто</p>
      </div>
    </div>
    <div class="orders-product-card__color"></div>
    <select class="orders-product-card__size">
      <option value="S">S</option>
      <option value="M">M</option>
      <option value="L">L</option>
    </select>
    <select class="orders-product-card__count">
      <option value="S">S</option>
      <option value="M">M</option>
      <option value="L">L</option>
    </select>
    <div class="orders-product-card__price">
      <p class="orders-product-card__price-amount">9450 руб</p>
      <button class="orders-product-card__price-delete">
        <Icon
          class="orders-product-card__price-delete-icon"
          name="actions:basket"
          size="20"
        />
      </button>
    </div>
  </div>
</template>
<style scoped lang="scss">
.orders-product-card {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;

  &::after {
    content: "";
    position: absolute;
    bottom: -10px;
    left: 0;
    display: block;
    width: 100%;
    height: 1px;
    background-color: $txt;
    opacity: 0.2;
  }
  &__product {
    display: flex;
    gap: 10px;

    &-info {
      display: flex;
      flex-direction: column;
      justify-content: start;
      gap: 30px;
      &-article {
        color: $accent-dark;
      }
    }
  }
  &__size,
  &__count {
    padding: 15px 30px;
    border-radius: 5px;
    border: 1px solid $accent;
  }
  &__color {
    width: 30px;
    aspect-ratio: 1/1;
    background-color: #f1ddaa;
    border-radius: 50%;
    outline: 1px solid $white;
    outline-offset: -5px;
  }
  &__price {
    display: flex;
    align-items: center;
    gap: 30px;
    &-amount {
      font-weight: 700;
    }
  }
}
</style>
