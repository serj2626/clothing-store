<script setup lang="ts">
const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Корзина", url: "/basket" },
];
</script>
<template>
  <div class="basket-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <BasketContent />
    </div>
  </div>
</template>
<style scoped lang="scss"></style>
