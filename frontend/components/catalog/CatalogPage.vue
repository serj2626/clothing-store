<script setup lang="ts">
import { catalogPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";

const productStore = useProductStore();
const isLoading = ref(false);
const error = ref<string | null>(null);

// Загружаем первую страницу при монтировании
onMounted(async () => {
  await loadProducts(1);
});

const loadProducts = async (page: number) => {
  if (isLoading.value) return;

  try {
    isLoading.value = true;
    await productStore.fetchAllProducts(page);
  } catch (e: any) {
    error.value = e.message;
  } finally {
    isLoading.value = false;
  }
};

const loadMore = async () => {
  if (productStore.nextPage && !isLoading.value) {
    await loadProducts(productStore.nextPage);
  }
};
</script>
<template>
  <div class="catalog-page">
    <div v-if="isLoading && productStore.products.length === 0">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <template v-else>
      <div class="container">
        <BaseBreadCrumbs :breadcrumbs="catalogPageBreadcrumbs" />
        <div class="catalog-page__content">
          <CatalogCategories style="flex: 1" />
          <div class="catalog-page__main" style="flex: 3">
            <CatalogFilters />
            <CatalogList :products="productStore.products" />

            <LoadMoreObserver
              v-if="productStore.nextPage && !isLoading"
              @intersect="loadMore"
            />

            <div v-if="isLoading" class="loading-indicator">
              Loading more products...
            </div>
          </div>
        </div>
      </div>
    </template>
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
