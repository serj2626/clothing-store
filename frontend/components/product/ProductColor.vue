<script setup lang="ts">
const { color = "#fff", size = "16px" } = defineProps<{
  color?: string;
  size?: string;
}>();
</script>
<template>
  <div
    class="products-color"
    :class="{ 'products-color_shadow': color === '#fff' || color === 'white' }"
  ></div>
</template>
<style scoped lang="scss">
.products-color {
  width: v-bind(size);
  aspect-ratio: 1/1;
  background-color: v-bind(color);
  border-radius: 50%;
  outline: 1px solid $white;
  outline-offset: -5px;
  cursor: pointer;

  &_shadow {
    box-shadow: 0 0 2px rgb(0, 0, 0);
  }
}
</style>
