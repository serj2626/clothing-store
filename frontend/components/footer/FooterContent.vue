<script setup lang="ts">
import type { ILinkGroup } from "./FooterComponent.vue";

defineProps<{ links: ILinkGroup[] }>();
</script>
<template>
  <div class="footer-content">
    <div class="footer-content__list">
      <div
        v-for="(item, index) in links"
        :key="index"
        class="footer-content__list-item"
      >
        <p class="footer-content__list-item-link">
          {{ item.name }}
        </p>
        <ul class="footer-content__list-item-children">
          <NuxtLink
            v-for="child in item.items"
            :key="child.name"
            :to="child.url"
            class="footer-content__list-item-children-link"
          >
            {{ child.name }}
          </NuxtLink>
        </ul>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.footer-content {
  padding-bottom: 55px;
  &__list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;

    &-item {
      display: flex;
      flex-direction: column;
      gap: 20px;

      &-children {
        display: flex;
        flex-direction: column;
        gap: 10px;
        &-link {
          font-size: 16px;
          font-weight: 200;
          color: #252525;
          opacity: 0.8;
          transition: all 0.3s ease-in-out;

          &:hover {
            color: $accent-dark;
          }
        }
      }

      &-link {
        font-size: 20px;
        font-weight: 300;
        color: #252525;
      }
    }
  }
}
</style>
