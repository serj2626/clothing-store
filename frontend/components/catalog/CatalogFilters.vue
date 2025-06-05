<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
</script>
<template>
  <ul class="catalog-filters">
    <li class="catalog-filters__item">
      <span>Размер</span>
      <button style="flex-shrink: 0">
        <Icon style="color: #e0bea2" :name="HeroIcons.DOWN" size="18" />
      </button>
    </li>
    <li class="catalog-filters__item">
      <span>Цвет</span>
      <button style="flex-shrink: 0">
        <Icon style="color: #e0bea2" :name="HeroIcons.DOWN" size="18" />
      </button>
    </li>
    <li class="catalog-filters__item">
      <span>Цена</span>
      <button style="flex-shrink: 0">
        <Icon style="color: #e0bea2" :name="HeroIcons.DOWN" size="18" />
      </button>
    </li>
    <li class="catalog-filters__item">
      <span>Сортировать по</span>
      <button style="flex-shrink: 0">
        <Icon style="color: #e0bea2" :name="HeroIcons.DOWN" size="18" />
      </button>
    </li>
  </ul>
</template>
<style scoped lang="scss">
.catalog-filters {
  display: flex;
  align-items: center;
  gap: 35px;

  &__item {
    display: flex;
    align-items: center;
    gap: 5px;

    span {
      font-size: 16px;
      line-height: 1;
    }

    button {
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0;
      border: none;
      background: none;
    }
  }
}
</style>
