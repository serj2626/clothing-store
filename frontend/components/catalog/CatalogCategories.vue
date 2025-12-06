<script setup lang="ts">
import type { ICatalogResponse } from "~/types";
defineProps<{
  categories: ICatalogResponse[];
}>();

const currentCategoryId = ref<string | null>(null);

const getPaddingLeft = (indent: number) => {
  return Number(indent) + 20 + "px";
};
</script>

<template>
  <aside class="catalog-categories">
    <ul class="catalog-categories__list">
      <li
        v-for="value in categories"
        :key="value.id"
        :class="[
          'catalog-categories__list-item',
          { 'is-active': currentCategoryId === value.id },
        ]"
        :style="{ paddingLeft: getPaddingLeft(+value.indent) }"
      >
        <span class="catalog-categories__name">
          <!-- Генерируем отступ в виде символов -->
          <!-- {{ '-'.repeat((value.indent - 1)*2 || 0 * 2) }}  -->
          {{ value.name }}
        </span>

        <div v-if="value.has_children">
          <CatalogCategories :categories="value.children" />
        </div>
      </li>
    </ul>
  </aside>
</template>

<style scoped lang="scss">
.catalog-categories {
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
    gap: 10px;
    margin-top: 10px;
  }

  &__list-item {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    overflow: hidden;
    position: relative;
    transition: transform 0.3s ease;

    // &::after {
    //   content: "";
    //   position: absolute;
    //   top: 0;
    //   left: 0;
    //   bottom: 0;
    //   width: 2px;
    //   transform: scaleY(0);
    //   background-color: $accent-dark;
    //   transition: transform 0.3s ease;
    // }

    // &:hover {
    //   transform: translateX(2px);
    //   &::after {
    //     transform: scaleY(0.6);
    //   }
    // }
  }

  &__list-item-summary {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    // padding: 10px;
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
    border: none;
    padding: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
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
