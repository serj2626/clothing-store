<script setup lang="ts">
import { api } from "~/api";
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { ICategoryResponse } from "~/types";
const { $api } = useNuxtApp();

const { data: allCategories } = await useAsyncData<ICategoryResponse[]>(
  "catalog-page-list-categories",
  () => $api(api.category.list)
);

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
        v-for="category in allCategories"
        :key="category.id"
        class="catalog-categories__item"
        :class="{
          'catalog-categories__item--opened': currentCategoryId === category.id,
          'catalog-categories__item--has-children': category.children?.length,
        }"
      >
        <div class="catalog-categories__parent" @click="toggleCategory(category.id)">
          <NuxtLink class="catalog-categories__link">
            {{ category.name }}
          </NuxtLink>

          <button
            v-if="category.children?.length"
            class="catalog-categories__toggle"
            aria-label="Toggle subcategories"
          >
            <Icon
              class="catalog-categories__toggle-icon"
              :name="
                currentCategoryId === category.id
                  ? HeroIcons.UP
                  : HeroIcons.DOWN
              "
              size="18"
            />
          </button>
        </div>

        <Transition name="catalog-categories">
          <ul
            v-if="category.children && currentCategoryId === category.id"
            class="catalog-categories__sublist"
          >
            <li
              v-for="child in category.children"
              :key="child.id"
              class="catalog-categories__subitem"
            >
              <NuxtLink class="catalog-categories__sublink">
                {{ child.name }}
              </NuxtLink>
            </li>
          </ul>
        </Transition>
      </li>
    </ul>
  </aside>
</template>

<style scoped lang="scss">
.catalog-categories {
  position: sticky;
  top: 60px;
  padding: 16px;
  background: var(--color-background);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);

  &__title {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0 0 1.5rem;
    color:var(--color-section-title);
  }

  &__list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  &__item {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    padding: 5px 10px;
    border-radius: $btn_radius;
    // &:hover{
    //   background-color: rgb(238, 235, 235);;
    // }
  }

  &__parent {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    cursor: pointer;
  }

  &__link {
    flex: 1;
    color: var(--color-text);
    text-decoration: none;
    transition: color 0.2s ease;
    padding: 0.5rem 0;
    position: relative;

    &:hover {
      // color: var(--color-accent);

      &::after {
        width: 100%;
      }
    }
  }

  &__toggle {
    background: none;
    border: none;
    padding: 0.25rem;
    cursor: pointer;
    color: $accent;
    transition: all 0.5s ease;
    border-radius: 4px;

    &:hover {
      color: $accent-dark;
      background: rgba(0, 0, 0, 0.05);
    }

    &-icon {
      transition: transform 0.5s ease;
    }
  }

  &__sublist {
    list-style: none;
    padding: 0.5rem 0 0.5rem 1rem;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    border-left: 1px solid var(--color-border);
  }

  &__subitem {
    display: flex;
    transition: color 0.2s ease;
    cursor: pointer;
    // &:hover {
    //   color: $accent-dark;
    // }
  }

  &__sublink {
    color: var(--color-text-secondary);
    text-decoration: none;
    font-size: 0.9rem;
    padding: 0.25rem 0;
    transition: color 0.2s ease;
    cursor: pointer;
    // &:hover {
    //   color: $accent-dark;
    // }
  }
}

.catalog-categories-enter-active,
.catalog-categories-leave-active {
  transition: all 0.5s ease;
  overflow: hidden;
}

.catalog-categories-enter-from,
.catalog-categories-leave-to {
  opacity: 0;
  transform: translateY(-60px);
  max-height: 0;
}

.catalog-categories-enter-to,
.catalog-categories-leave-from {
  opacity: 1;
  transform: translateY(0);
  max-height: 500px;
}
</style>
