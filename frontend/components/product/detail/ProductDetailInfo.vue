<script setup lang="ts">
import { api } from "~/api";
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IProduct, IProductVariant } from "~/types";

const productStoreDetail = useProductDetailStore();
const modalsStore = useModalsStore();
const error = ref("");

const currentColor = ref<string>('')

const { $api } = useNuxtApp();
defineProps<{
  product: IProduct;
  variants: IProductVariant[];
}>();

const activeIndex = ref<number | null>(null);

function toggleAccordion(id: number): void {
  activeIndex.value = activeIndex.value === id ? null : id;
}

async function addLikeByProduct(id: string) {
  try {
    await $api(api.products.like(id), { method: "POST" });
    await productStoreDetail.fetchProduct(id);
  } catch (e: unknown) {
    error.value =
      e instanceof Error ? e.message : "Произошла ошибка при добавлении лайка";
  }
}
</script>

<template>
  <div class="products-detail-info">
    <p class="products-detail-info__title">
      <span class="title-span">Название: </span>{{ product.title }}
    </p>
    <p class="products-detail-info__article">
      <span class="title-span">Артикул: </span>{{ product.id }}
    </p>
    <p
      class="products-detail-info__brand"
      :style="{ cursor: product.brand ? 'pointer' : 'default' }"
      @click="product.brand && modalsStore.openModal('brand', product.brand)"
    >
      <span class="title-span">Торговая марка: </span>
      {{ product.brand ? product.brand.name : "Без ТМ" }}
    </p>
    <p class="products-detail-info__price">
      <span class="title-span">Цена: </span> {{ product.price }}
      {{ product.currency }}
    </p>
    <div class="products-detail-info__colors">
      <div class="products-detail-info__colors-values">
        <ProductColor
          v-for="item in variants"
          :key="item.color"
          :color="item.color"
          :title="item.color_name"
          size="22px"
          @updated:new-color="currentColor = item.color_name"
        />
      </div>
      <div class="products-detail-info__colors-current">
        <!-- Цвет: Кофе с молоком меланж -->
        Цвет: {{ currentColor }}
      </div>
    </div>
    <BaseInputSelect
      placeholder="Выберите размер"
      :options="['sm', 'md', 'lg']"
    />
    <button
      class="products-detail-info__likes"
      :class="{ 'products-detail-info__likes_active': product.liked }"
      @click="addLikeByProduct(product.id)"
    >
      <Icon
        :name="HeroIcons.HEART_SOLID"
        class="products-detail-info__likes-icon"
      />
      <span class="products-detail-info__likes-count"
        >{{ product.count_likes }} человеку понравился товар
        {{ product.liked }}</span
      >
    </button>
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

    <div v-if="!product.details?.length" class="products-detail-info__empty">
      Подробности отсутствуют
    </div>

    <div v-else class="products-detail-info__accordion">
      <BaseAccordionComponent
        v-for="detail in product.details"
        :key="detail.id"
        :is-open="activeIndex === detail.id"
        class="products-detail-info__accordion-item"
        @click="toggleAccordion(detail.id)"
      >
        <template #summary>
          <div class="products-detail-info__accordion-item-title">
            <span class="products-detail-info__accordion-item-title-text">
              {{ detail.title }}
            </span>
            <button
              class="products-detail-info__accordion-item-title-icon"
              style="flex-shrink: 0"
            >
              <Icon
                style="color: #e0bea2"
                :name="
                  activeIndex === detail.id ? HeroIcons.UP : HeroIcons.DOWN
                "
                size="20"
              />
            </button>
          </div>
        </template>
        <template #default>
          <div class="products-detail-info__accordion-item-content">
            {{ detail.description }}
          </div>
        </template>
      </BaseAccordionComponent>
    </div>
  </div>
</template>

<style scoped lang="scss">
.products-detail-info {
  display: flex;
  flex-direction: column;
  gap: 20px;

  &__likes {
    display: flex;
    align-items: center;
    gap: 8px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px 12px;
    border-radius: 6px;
    transition: $default_transition;
    font-family: $ff_second;
    color: $txt;

    &:hover {
      background: rgba($accent, 0.1);
    }

    &_active {
      color: red;
    }

    &-count {
      font-size: 14px;
      color: rgba($txt, 0.7);
    }
    &-icon {
      font-size: 20px;
      background-color: red;
      transition: $default_transition;
    }
  }

  &__title {
  }
  &__article {
  }

  &__price {
  }

  &__colors {
    display: flex;
    flex-direction: column;
    gap: 15px;
    &-values {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    &-current {
      font-size: 14px;
      color: #c28859;
    }
  }

  &__actions {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  &__description {
    font-weight: 700;
    margin-top: 20px;
  }

  &__empty {
    color: rgba(0, 0, 0, 0.5);
    font-style: italic;
  }

  &__accordion {
    display: flex;
    flex-direction: column;
    gap: 30px;
    margin-top: 20px;

    &-item {
      &-title {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 5px;

        &-text {
          font-weight: 700;
        }

        &-icon {
          color: $accent-dark;
          background: none;
          border: none;
          cursor: pointer;
        }
      }

      &-content {
        padding-top: 10px;
      }
    }
  }
}

.title-span {
  font-weight: 700;
  color: rgba($txt, 0.9);
}
</style>
