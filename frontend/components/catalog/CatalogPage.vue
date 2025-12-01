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
  display: grid;
  grid-template-columns: 320px 1fr; // sidebar + основной контент
  gap: 20px;
  margin-top: 20px;
  margin-bottom: 100px;
  height: 100%; // чтобы sidebar мог скроллиться
}

.catalog-sidebar {
  grid-column: 1;
  overflow-y: auto; // вертикальный скролл, если контента много
  max-height: 100vh; // ограничение высоты, чтобы скролл работал
  padding: 20px;
  padding-left: 0;
}

.catalog-content {
  grid-column: 2;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

// Если нужно, чтобы после sidebar текст/контент занимал всю ширину:
.catalog-content-fullwidth {
  grid-column: 1 / -1; // растягиваем на все колонки
}
</style>