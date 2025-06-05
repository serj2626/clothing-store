<script setup lang="ts">
interface Product {
  title: string;
  price: string;
  sizes: string;
  colors: string;
  image?: string;
}

const products: Product[] = [
  {
    title: "Белая куртка",
    price: "2900 грн",
    sizes: "XS, S, M",
    colors: "Белый, Чёрный",
    image: "favorites/one.png",
  },
  {
    title: "Кожаная куртка",
    price: "3700 грн",
    sizes: "S, M",
    colors: "Чёрный",
    image: "favorites/two.png",
  },
  {
    title: "Пальто оверсайз",
    price: "4500 грн",
    sizes: "M, L",
    colors: "Бежевый",
    image: "favorites/three.png",
  },
  {
    title: "Пуховик длинный",
    price: "5200 грн",
    sizes: "S, M, L",
    colors: "Белый, Серый",
    image: "favorites/one.png",
  },
  {
    title: "Жилет женский",
    price: "3100 грн",
    sizes: "XS, S",
    colors: "Оливковый",
    image: "favorites/two.png",
  },
  {
    title: "Плащ тренч",
    price: "4100 грн",
    sizes: "S, M, L",
    colors: "Бежевый, Серый",
    image: "favorites/three.png",
  },
  {
    title: "Костюм двойка",
    price: "4800 грн",
    sizes: "S, M",
    colors: "Синий, Чёрный",
    image: "favorites/one.png",
  },
  {
    title: "Платье миди",
    price: "2700 грн",
    sizes: "XS, S, M",
    colors: "Розовый, Бежевый",
    image: "favorites/two.png",
  },
  {
    title: "Футболка базовая",
    price: "900 грн",
    sizes: "XS, S, M, L",
    colors: "Белый, Чёрный",
    image: "favorites/three.png",
  },
  {
    title: "Жакет твидовый",
    price: "3900 грн",
    sizes: "M, L",
    colors: "Серый, Голубой",
    image: "favorites/one.png",
  },
  {
    title: "Топ с вырезом",
    price: "1200 грн",
    sizes: "XS, S",
    colors: "Чёрный, Красный",
    image: "favorites/two.png",
  },
  {
    title: "Пальто оверсайз",
    price: "4500 грн",
    sizes: "M, L",
    colors: "Бежевый",
    image: "favorites/three.png",
  },
];
</script>
<template>
  <div class="catalog-list">
    <ProductsCard
      v-for="(product, index) in products"
      :key="index"
      :title="product.title"
      :price="product.price"
      :sizes="product.sizes"
      :colors="product.colors"
      :image="product.image"
    />
  </div>
</template>
<style scoped lang="scss">
.catalog-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}
</style>
