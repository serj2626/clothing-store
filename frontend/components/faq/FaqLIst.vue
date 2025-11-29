<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IFaqItem } from "~/types/contacts/faq";

const { faqData, isNext = false } = defineProps<{
  faqData: IFaqItem[];
  isNext?: boolean;
}>();

const emit = defineEmits<{
  (e: "loadMore"): void;
}>();

const loadMore = () => {
  if (isNext) {
    emit("loadMore");
  }
};
const activeFaqIndex = ref<number | null>(null);

const toogle = (index: number) => {
  if (activeFaqIndex.value === index) {
    activeFaqIndex.value = null;
  } else {
    activeFaqIndex.value = index;
  }
};
</script>
<template>
  <ul class="faq-list">
    <li v-for="value in faqData" :key="value.id" class="faq-list__item">
      <BaseAccordion
        :is-open="activeFaqIndex === value.id"
        @update:is-open="toogle(value.id)"
      >
        <template #summary>
          <div class="faq-list__item-header">
            {{ value.question }}
            <Icon
              :name="HeroIcons.DOWN"
              class="faq-list__item-header-icon"
              :class="{
                'faq-list__item-header-icon--active':
                  activeFaqIndex === value.id,
              }"
            />
          </div>
        </template>
        <template #content> {{ value.answer }}</template>
      </BaseAccordion>
    </li>
    <button :disabled="!isNext" @click="loadMore">Загрузить еще...</button>
  </ul>
</template>
<style scoped lang="scss">
.faq-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.faq-list__item {
  border-radius: 5px;
}
.faq-list__item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 26px;
  cursor: pointer;
  font-weight: 500;

  &-icon {
    transition: rotate 0.3s ease-in-out;
    &--active {
      rotate: 180deg;
    }
  }
}
button {
  padding: 10px 20px;
  background: $accent;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;

  &:disabled {
    background: #ccc;
    color: #666;
    cursor: not-allowed;
    opacity: 0.6;
  }

  &:not(:disabled):hover {
    background: darken($accent, 10%);
  }
}
</style>
