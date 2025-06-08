<script setup lang="ts">
import { api } from "~/api";
import type { ICategoryResponse } from "~/types";
const { $api } = useNuxtApp();

const { data: allCategories } = await useAsyncData<ICategoryResponse[]>(
  "catalog-page-list-categories",
  () => $api(api.category.list)
);
</script>
<template>
  <div class="catalog-categories">
    <p class="catalog-categories__title">Категории</p>
    <ul class="catalog-categories__list">
      <li v-for="category in allCategories" :key="category.slug">
        <NuxtLink class="catalog-categories__list-item">
          {{ category.name }}
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>
<style scoped lang="scss">
.catalog-categories {
  position: sticky;
  top: 60px;
  align-self: flex-start;

  &__title {
    font-size: 20px;
    margin-bottom: 30px;
  }
  &__list {
    display: flex;
    flex-direction: column;
    gap: 20px;

    &-item {
      color: $txt;
      cursor: pointer;
      position: relative;

      &::after {
        content: "";
        display: inline;
        height: 1px;
        width: 0;
        background-color: $txt;
        transition: width 0.3s ease;
        margin-top: 2px;
      }

      &:hover::after {
        width: max-content;
      }
    }
  }
}
</style>
