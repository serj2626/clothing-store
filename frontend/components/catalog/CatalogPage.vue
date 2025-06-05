<script setup lang="ts">
const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Каталог", url: "/catalog" },
];
</script>
<template>
  <div class="catalog-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <div class="catalog-page__content">
        <CatalogCategories style="flex: 1" />
        <CatalogContent style="flex: 3" />
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.catalog-page {
  &__content {
    margin-block: 30px 100px;
    display: flex;
    gap: 15px;
  }
}
</style>
