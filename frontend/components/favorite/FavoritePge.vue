<!-- <script setup lang="ts">
import { favoritePageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
import { products } from "~/assets/data/products.data";
</script>
<template>
  <div class="favorite-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="favoritePageBreadcrumbs" />
      <div class="favorite-page__content">
        
        <!-- <h2 class="favorite-page__content-title">Избранное</h2>
        <div class="favorite-page__content-list">
          <ProductCard
            v-for="product in products"
            :id="product.id"
            :key="product.id"
            :title="product.title"
            :price="product.price"
            :sizes="product.sizes"
            :colors="product.colors"
            :image="product.image"
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
</style> -->

<script lang="ts" setup>
import { favoritePageBreadcrumbs } from "~/assets/data/breadcrumbs.data";

// Моковые данные в стиле Ozon
const favorites = ref([
  {
    id: 1,
    slug: "smartphone-x3",
    title: "Смартфон X3 Pro 128GB Черный",
    currentPrice: 34990,
    oldPrice: 39990,
    discount: 13,
    image: "./favorites/one.png",
    rating: 4,
    reviews: 125,
    inStock: true,
  },
  {
    id: 2,
    slug: "wireless-headphones",
    title: "Беспроводные наушники SoundPro",
    currentPrice: 5990,
    image: "./favorites/two.png",
    rating: 5,
    reviews: 87,
    inStock: true,
  },
  {
    id: 3,
    slug: "coffee-machine",
    title: "Кофемашина HomeBarista 500",
    currentPrice: 28990,
    oldPrice: 32990,
    discount: 12,
    image: "./favorites/one.png",
    rating: 3,
    reviews: 42,
    inStock: false,
  },
  {
    id: 4,
    slug: "fitness-tracker",
    title: "Фитнес-браслет FitBand 4",
    currentPrice: 3990,
    image: "./favorites/three.png",
    rating: 4,
    reviews: 215,
    inStock: true,
  },
]);

const removeFromFavorites = (id: number) => {
  favorites.value = favorites.value.filter((item) => item.id !== id);
};

const clearFavorites = () => {
  favorites.value = [];
};

const addToCart = (item: any) => {
  console.log("Added to cart:", item);
};

const navigateToCatalog = () => {
  navigateTo("/catalog");
};
</script>

<template>
  <div class="favorites-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="favoritePageBreadcrumbs" style="margin-bottom: 50px;" />

      <!-- Заголовок с количеством -->
      <div class="favorites-header">
        <h1 class="favorites-title">Избранное</h1>
        <span class="favorites-count">{{ favorites.length }} товаров</span>
      </div>

      <!-- Фильтры и сортировка -->
      <div class="favorites-controls">
        <div class="favorites-filter">
          <button class="filter-btn active">Все товары</button>
          <button class="filter-btn">Товары со скидкой</button>
          <button class="filter-btn">Доступные к заказу</button>
        </div>
        <div class="favorites-sort">
          <span class="sort-label">Сортировка:</span>
          <select class="sort-select">
            <option>По популярности</option>
            <option>По цене ↑</option>
            <option>По цене ↓</option>
            <option>По новизне</option>
          </select>
        </div>
      </div>

      <!-- Состояние пустого избранного -->
      <div v-if="!favorites.length" class="favorites-empty">
        <svg
          class="favorites-empty-icon"
          width="80"
          height="80"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12 21.35L10.55 20.03C5.4 15.36 2 12.28 2 8.5C2 5.42 4.42 3 7.5 3C9.24 3 10.91 3.81 12 5.09C13.09 3.81 14.76 3 16.5 3C19.58 3 22 5.42 22 8.5C22 12.28 18.6 15.36 13.45 20.03L12 21.35Z"
            fill="#E0BEA2"
          />
        </svg>
        <h2 class="favorites-empty-title">В избранном пока ничего нет</h2>
        <p class="favorites-empty-text">
          Нажимайте ♡ на карточках товаров — и они появятся здесь
        </p>
        <button class="favorites-empty-btn" @click="navigateToCatalog">
          В каталог
        </button>
      </div>

      <!-- Список избранных товаров -->
      <div v-else class="favorites-grid">
        <div v-for="item in favorites" :key="item.id" class="favorites-item">
          <div class="item-badge" v-if="item.discount">
            -{{ item.discount }}%
          </div>
          <button
            class="favorites-item-remove"
            @click="removeFromFavorites(item.id)"
          >
            <svg
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41Z"
                fill="#252525"
              />
            </svg>
          </button>
          <NuxtLink :to="`/product/${item.slug}`" class="favorites-item-link">
            <div class="favorites-item-image">
              <img :src="item.image" :alt="item.title" loading="lazy" />
            </div>
            <div class="favorites-item-info">
              <h3 class="favorites-item-title">{{ item.title }}</h3>
              <div class="price-container">
                <span class="current-price">{{ item.currentPrice }} ₽</span>
                <span class="old-price" v-if="item.oldPrice"
                  >{{ item.oldPrice }} ₽</span
                >
              </div>
              <div class="item-rating">
                <div class="stars">
                  <span
                    v-for="i in 5"
                    :key="i"
                    :class="['star', { active: i <= item.rating }]"
                    >★</span
                  >
                </div>
                <span class="reviews">({{ item.reviews }})</span>
              </div>
              <button class="add-to-cart-btn" @click.prevent="addToCart(item)">
                В корзину
              </button>
            </div>
          </NuxtLink>
        </div>
      </div>

      <!-- Кнопки управления -->
      <div class="favorites-actions" v-if="favorites.length">
        <button class="clear-favorites-btn" @click="clearFavorites">
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41Z"
              fill="currentColor"
            />
          </svg>
          Очистить избранное
        </button>
        <button class="select-all-btn">
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M10 17L5 12L6.41 10.59L10 14.17L17.59 6.58L19 8L10 17Z"
              fill="currentColor"
            />
          </svg>
          Выбрать все
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.favorites-page {
  padding: 20px 0 40px;

  @media (min-width: $tablet) {
    padding: 30px 0 60px;
  }
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

.favorites-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.favorites-title {
  font-family: $ff_title;
  font-size: 28px;
  font-weight: 700;
  color: $txt;
  margin: 0;

  @media (min-width: $tablet) {
    font-size: 32px;
  }
}

.favorites-count {
  font-family: $ff_second;
  font-size: 14px;
  color: lighten($txt, 30%);
  margin-left: 15px;
  padding-top: 5px;
}

.favorites-controls {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 1px solid lighten($txt, 80%);

  @media (min-width: $tablet) {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}

.favorites-filter {
  display: flex;
  gap: 10px;
  overflow-x: auto;
  padding-bottom: 5px;

  @media (min-width: $tablet) {
    gap: 15px;
  }
}

.filter-btn {
  font-family: $ff_second;
  font-size: 14px;
  color: $txt;
  background: none;
  border: 1px solid lighten($txt, 70%);
  border-radius: 20px;
  padding: 8px 15px;
  white-space: nowrap;
  cursor: pointer;
  transition: $default_transition;

  &.active {
    background-color: $accent;
    color: $white;
    border-color: $accent;
  }

  &:hover {
    border-color: $accent;
  }
}

.favorites-sort {
  display: flex;
  align-items: center;
  gap: 10px;
}

.sort-label {
  font-family: $ff_second;
  font-size: 14px;
  color: lighten($txt, 30%);
}

.sort-select {
  font-family: $ff_second;
  font-size: 14px;
  color: $txt;
  border: 1px solid lighten($txt, 70%);
  border-radius: 4px;
  padding: 8px 12px;
  background-color: $white;
  cursor: pointer;
}

.favorites-empty {
  text-align: center;
  padding: 60px 20px;
  background-color: $white;
  border-radius: $btn_radius;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  margin-top: 30px;
}

.favorites-empty-icon {
  margin-bottom: 20px;
}

.favorites-empty-title {
  font-family: $ff_title;
  font-size: 22px;
  color: $txt;
  margin-bottom: 10px;

  @media (min-width: $tablet) {
    font-size: 24px;
  }
}

.favorites-empty-text {
  font-family: $ff_second;
  font-size: 16px;
  color: lighten($txt, 30%);
  margin-bottom: 30px;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
}

.favorites-empty-btn {
  display: inline-block;
  padding: 12px 30px;
  background-color: $accent;
  color: $white;
  font-family: $ff_second;
  font-weight: 500;
  border-radius: $btn_radius;
  transition: $default_transition;
  border: none;
  cursor: pointer;

  &:hover {
    background-color: $accent-dark;
    box-shadow: $btn-accent-hover-shadow;
  }
}

.favorites-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;

  @media (min-width: $tablet) {
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }

  @media (min-width: $laptop) {
    grid-template-columns: repeat(4, 1fr);
    gap: 25px;
  }
}

.favorites-item {
  position: relative;
  background-color: $white;
  border-radius: $btn_radius;
  overflow: hidden;
  transition: $default_transition;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  }
}

.item-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  background-color: $error;
  color: $white;
  font-family: $ff_second;
  font-size: 12px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 12px;
  z-index: 2;
}

.favorites-item-remove {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 30px;
  height: 30px;
  background-color: rgba($white, 0.8);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
  transition: $default_transition;
  border: none;
  cursor: pointer;

  &:hover {
    background-color: $white;
  }
}

.favorites-item-link {
  display: block;
  text-decoration: none;
  color: inherit;
}

.favorites-item-image {
  position: relative;
  padding-top: 100%;
  overflow: hidden;

  img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
    padding: 15px;
    transition: $default_transition;
  }
}

.favorites-item-info {
  padding: 15px;
  border-top: 1px solid lighten($txt, 85%);
}

.favorites-item-title {
  font-family: $ff_second;
  font-size: 14px;
  font-weight: 400;
  color: $txt;
  margin-bottom: 12px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  min-height: 40px;

  @media (min-width: $tablet) {
    font-size: 15px;
  }
}

.price-container {
  margin-bottom: 10px;
}

.current-price {
  font-family: $ff_second;
  font-size: 18px;
  font-weight: 700;
  color: $txt;
  margin-right: 8px;

  @media (min-width: $tablet) {
    font-size: 20px;
  }
}

.old-price {
  font-family: $ff_second;
  font-size: 14px;
  color: lighten($txt, 50%);
  text-decoration: line-through;
}

.item-rating {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 15px;
}

.stars {
  display: flex;
}

.star {
  font-size: 14px;
  color: lighten($txt, 70%);

  &.active {
    color: #ffb800;
  }
}

.reviews {
  font-family: $ff_second;
  font-size: 12px;
  color: lighten($txt, 40%);
}

.add-to-cart-btn {
  width: 100%;
  padding: 10px;
  background-color: $accent;
  color: $white;
  font-family: $ff_second;
  font-size: 14px;
  font-weight: 500;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: $default_transition;

  &:hover {
    background-color: $accent-dark;
  }
}

.favorites-actions {
  display: flex;
  gap: 15px;
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid lighten($txt, 80%);
}

.clear-favorites-btn,
.select-all-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: $ff_second;
  font-size: 14px;
  color: $txt;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px 12px;
  transition: $default_transition;

  &:hover {
    color: $accent;
  }
}
</style>
