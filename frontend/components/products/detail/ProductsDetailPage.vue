<script setup lang="ts">
const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Каталог", url: "/catalog" },
  { title: "Товар", url: "/" },
  { title: "Кремовое пальто", url: "/" },
];
</script>
<template>
  <div class="products-detail-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <div class="products-detail-page__content">
          <ProductsDetailImages />
        <ProductsDetailInfo />
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.products-detail-page {
  &__content {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 50px;
    margin-top: 50px;
  }
}
</style>
