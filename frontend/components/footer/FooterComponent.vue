<script lang="ts" setup>
import { footerLinks } from "~/assets/data/footer.data";
</script>
<template>
  <footer class="footer-component">
    <div class="container">
      <div class="footer-component__content">
        <div class="footer-component__content-list">
          <div
            v-for="(item, index) in footerLinks"
            :key="index"
            class="footer-component__content-list-item"
          >
            <p class="footer-component__content-list-item-link">
              {{ item.label }}
            </p>
            <ul class="footer-component__content-list-item-children">
              <NuxtLink
                v-for="child in item.children"
                :key="child.label"
                :to="child.link"
                class="footer-component__content-list-item-children-link"
              >
                {{ child.label }}
              </NuxtLink>
            </ul>
          </div>
        </div>
      </div>
      <p class="footer-component__copyright">Copyright © 2023. All rights reserved</p>
    </div>
  </footer>
</template>
<style lang="scss">
.footer-component {
  &__content {
    padding-bottom: 55px;
    &-list {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;

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
              color: teal;
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
  &__copyright {
    font-weight: 200;
    color: $black;
    opacity: 0.8;
    text-align: center;
    padding-bottom: 10px;
  }
}
</style>
