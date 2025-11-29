<script setup lang="ts">
import { api } from "~/api";
import { catalogPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import type { IProductResponse } from "~/types";

const productStore = useProductsStore();
const isLoading = ref(false);
const error = ref<string | null>(null);
const { $api } = useNuxtApp();

const { slug } = useRoute().params;

export interface ICategoriesBySlugResponse {
  id: string;
  name: string;
  slug: string;
  has_children: boolean;
  children: ICategoriesBySlugResponse[];
}

// Загружаем первую страницу при монтировании
// onMounted(async () => {
//   await loadProducts(1);
// });

const { data: productsList } = await useAsyncData<IProductResponse>(
  `catalog-page-list-products-${slug}`,
  () => productStore.fetchAllProducts(1, 15, slug as string),
  {
    watch: [() => slug],
  }
);

const { data: categoriesData } = await useAsyncData<ICategoriesBySlugResponse>(
  `catalog-page-list-categories-${slug}`,
  () => $api(api.category.listBySlug(slug as string)),
  {
    watch: [() => slug],
  }
);

const loadProducts = async (page: number) => {
  if (isLoading.value) return;

  try {
    isLoading.value = true;
    await productStore.fetchAllProducts(page);
  } catch (e: unknown) {
    if (e instanceof Error) {
      error.value = e.message;
    } else {
      error.value = "Ошибка получения товаров";
    }
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
        <div class="catalog-layout">
          <div class="catalog-sidebar">
            <CatalogCategories :categories="categoriesData?.children || []" />
          </div>
          <div class="catalog-content">
            <h1 style="text-align: center; font-size: 45px">
              {{ categoriesData?.name }}
            </h1>
            <CatalogFilters />
            <CatalogList
              v-if="productsList?.results"
              :products="productsList?.results"
            />
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
.catalog-layout {
  margin-top: 20px;
  margin-bottom: 100px;
  
  &:after {
    content: "";
    display: table;
    clear: both;
  }
}

.catalog-sidebar {
  width: 250px;
  float: left;
  position: sticky;
  top: 20px;
  height: fit-content;
  max-height: calc(100vh - 100px);
  overflow-y: auto;
}

.catalog-content {
  float: left;
  width: calc(100% - 290px); /* 100% минус сайдбар + отступ */
  margin-left: 40px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 30px;
  
  /* Если контент выше сайдбара - он займет всю ширину автоматически */
}

.loading-indicator {
  padding: 20px;
  text-align: center;
  color: #666;
}

@media (max-width: 768px) {
  .catalog-sidebar {
    width: 100%;
    float: none;
    position: static;
    max-height: none;
    margin-bottom: 20px;
  }
  
  .catalog-content {
    width: 100%;
    margin-left: 0;
    padding: 20px 0;
    float: none;
  }
}
</style>