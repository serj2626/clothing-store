<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IProduct } from "~/types";
defineProps<{
  product: IProduct;
}>();
</script>
<template>
  <div class="products-detail-info">
    <p class="products-detail-info__title">{{ product.title }}</p>
    <p class="products-detail-info__price">
      {{ product.price }} {{ product.currency }}
    </p>
    <div class="products-detail-info__colors">
      <div class="products-detail-info__colors-values">asdsadsd</div>
      <div class="products-detail-info__colors-current">
        Цвет: Кофе с молоком меланж
      </div>
    </div>
    <BaseInputSelect
      placeholder="Выберите размер"
      :options="['sm', 'md', 'lg']"
    />
    <div class="products-detail-info__actions">
      <BaseButton
        radius="5px"
        label="В КОРЗИНУ"
        size="lg"
        style="width: 100%"
      />
      <BaseButtonOutline
        radius="5px"
        label="В ИЗБРАННОЕ"
        size="lg"
        style="width: 100%"
      />
    </div>
    <p class="products-detail-info__description">Подробности</p>
    <div
      v-if="product.details?.length === 0"
      class="products-detail-info__accordion"
    >
      <div>Подробности отсутствуют</div>
    </div>
    <div v-else class="products-detail-info__accordion">
      <div
        v-for="detail in product.details"
        :key="detail.id"
        class="products-detail-info__accordion-item"
      >
        <div class="products-detail-info__accordion-item-title">
          <span class="products-detail-info__accordion-item-title-text">{{
            detail.title
          }}</span>
          <button
            class="products-detail-info__accordion-item-title-icon"
            style="flex-shrink: 0"
          >
            <Icon style="color: #e0bea2" :name="HeroIcons.DOWN" size="20" />
          </button>
        </div>
        <div class="products-detail-info__accordion-item-content">
          {{ detail.description }}
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.products-detail-info {
  display: flex;
  flex-direction: column;
  gap: 20px;
  &__title {
    font-size: 20px;
  }
  &__price {
    font-weight: 700;
  }
  &__colors {
    display: flex;
    flex-direction: column;
    gap: 15px;
    &-current {
      font-size: 14px;
      color: #c28859;
    }
  }
  &__actions {
    display: flex;
    align-items: center;
    gap: 20px;
    &-basket {
      background-color: $accent;
      color: $white;
      padding-block: 16px;
      width: 100%;
    }
    &-favorite {
      outline: 1px solid $txt;
      color: $txt;
      padding-block: 16px;
      width: 100%;
    }
  }
  &__accordion {
    display: flex;
    flex-direction: column;
    gap: 20px;
    &-item {
      display: flex;
      flex-direction: column;
      gap: 20px;
      &-title {
        display: flex;
        justify-content: space-between;
        &-text {
          font-weight: 700;
        }
        &-icon {
          color: $accent-dark;
        }
      }
    }
  }
}
</style>
