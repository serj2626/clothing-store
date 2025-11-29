<script setup lang="ts">
import { useFaqStore } from "~/stores/faq";
import type { IFaqResponse } from "~/types";

const faqStore = useFaqStore();
const { faqList, next } = storeToRefs(faqStore);
const { fetchAllFaqList } = faqStore;

await useAsyncData<IFaqResponse>("faq-list-data", () => fetchAllFaqList(1, 6));

const loadMore = () => {
  if (next.value) {
    fetchAllFaqList(next.value as number, 6);
  }
};
</script>
<template>
  <section id="faq" class="container faq-component">
    <div class="faq-component__wrapper">
      <h4 class="faq-component__wrapper-title">Вопросы и ответы</h4>
      <FaqLIst
        v-if="faqList"
        :faq-data="faqList"
        :is-next="next !== null"
        @load-more="loadMore"
      />
    </div>
  </section>
</template>
<style scoped lang="scss">
.faq-component {
}
.faq-component__wrapper {
}
.faq-component__wrapper-title {
  text-align: center;
  color: var(--color-section-title);
  font-size: 36px;
  font-weight: 300;
  margin-bottom: 50px;
}
</style>
