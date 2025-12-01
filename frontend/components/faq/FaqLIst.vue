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

// const activeIndexList = ref<number[]>([]);

const toogle = (index: number) => {
  if (activeFaqIndex.value === index) {
    activeFaqIndex.value = null;
  } else {
    activeFaqIndex.value = index;
  }
};

// const addActiveIndex = (index: number) => {
//   if (!activeIndexList.value.includes(index)) {
//     activeIndexList.value.push(index);
//   } else {
//     activeIndexList.value = activeIndexList.value.filter(
//       (item) => item !== index
//     );
//   }
// };

// const indexInList = (index: number) => {
//   return activeIndexList.value.includes(index);
// }
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
  </ul>
  <button
    v-if="isNext"
    class="faq-list__btn"
    :disabled="!isNext"
    @click="loadMore"
  >
    {{ isNext ? "Загрузить еще..." : "Данные закончились" }}
  </button>
</template>
<style scoped lang="scss">
.faq-list {
  column-count: 2;
  column-gap: 20px;
  list-style: none;
  padding: 0;
  margin: 0;

  &__item {
    display: inline-block;
    width: 100%;
    margin-bottom: 20px; 
    break-inside: avoid; 
    border-radius: 3px;
    background-color: #e0bea22d;
    padding: 10px;
    position: relative;
    overflow: hidden;

    &::before {
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 3px;
      background: $accent-dark;
      transform: scaleY(0);
      transition: transform 0.3s ease;
    }

    &--active::before {
      transform: scaleY(1);
    }
  }

  &__item-header {
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

  &__btn {
    display: block;
    margin: 40px auto 0;
    max-width: 45%;
    width: 100%;
    padding: 16px;
    background: $accent;
    color: #fff;
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
}

// Адаптив
@media (max-width: 768px) {
  .faq-list {
    column-count: 1;
    column-gap: 0;
  }
}
</style>
