<script setup lang="ts">
import { ref } from "vue";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Thumbs, Zoom } from "swiper/modules";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/thumbs";
import "swiper/css/zoom";

// Для теста используем базовые URL изображений
const placeholderImage =
  "https://via.placeholder.com/800x800/f5f5dc/000000?text=Product+Image";

const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Каталог", url: "/catalog" },
  { title: "Товар", url: "/" },
  { title: "Кремовое пальто", url: "/" },
];

const thumbsSwiper = ref<any>(null);
const activeColor = ref("#f5f5dc"); // Используем hex-код вместо строки
const activeSize = ref("M");

const product = {
  title: "Кремовое пальто",
  price: 12990,
  oldPrice: 15990,
  colors: ["#f5f5dc", "#000000", "#a52a2a", "#0000ff"],
  sizes: ["XS", "S", "M", "L", "XL"],
  description:
    "Элегантное кремовое пальто из шерсти с кашемиром. Классический крой, отложной воротник, длинные рукава. Подходит для любого сезона.",
  details: [
    { title: "Состав", value: "Шерсть 80%, кашемир 20%" },
    { title: "Уход", value: "Химчистка" },
    { title: "Сезон", value: "Демисезон" },
    { title: "Страна", value: "Италия" },
  ],
};

const galleryImages = [
  { id: 1, src: placeholderImage, alt: "Кремовое пальто - вид спереди" },
  { id: 2, src: placeholderImage, alt: "Кремовое пальто - вид сбоку" },
  { id: 3, src: placeholderImage, alt: "Кремовое пальто - детали" },
  { id: 4, src: placeholderImage, alt: "Кремовое пальто - на модели" },
];

const setThumbsSwiper = (swiper: any) => {
  thumbsSwiper.value = swiper;
};
</script>

<template>
  <div class="product-page">
    <div class="container">

      <div class="product-page__content">
        <!-- Галерея изображений -->
        <div class="product-gallery">
          <div class="product-gallery__main">
            <Swiper
              :modules="[Navigation, Thumbs, Zoom]"
              :thumbs="{ swiper: thumbsSwiper }"
              navigation
              zoom
              class="product-gallery__swiper"
            >
              <SwiperSlide v-for="image in galleryImages" :key="image.id">
                <div class="swiper-zoom-container">
                  <img
                    :src="image.src"
                    :alt="image.alt"
                    class="product-gallery__image"
                  />
                </div>
              </SwiperSlide>
            </Swiper>
          </div>

          <div class="product-gallery__thumbs">
            <Swiper
              @swiper="setThumbsSwiper"
              :modules="[Thumbs]"
              :spaceBetween="10"
              :slidesPerView="4"
              :freeMode="true"
              :watchSlidesProgress="true"
              class="product-gallery__thumbs-swiper"
            >
              <SwiperSlide v-for="image in galleryImages" :key="image.id">
                <img
                  :src="image.src"
                  :alt="image.alt"
                  class="product-gallery__thumb"
                />
              </SwiperSlide>
            </Swiper>
          </div>
        </div>

        <!-- Информация о товаре -->
        <div class="product-info">
          <h1 class="product-info__title">{{ product.title }}</h1>

          <div class="product-info__price">
            <span class="product-info__current-price">
              {{ product.price.toLocaleString() }} ₽
            </span>
            <span v-if="product.oldPrice" class="product-info__old-price">
              {{ product.oldPrice.toLocaleString() }} ₽
            </span>
          </div>

          <div class="product-info__section">
            <h3 class="product-info__section-title">Цвет</h3>
            <div class="product-info__colors">
              <button
                v-for="(color, index) in product.colors"
                :key="index"
                class="product-info__color"
                :class="{
                  'product-info__color--active': activeColor === color,
                }"
                :style="{ backgroundColor: color }"
                @click="activeColor = color"
                :aria-label="`Цвет ${index + 1}`"
              />
            </div>
          </div>

          <div class="product-info__section">
            <h3 class="product-info__section-title">Размер</h3>
            <div class="product-info__sizes">
              <button
                v-for="size in product.sizes"
                :key="size"
                class="product-info__size"
                :class="{ 'product-info__size--active': activeSize === size }"
                @click="activeSize = size"
              >
                {{ size }}
              </button>
            </div>
            <a href="#" class="product-info__size-guide">Таблица размеров</a>
          </div>

          <button class="product-info__add-to-cart">Добавить в корзину</button>

          <div class="product-info__description">
            <h3 class="product-info__section-title">Описание</h3>
            <p>{{ product.description }}</p>
          </div>

          <div class="product-info__details">
            <h3 class="product-info__section-title">Детали</h3>
            <ul class="product-info__details-list">
              <li
                v-for="(detail, index) in product.details"
                :key="index"
                class="product-info__details-item"
              >
                <span class="product-info__detail-title"
                  >{{ detail.title }}:</span
                >
                <span class="product-info__detail-value">{{
                  detail.value
                }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Базовые стили */
.product-page {
  padding: 30px 0 60px;
  font-family: Arial, sans-serif;
  color: #333;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

/* Хлебные крошки */
.product-page__breadcrumbs {
  margin-bottom: 30px;
  display: flex;
  gap: 8px;
}

.breadcrumb-item {
  color: #666;
  text-decoration: none;
}

.breadcrumb-item:hover {
  text-decoration: underline;
}

/* Основной контент */
.product-page__content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

/* Галерея */
.product-gallery__main {
  margin-bottom: 16px;
  border-radius: 8px;
  overflow: hidden;
  height: 500px;
  background: #f8f8f8;
}

.product-gallery__swiper {
  height: 100%;
}

.product-gallery__image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.product-gallery__thumbs {
  padding: 0 20px;
}

.product-gallery__thumbs-swiper {
  padding: 10px 0;
}

.product-gallery__thumb {
  width: 100%;
  height: 80px;
  object-fit: cover;
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.2s ease;
}

.product-gallery__thumb:hover {
  border-color: #007bff;
}

.swiper-slide-thumb-active .product-gallery__thumb {
  border-color: #007bff;
}

/* Информация о товаре */
.product-info__title {
  font-size: 28px;
  margin: 0 0 16px;
}

.product-info__price {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.product-info__current-price {
  font-size: 24px;
  font-weight: bold;
  color: #007bff;
}

.product-info__old-price {
  font-size: 18px;
  color: #999;
  text-decoration: line-through;
}

.product-info__section {
  margin-bottom: 24px;
  padding-bottom: 24px;
  border-bottom: 1px solid #eee;
}

.product-info__section:last-child {
  border-bottom: none;
}

.product-info__section-title {
  font-size: 16px;
  font-weight: bold;
  margin: 0 0 16px;
}

.product-info__colors {
  display: flex;
  gap: 12px;
}

.product-info__color {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid transparent;
  cursor: pointer;
  position: relative;
  padding: 0;
}

.product-info__color--active {
  border-color: #007bff;
}

.product-info__color--active::after {
  content: "";
  position: absolute;
  top: -4px;
  left: -4px;
  right: -4px;
  bottom: -4px;
  border: 1px solid #007bff;
  border-radius: 50%;
}

.product-info__sizes {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 12px;
}

.product-info__size {
  min-width: 40px;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: none;
  cursor: pointer;
}

.product-info__size--active {
  background: #007bff;
  color: white;
  border-color: #007bff;
}

.product-info__size-guide {
  color: #007bff;
  text-decoration: none;
  font-size: 14px;
}

.product-info__size-guide:hover {
  text-decoration: underline;
}

.product-info__add-to-cart {
  width: 100%;
  padding: 16px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  margin: 24px 0;
  transition: background 0.2s;
}

.product-info__add-to-cart:hover {
  background: #0069d9;
}

.product-info__description p {
  margin: 0;
  line-height: 1.6;
}

.product-info__details-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.product-info__details-item {
  display: flex;
  margin-bottom: 8px;
}

.product-info__detail-title {
  font-weight: bold;
  min-width: 80px;
}

/* Адаптив */
@media (max-width: 768px) {
  .product-page__content {
    grid-template-columns: 1fr;
    gap: 30px;
  }

  .product-gallery {
    order: -1;
  }

  .product-gallery__main {
    height: 400px;
  }
}
</style>
