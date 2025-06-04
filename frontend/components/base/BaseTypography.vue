<script lang="ts" setup>
interface ITypoghraphy {
  title: string;
  view: "h1" | "h2" | "h3";
}

defineProps<ITypoghraphy>();
</script>
<template>
  <component
    :class="{
      typography_h1: view === 'h1',
      typography_h2: view === 'h2',
      typography_h3: view === 'h3',
    }"
    :is="view"
    >{{ title }}</component
  >
</template>

<style scoped lang="scss">
.typography {
  &_h1 {
    @include txt_title_h1;
  }
  &_h2 {
    @include txt_title_h2;
  }
  &_h3 {
    @include txt_title_h3;
  }
}
</style>
