<script setup lang="ts">
defineProps<{ color: string }>();
</script>
<template>
  <div class="products-color"></div>
</template>
<style scoped lang="scss">
.products-color {
  width: 30px;
  aspect-ratio: 1/1;
  background-color: v-bind(color);
  border-radius: 50%;
  outline: 1px solid $white;
  outline-offset: -5px;
  cursor: pointer;
}
</style>
