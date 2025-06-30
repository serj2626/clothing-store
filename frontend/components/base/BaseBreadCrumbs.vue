<script lang="ts" setup>
export interface ILink {
  title: string;
  url: string;
}

const props = defineProps<{
  breadcrumbs?: ILink[];
  currentPage?: ILink;
}>();

const breadcrumbsAll = computed(() => {
  const base = props.breadcrumbs ?? [];
  return props.currentPage ? [...base, props.currentPage] : base;
});
</script>
<template>
  <div class="base-bread-crumbs">
    <ul class="base-bread-crumbs__links">
      <NuxtLink class="base-bread-crumbs__links-back" to="/">Назад</NuxtLink>
      <NuxtLink
        v-for="(link, indx) in breadcrumbsAll"
        :key="indx"
        :to="link.url"
        class="base-bread-crumbs__links-item"
      >
        {{ link.title }}
      </NuxtLink>
    </ul>
  </div>
</template>
<style scoped lang="scss">
.base-bread-crumbs {
  margin-top: 100px;
  &__links {
    display: none;
    gap: 10px;
    align-items: center;
    position: relative;
    @include mediaMobile {
      display: flex;
    }

    &-item {
      cursor: pointer;
      color: var(--color-text);
      display: inline-block;
      &:not(:last-child)::after {
        content: ">";
        cursor: none;
        margin-left: 10px;
        color: #dca273;
      }

      &:last-child {
        pointer-events: none;
        color: var(--color-text);
        opacity: 0.7;
        cursor: default;
      }
    }
    &-back {
      color: $white;
      @include mediaMobile {
        display: none;
      }
    }
  }
}
</style>
