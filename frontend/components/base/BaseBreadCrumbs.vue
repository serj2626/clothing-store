<script setup lang="ts">
const {
  breadcrumbs = [],
  currentPage,
  color = '#000',
} = defineProps<{
  breadcrumbs?: { title: string; path: string }[];
  currentPage?: string;
  color?: string;
}>();
</script>
<template>
  <nav class="base-breadcrumbs">
    <ul class="base-breadcrumbs__list">
      <li class="base-breadcrumbs__list-back">
        <NuxtLink class="base-breadcrumbs__list-item-link" to="/">
          <span>Назад</span>
        </NuxtLink>
      </li>
      <li class="base-breadcrumbs__list-item">
        <NuxtLink class="base-breadcrumbs__list-item-link" to="/">
          Главная
        </NuxtLink>
      </li>
      <li
        class="base-breadcrumbs__list-item"
        v-for="breadcrumb in breadcrumbs"
        :key="breadcrumb.title + breadcrumb.path"
      >
        <NuxtLink
          class="base-breadcrumbs__list-item-link"
          :to="breadcrumb.path"
        >
          {{ breadcrumb.title }}
        </NuxtLink>
      </li>
      <li
        v-if="currentPage"
        class="base-breadcrumbs__list-item base-breadcrumbs__list-item_current"
      >
        {{ currentPage }}
      </li>
    </ul>
  </nav>
</template>

<style lang="scss" scoped>
.base-breadcrumbs {
  padding-block: 15px;
  border-bottom: 1px solid #c2babaab;
  &__list {
    display: flex;
    align-items: center;
    color: $txt;

    &-back {
      display: flex;
      align-items: center;
      width: 74px;
      height: 17px;

      @include mediaMobile {
        display: none;
      }
    }

    &-item {
      display: none;

      &-link {
        display: flex;
        gap: 5px;
        color: $teal;

        &-icon {
          display: flex;
        }
      }

      @include mediaMobile {
        display: flex;
      }

      &_current {
        opacity: 0.7;
      }
    }

    &-item:last-child {
      color: v-bind(color);
    }

    &-item:not(:last-child)::after {
      content: '/';
      padding: 0 5px;
      color: v-bind(color);
      opacity: 0.7;
    }
  }
}
</style>
