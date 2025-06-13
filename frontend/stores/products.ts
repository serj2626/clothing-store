import type { IproductsResponse } from "~/types";
import { api } from "~/api";
import { defineStore } from "pinia";

export const useProductStore = defineStore("product", () => {
  const products = ref([]);
  const error = ref(null);

  const currentPage = ref<number | null>(null);
  const nextPage = ref<number | null>(null);
  const prevPage = ref<number | null>(null);
  const countProducts = ref<number | null>(null);

  
  const fetchAllProducts = async () => {
    const { $api } = useNuxtApp();
    try {
      const { data } = await $fetch<IproductsResponse[]>(api.products.list);
      products.value = data;
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };

  return {
    products,
    fetchAllProducts,
  };
});
