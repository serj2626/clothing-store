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
      <div class="contacts-catalog">
        <ul class="contacts-catalog-filters">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Amet,
          aliquam?
        </ul>
        <ul class="contacts-catalog-content">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. In,
          explicabo?
        </ul>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">

.contacts-catalog{
  display: grid;
  grid-template-columns: 1fr 3fr;
  gap: 30px;
}
</style>
