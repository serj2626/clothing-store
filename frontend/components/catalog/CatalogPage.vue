<script setup lang="ts">
import { api } from "~/api";
import { catalogPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
const { $api } = useNuxtApp();

const productStore = useProductStore();
const { products } = storeToRefs(productStore);
const isLoading = ref(false);
const error = ref<string | null>(null);

// Загружаем первую страницу при монтировании
onMounted(async () => {
  try {
    isLoading.value = true;
    await productStore.fetchAllProducts(1);
  } catch (e: any) {
    error.value = e.message;
  } finally {
    isLoading.value = false;
  }
});

// Функция для загрузки следующей страницы
const loadMore = async () => {
  if (productStore.nextPage) {
    try {
      isLoading.value = true;
      await productStore.fetchAllProducts(productStore.nextPage);
    } catch (e: any) {
      error.value = e.message;
    } finally {
      isLoading.value = false;
    }
  }
};
</script>
<template>
  <div class="catalog-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="catalogPageBreadcrumbs" />
      <div class="catalog-page__content">
        <CatalogCategories style="flex: 1" />
        <div class="catalog-page__main" style="flex: 3">
          <CatalogFilters />
          <div v-if="isLoading && productStore.products.length === 0">Loading...</div>
          <CatalogList v-else :products />
        </div>
      </div>
    </div>
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
