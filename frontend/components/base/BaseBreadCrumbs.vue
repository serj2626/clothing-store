<script lang="ts" setup>
interface ILink {
  title: string;
  url: string;
}

defineProps<{
  breadcrumbs?: ILink[];
}>();
</script>
<template>
  <div class="base-bread">
      <ul class="base-bread__links">
        <NuxtLink class="base-bread__links-back" to="/">Назад</NuxtLink>
        <NuxtLink
          v-for="(link, indx) in breadcrumbs"
          :key="indx"
          :to="link.url"
          class="base-bread__links-item"
        >
          {{ link.title }}
        </NuxtLink>
      </ul>
  </div>
</template>
<style scoped lang="scss">
.base-bread {
  padding-top: 50px;
  &__links {
    display: none;
    gap: 10px;
    align-items: center;
    position: relative;
    @include mediaMobile {
      display: flex;
    }
    &::after {
      content: "";
      position: absolute;
      bottom: -10px;
      left: 0;
      width: 100%;
      height: 1px;
      background-color: #ffffff81;
    }
    &-item {
      cursor: pointer;
      color: $white;
      display: inline-block;
      &:not(:last-child)::after {
        content: "/";
        padding: 0 5px;
      }

      &:last-child {
        pointer-events: none;
        color: $accent;
        opacity: 0.8;
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