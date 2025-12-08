<script setup lang="ts">
import type { ICategoryResponse } from "./HomePage.vue";

defineProps<{ list: ICategoryResponse[] }>();
</script>

<template>
  <section class="home-section-categories">
    <div class="container">
      <h2 class="home-section-categories__title">Наши категории</h2>
      <ul class="home-section-categories__list">
        <li
          v-for="item in list"
          :key="item.slug"
          class="home-section-categories__list-item"
        >
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
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped lang="scss">
.home-section-categories {
  position: relative;
  overflow: hidden;

  &__list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
    margin-bottom: 50px;
    @include mediaMobile {
      grid-template-columns: repeat(2, 1fr);
    }
    @include mediaTablet {
      grid-template-columns: repeat(3, 1fr);
    }
    @include mediaLaptop {
      grid-template-columns: repeat(4, 1fr);
    }
  }

  &__title {
    margin-block: 100px 50px;
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
}
</style>
