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
    <li
      v-for="value in faqData"
      :key="value.id"
      class="faq-list__item"
      :class="{ 'faq-list__item--active': activeFaqIndex === value.id }"
    >
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
    <button v-if="isNext" :disabled="!isNext" @click="loadMore">
      {{ isNext ? "Загрузить еще..." : "Данные закончились" }}
    </button>
  </ul>
</template>
<style scoped lang="scss">
.faq-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width:70%;
  width: 100%;
  margin-inline: auto;
}
.faq-list__item {
  border-radius: 5px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  position: relative;
  &::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 3px;
    background: $accent-dark;
    transform: scaleY(0.08);
    transition: transform 0.3s ease;
  }

  &--active {
    &::before {
      transform: scaleY(1);
    }
  }
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
    font-size: 22px;
    color: $accent-dark;
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
