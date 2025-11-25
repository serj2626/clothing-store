<script lang="ts" setup>
import { api } from "~/api";
const { $api } = useNuxtApp();

export interface ICategoryResponse {
  name: string;
  slug: string;
  image: string;
}

const { data: categoriesList } = await useAsyncData<ICategoryResponse[]>(
  "home-page-list-categories",
  () => $api(api.category.list)
);
</script>

<template>
  <div class="home-page">
    <HomeSectionHero />
    <HomeSectionCategories
      id="catalog"
      v-bind="$attrs"
      :list="categoriesList || []"
    />
    <BaseFormSubscribe />
  </div>
</template>

<style scoped lang="scss">
.home-page {
  &__categories {
    &-title {
      margin-block: 100px 50px;
      color: #252525;
      font-size: 36px;
      font-weight: 300;
    }

    &-list {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 100px;

      &-item {
        position: relative;

        &-img {
          width: 100%;
        }

        &-value {
          position: absolute;
          bottom: 0;
          width: 100%;
          padding-block: 15px;
          text-align: center;
          font-size: 20px;
          font-weight: 400;
          color: #fff;
          background-color: #e0bea2c1;
        }
      }
    }
  }
}
</style>
