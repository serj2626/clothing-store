import type { IProduct, IproductResponse } from "~/types";

import { api } from "~/api";
import { defineStore } from "pinia";

export const useProductStore = defineStore("product", () => {
  const products = ref<IProduct[]>([]); 
  const error = ref<string | null>(null);

  const currentPage = ref<number>(1); 
  const nextPage = ref<number | null>(null);
  const prevPage = ref<number | null>(null);
  const countProducts = ref<number>(0);

  async function fetchAllProducts(page: number = 1, page_size: number = 10) {
    const { $api } = useNuxtApp();
    try {
      const res = await $api<IproductResponse>(api.products.list, {
        query: {
          page,
          page_size,
        },
      });

      if (res.results) {
        if (page > 1) {
          products.value = [...products.value, ...res.results];
        } else {
          products.value = res.results;
        }
      }

      currentPage.value = page;
      countProducts.value = res.count ?? 0;
      nextPage.value = res.next;
      prevPage.value = res.previous;

      return res;
    } catch (e: Error) {
      error.value = e.message || "Something went wrong";
      throw e; 
    }
  }

  return {
    products,
    currentPage,
    nextPage,
    prevPage,
    countProducts,
    error,
    fetchAllProducts,
  };
});
