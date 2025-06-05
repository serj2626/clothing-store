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
  margin-top: 100px;
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
      background-color: #6058583d;
    }
    &-item {
      cursor: pointer;
      color: $txt;
      display: inline-block;
      &:not(:last-child)::after {
        content: ">";
        cursor: none;
        margin-left: 10px;
        color: #dca273;
      }

      &:last-child {
        pointer-events: none;
        color: $txt;
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
