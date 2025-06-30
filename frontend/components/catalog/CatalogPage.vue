<script setup lang="ts">
import { catalogPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";

const productStore = useProductsStore();
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
        <!-- <div class="catalog-layout">
          <div class="catalog-sidebar">
            <CatalogCategories />
          </div>
          <div class="catalog-content">
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
        </div> -->
        {{ productStore.products[0] }}
      </div>
    </template>
  </div>
</template>

<style scoped lang="scss">
.catalog-layout {
  display: flex;
  gap: 30px;
  margin-top: 20px;
  margin-bottom: 100px;
  position: relative;
}

.catalog-sidebar {
  width: 250px;
  flex-shrink: 0;
  position: sticky;
  top: 20px;
  align-self: flex-start;
  height: fit-content;
  max-height: calc(100vh - 100px);
  overflow-y: auto;
}

.catalog-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.loading-indicator {
  padding: 20px;
  text-align: center;
  color: #666;
}

@media (max-width: 768px) {
  .catalog-layout {
    flex-direction: column;
  }

  .catalog-sidebar {
    width: 100%;
    position: static;
    max-height: none;
  }
}
</style>
