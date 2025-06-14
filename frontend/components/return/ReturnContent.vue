<script setup lang="ts">
import type { IExchangeReturnResponse } from "./ReturnPage.vue";
defineProps<IExchangeReturnResponse>();
</script>
<template>
  <div class="return-content">
    <p class="return-content__title">{{ title }}</p>
    <p class="return-content__text">
      {{ description }}
    </p>
    <p class="return-content__conditions">
      {{ text }}
    </p>
    <div class="return-content__conditions-list">
      <div
        v-for="(condition, index) in terms_processes_items"
        :key="index"
        class="return-content__conditions-list-item"
      >
        <NuxtImg width="30" :src="getMedia(condition.icon)" />

        <p class="return-content__conditions-list-item-text">
          {{ condition.text }}
        </p>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.return-content {
  &__title {
    @include title_page;
  }
  &__text {
    margin-bottom: 10px;
  }
  &__conditions {
    margin-bottom: 20px;

    &-list {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 30px;
      &-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;

        &-text {
          flex: 1;
          text-align: center;
        }
      }
    }
  }
}
</style>
