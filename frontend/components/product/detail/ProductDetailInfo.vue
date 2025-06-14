<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
</script>
<template>
  <div class="products-detail-info">
    <p class="products-detail-info__title">Кремовое пальто</p>
    <p class="products-detail-info__price">3150 руб</p>
    <div class="products-detail-info__colors">
      <div class="products-detail-info__colors-values">asdsadsd</div>
      <div class="products-detail-info__colors-current">
        Цвет: Кофе с молоком меланж
      </div>
    </div>
    <select class="products-detail-info__sizes">
      <option value="">Выберите размер</option>
      <option value="">sm</option>
      <option value="">md</option>
      <option value="">xl</option>
      <option value="">2xl</option>
    </select>
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
    <div class="products-detail-info__accordion">
      <div class="products-detail-info__accordion-item">
        <div class="products-detail-info__accordion-item-title">
          <span class="products-detail-info__accordion-item-title-text"
            >Обмеры и описание</span
          >
          <button
            class="products-detail-info__accordion-item-title-icon"
            style="flex-shrink: 0"
          >
            <Icon style="color: #e0bea2" :name="HeroIcons.DOWN" size="20" />
          </button>
        </div>
        <div class="products-detail-info__accordion-item-content">
          Состав и уход Состав: 50% Шерсть, 50% Полиэстер Подкладка: 100%
          Полиэстер Утеплитель: 90% Пух, 10% Перо - Не стирать - Гладить при
          температуре утюга до 110°C - Не отбеливать - Сухая чистка (химчистка)
          - Барабанная сушка запрещена
        </div>
      </div>
      <div class="products-detail-info__accordion-item">
        <div class="products-detail-info__accordion-item-title">
          <span class="products-detail-info__accordion-item-title-text"
            >Состав и уход</span
          >
          <button
            class="products-detail-info__accordion-item-title-icon"
            style="flex-shrink: 0"
          >
            <Icon style="color: #e0bea2" :name="HeroIcons.DOWN" size="20" />
          </button>
        </div>
        <div class="products-detail-info__accordion-item-content">
          Состав и уход Состав: 50% Шерсть, 50% Полиэстер Подкладка: 100%
          Полиэстер Утеплитель: 90% Пух, 10% Перо - Не стирать - Гладить при
          температуре утюга до 110°C - Не отбеливать - Сухая чистка (химчистка)
          - Барабанная сушка запрещена
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
  &__sizes {
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
      &-content {
      }
    }
  }
}
</style>
