<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { ICategoriesBySlugResponse } from "./CatalogPage.vue";

defineProps<{
  categories: ICategoriesBySlugResponse[];
}>();

const currentCategoryId = ref<string | null>(null);

const toggleCategory = (categoryId: string) => {
  currentCategoryId.value =
    currentCategoryId.value === categoryId ? null : categoryId;
};
</script>

<template>
  <aside class="catalog-categories">
    <h2 class="catalog-categories__title">Категории</h2>
    <ul class="catalog-categories__list">
      <li
        v-for="value in categories"
        :key="value.id"
        class="catalog-categories__list-item"
        :class="{ 'is-active': currentCategoryId === value.id }"
      >
        <BaseAccordion>
          <template #summary>
            <div
              class="catalog-categories__list-item-summary"
              @click="toggleCategory(value.id)"
            >
              <span class="catalog-categories__name">{{ value.name }}</span>
              <button class="catalog-categories__list-item-summary-btn">
                <Icon
                  :name="HeroIcons.DOWN"
                  class="catalog-categories__list-item-summary-btn-icon"
                  :class="{ 'is-rotated': currentCategoryId === value.id }"
                />
              </button>
            </div>
          </template>

          <!-- Контент аккордеона -->
          <template #content>
            <div class="catalog-categories__content">
              <!-- Тут можешь добавить подкатегории -->
              <div class="catalog-categories__subitem">
                {{ value.children }}
              </div>
            </div>
          </template>
        </BaseAccordion>
      </li>
    </ul>
  </aside>
</template>

<style scoped lang="scss">
.catalog-categories {
  position: sticky;
  top: 80px;

  &__title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 30px;
  }

  &__list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    // gap: 10px;
  }

  &__list-item {
    border-radius: 12px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    overflow: hidden;

    &:hover {
      transform: translateX(2px);
      // box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05);
      box-shadow:-10px 0 10px 5px rgba(0, 0, 0, 0.13);
      border-color: #cbd5e0;
    }

    // &.is-active {
    //   background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
    //   border-color: #667eea;
    // }
  }

  &__list-item-summary {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 10px;
    cursor: pointer;
    width: 100%;

    flex: 1;
    flex-shrink: 0;
  }

  &__name {
    font-weight: 600;
    color: #2d3748;
    font-size: 1rem;
    line-height: 1.4;
    flex: 1;
  }

  &__list-item-summary-btn {
    // background: rgba(102, 126, 234, 0.1);
    border: none;
    padding: 8px;
    cursor: pointer;
    // color: #667eea;
    transition: all 0.3s ease;
    // border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 32px;
    height: 32px;

    &:hover {
      background: rgba(102, 126, 234, 0.2);
      transform: scale(1.05);
    }

    &:active {
      transform: scale(0.95);
    }
  }

  &__list-item-summary-btn-icon {
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    width: 20px;
    height: 20px;

    &.is-rotated {
      transform: rotate(180deg);
    }
  }

  &__content {
    padding: 0 20px 16px;
  }

  &__subitem {
    padding: 12px 16px;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 8px;
    margin: 4px 0;
    color: #4a5568;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    border-left: 3px solid transparent;

    &:hover {
      background: white;
      border-left-color: #667eea;
      color: #2d3748;
      transform: translateX(4px);
    }
  }
}

// Анимации
.catalog-categories-enter-active,
.catalog-categories-leave-active {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
}

.catalog-categories-enter-from,
.catalog-categories-leave-to {
  opacity: 0;
  transform: translateY(-10px);
  max-height: 0;
}

.catalog-categories-enter-to,
.catalog-categories-leave-from {
  opacity: 1;
  transform: translateY(0);
  max-height: 500px;
}

// Responsive
@media (max-width: 768px) {
  .catalog-categories {
    position: static;
    margin-bottom: 2rem;
    padding: 20px;

    &__list-item-summary {
      padding: 14px 16px;
      min-height: 56px;
    }
  }
}
</style>
