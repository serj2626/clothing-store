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
      <NewsProductsList
        v-if="productNewsCollection"
        :products="productNewsCollection"
      />
      <BaseFormSubscribe />
    </div>
  </div>
</template>