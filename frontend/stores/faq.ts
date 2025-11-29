import type { IFaqItem, IFaqResponse } from "~/types";

import { api } from "~/api";
import { defineStore } from "pinia";

export const useFaqStore = defineStore("faq", () => {
  const faqList = ref<IFaqItem[]>([]);
  const error = ref<string | null>(null);
  const loading = ref(false);

  const current = ref<number>(1);
  const next = ref<number | null>(null);
  const previous = ref<number | null>(null);
  const count = ref<number>(0);
  const total_pages = ref<number>(0);

  async function fetchAllFaqList(page: number = 1, page_size: number = 9) {
    const { $api } = useNuxtApp();
    try {
      const res = await $api<IFaqResponse>(api.contacts.faq, {
        query: {
          page,
          page_size,
        },
      });

      if (res.results) {
        if (page > 1) {
          faqList.value = [...faqList.value, ...res.results];
        } else {
          faqList.value = res.results;
        }
      }

      current.value = page;
      count.value = res.count ?? 0;
      next.value = res.next;
      previous.value = res.previous;

      return res;
    } catch (e: Error) {
      error.value = e.message || "Something went wrong";
      throw e;
    }
  }

  return {
    faqList,
    error,
    loading,
    current,
    next,
    previous,
    count,
    total_pages,
    fetchAllFaqList,
  };
});
