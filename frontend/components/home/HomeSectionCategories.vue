<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Autoplay, Navigation, Pagination } from "swiper/modules";
import type { ICategoryResponse } from "./HomePage.vue";

// Import Swiper styles
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";

defineProps<{ list: ICategoryResponse[] }>();

const modules = [Autoplay, Navigation, Pagination];
</script>

<template>
  <section class="home-section-categories">
    <div class="container">
      <h2 class="home-section-categories__title">Наши категории</h2>

      <div class="swiper-wrapper">
        <Swiper
          :modules="modules"
          :slides-per-view="1.2"
          :space-between="20"
          :loop="true"
          :autoplay="{
            delay: 5000,
            disableOnInteraction: false,
          }"
          :navigation="{
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          }"
          :pagination="{
            clickable: true,
            el: '.swiper-pagination',
          }"
          :breakpoints="{
            640: {
              slidesPerView: 2.2,
              spaceBetween: 20,
            },
            1024: {
              slidesPerView: 3,
              spaceBetween: 30,
            },
            1440: {
              slidesPerView: 3,
              spaceBetween: 40,
            },
          }"
          class="categories-swiper"
        >
          <SwiperSlide v-for="item in list" :key="item.slug">
            <div class="home-section-categories__list-item">
              <NuxtImg
                class="home-section-categories__list-item-img"
                :src="getMedia(item.image ?? '')"
                format="webp"
                loading="lazy"
                :alt="item.name"
              />
              <div class="home-section-categories__list-item-overlay">
                <p class="home-section-categories__list-item-value">
                  {{ item.name }}
                </p>
                <NuxtLink :to="`/catalog/${item.slug}`">
                  <button class="home-section-categories__list-item-button">
                    Смотреть коллекцию
                  </button>
                </NuxtLink>
              </div>
            </div>
          </SwiperSlide>

          <div class="swiper-pagination"></div>
          <div class="swiper-button-prev"></div>
          <div class="swiper-button-next"></div>
        </Swiper>
      </div>
    </div>
  </section>
</template>

<style scoped lang="scss">
.home-section-categories {
  position: relative;
  overflow: hidden;

  &__title {
    margin-block: 100px 50px;
    // color: #252525;
    color: var(--color-section-title);
    font-size: 36px;
    font-weight: 300;
    text-align: center;
    letter-spacing: 1px;
    position: relative;

    &::after {
      content: "";
      display: block;
      width: 80px;
      height: 2px;
      background: #e0bea2;
      margin: 20px auto 0;
    }
  }

  .swiper-wrapper {
    position: relative;
    padding-bottom: 60px;
    margin-bottom: 60px;
  }

  .categories-swiper {
    padding: 20px 40px;
    margin: -20px -40px;

    .swiper-slide {
      width: 100%;
      min-width: 300px;
      height: auto;
    }
  }

  &__list-item {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    aspect-ratio: 3/4;
    height: 100%;

    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);

      .home-section-categories__list-item-overlay {
        opacity: 1;
        background: rgba(0, 0, 0, 0.5);
      }

      .home-section-categories__list-item-value {
        transform: translateY(0);
      }

      .home-section-categories__list-item-button {
        transform: translateY(0);
        opacity: 1;
      }
    }

    &-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;

      &:hover {
        transform: scale(1.05);
      }
    }

    &-overlay {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      align-items: center;
      padding: 30px;
      background: linear-gradient(
        to top,
        rgba(0, 0, 0, 0.7) 0%,
        rgba(0, 0, 0, 0) 100%
      );
      opacity: 1;
      transition: all 0.4s ease;
      color: white;
    }

    &-value {
      font-size: 24px;
      font-weight: 500;
      margin-bottom: 15px;
      text-align: center;
      text-transform: uppercase;
      letter-spacing: 1px;
      transform: translateY(20px);
      transition: transform 0.3s ease;
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    }

    &-button {
      padding: 12px 24px;
      background: transparent;
      color: white;
      border: 1px solid white;
      border-radius: 25px;
      font-size: 14px;
      font-weight: 500;
      letter-spacing: 1px;
      cursor: pointer;
      transition: all 0.3s ease;
      transform: translateY(30px);
      opacity: 0;

      &:hover {
        background: white;
        color: #252525;
      }
    }
  }

  // Navigation buttons
  .swiper-button-prev,
  .swiper-button-next {
    color: #e0bea2;
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 50%;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;

    &::after {
      font-size: 20px;
      font-weight: bold;
    }

    &:hover {
      background: #e0bea2;
      color: white;
      transform: scale(1.1);
    }
  }

  .swiper-button-prev {
    left: 0;
  }

  .swiper-button-next {
    right: 0;
  }

  // Pagination
  .swiper-pagination {
    position: absolute;
    bottom: 10px;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 8px;
  }

  .swiper-pagination-bullet {
    background: #d3d3d3;
    opacity: 1;
    width: 12px;
    height: 12px;
    transition: all 0.3s ease;

    &-active {
      background: #e0bea2;
      transform: scale(1.2);
    }
  }
}
</style>
