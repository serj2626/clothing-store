<script setup lang="ts">
const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Новинки", url: "/news" },
];
</script>
<template>
  <div class="news-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <div class="news-page__content">
        <h2 class="news-page__content-title">Новые коллекции</h2>
        <div class="news-page__content-list">
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
.news-page {
  &__content {
    &-title {
      @include title_page;
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
