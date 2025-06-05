<script setup lang="ts">
const categories = [
  { title: "Каталог", slug: "catalog" },
  { title: "New", slug: "new" },
  { title: "Bestsellers", slug: "bestsellers" },
  { title: "Верхняя одежда", slug: "outerwear" },
  { title: "Шубы", slug: "fur-coats" },
  { title: "Тренчи", slug: "trench-coats" },
  { title: "Пальто", slug: "coats" },
  { title: "Пуховики и жилеты", slug: "down-jackets" },
  { title: "Костюмы", slug: "suits" },
  { title: "Жакеты", slug: "jackets" },
  { title: "Платья", slug: "dresses" },
  { title: "Рубашки и блузы", slug: "shirts-blouses" },
  { title: "Юбки", slug: "skirts" },
  { title: "Футболки и топы", slug: "tshirts-tops" },
  { title: "Аксессуары", slug: "accessories" },
  { title: "Sale", slug: "sale" },
  { title: "Summer", slug: "summer" },
  { title: "Посмотреть всё", slug: "all" },
];
</script>
<template>
  <div class="catalog-categories">
    <p class="catalog-categories__title">Категории</p>
    <ul class="catalog-categories__list">
      <NuxtLink
        v-for="category in categories"
        :key="category.slug"
        class="catalog-categories__list-item"
      >
        {{ category.title }}
      </NuxtLink>
    </ul>
  </div>
</template>
<style scoped lang="scss">
.catalog-categories {
  position: sticky;
  top: 60px;
  align-self: flex-start;

  &__title {
    font-size: 20px;
    margin-bottom: 30px;
  }
  &__list {
    display: flex;
    flex-direction: column;
    gap: 20px;

    &-item {
      color: $txt;
      cursor: pointer;
      position: relative;

      &::after {
        content: "";
        display: inline;
        height: 1px;
        width: 0;
        background-color: $txt;
        transition: width 0.3s ease;
        margin-top: 2px;
      }

      &:hover::after {
        width: max-content;
      }
    }
  }
}
</style>
