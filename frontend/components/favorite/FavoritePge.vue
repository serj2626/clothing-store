<script setup lang="ts">
const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Избранное", url: "/favorite" },
];
</script>
<template>
  <div class="favorite-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <div class="favorite-page__content">
        <h2 class="favorite-page__content-title">Избранное</h2>
        <div class="favorite-page__content-list">
          <ProductsCard
            title="Белая куртка"
            price="2900 грн"
            sizes="vsadadad"
            colors="asdsadsad"
          />
          <ProductsCard
            title="Белая куртка"
            price="2900 грн"
            sizes="vsadadad"
            colors="asdsadsad"
          />
          <ProductsCard
            title="Белая куртка"
            price="2900 грн"
            sizes="vsadadad"
            colors="asdsadsad"
          />
          <ProductsCard
            title="Белая куртка"
            price="2900 грн"
            sizes="vsadadad"
            colors="asdsadsad"
          />
          <ProductsCard
            title="Белая куртка"
            price="2900 грн"
            sizes="vsadadad"
            colors="asdsadsad"
          />
          <ProductsCard
            title="Белая куртка"
            price="2900 грн"
            sizes="vsadadad"
            colors="asdsadsad"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.favorite-page {
  &__content {
    &-title {
      font-size: 20px;
      margin-block: 30px;
    }
    &-list {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 15px;
      margin-bottom: 100px;
    }
  }
}
</style>
