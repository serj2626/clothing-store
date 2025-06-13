<script setup lang="ts">
import { api } from "~/api";
import { newsPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { IProduct } from "~/types";

const { $api } = useNuxtApp();

const { data: productNewsCollection } = await useAsyncData<IProduct[]>(
  "news-page-products-last-list",
  () => $api<IProduct[]>(api.products.last)
);
</script>

<template>
  <div class="news-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="newsPageBreadcrumbs" />
      <div class="news-page__content">
        <h2 class="news-page__content-title">Новые коллекции</h2>
      </div>
      <NewsProductsList :products="productNewsCollection" />
      <BaseFormSubscribe />
    </div>
  </div>
</template>

<style scoped lang="scss">
.news-page {
  &__content {
    &-title {
      @include title_page;
    }
  }
}
</style>
