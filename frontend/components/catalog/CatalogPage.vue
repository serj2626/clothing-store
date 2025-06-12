<script setup lang="ts">
import { api } from "~/api";
import { catalogPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { IproductsResponse } from "~/types";
const { $api } = useNuxtApp();

const { data: productsList } = await useAsyncData<IproductsResponse[]>(
  "catalog-page-list-products",
  () => $api(api.products.list)
);
</script>
<template>
  <div class="catalog-page">
    {{ productsList }}
    <!-- <div class="container">
      <BaseBreadCrumbs :breadcrumbs="catalogPageBreadcrumbs" />
      <div class="catalog-page__content">
        <CatalogCategories style="flex: 1" />
        <div class="catalog-page__main" style="flex: 3">
          <CatalogFilters />
          <CatalogList :products="productsList || []" />
        </div>
      </div>
    </div> -->
  </div>
</template>
<style scoped lang="scss">
.catalog-page {
  &__content {
    margin-block: 30px 100px;
    display: flex;
    gap: 15px;
  }
  &__main {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
}
</style>
