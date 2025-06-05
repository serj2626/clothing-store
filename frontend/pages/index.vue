<script lang="ts" setup>
import { HeroIcons } from "~/assets/icons/types/hero-icons";
</script>
<template>
  <div class="home-page">
    <section class="home-page__hero">
      <div class="home-page__hero-overlay" />
      <div class="home-page__hero-block">
        <h2 class="home-page__hero-block-title">Новая коллекция</h2>
        <div class="home-page__hero-block-separator" />
        <NuxtLink class="home-page__hero-block-link" to="/">
          <p style="display: flex; align-items: center; text-align: center">
            <span>Смотреть Новинки</span>
            <button>
              <Icon :name="HeroIcons.ARROW_RIGHT_SOLID" size="22" />
            </button>
          </p>
        </NuxtLink>
      </div>
    </section>

    <section class="home-page__categories">
      <div class="container">
        <h2 class="home-page__categories-title">Категории</h2>
        <div class="home-page__categories-list">
          <div class="home-page__categories-list-item">
            <img
              class="home-page__categories-list-item-img"
              src="/public/categories/one.png"
              alt=""
            />
            <p class="home-page__categories-list-item-value">Мужская одежда</p>
          </div>
          <div class="home-page__categories-list-item">
            <img
              class="home-page__categories-list-item-img"
              src="/public/categories/two.png"
              alt=""
            />
            <p class="home-page__categories-list-item-value">Женская одежда</p>
          </div>
          <div class="home-page__categories-list-item">
            <img
              class="home-page__categories-list-item-img"
              src="/public/categories/three.png"
              alt=""
            />
            <p class="home-page__categories-list-item-value">Детская одежда</p>
          </div>
        </div>
      </div>
    </section>

    <BaseFormSubscribe />
  </div>
</template>

<style scoped lang="scss">
.home-page {
  &__hero {
    position: relative;
    width: 100%;
    height: 130vh;
    background-image: url("/public/store.jpg");
    background-size: cover;
    background-position: center;
    box-shadow: 0 10px 30px 20px rgba(0, 0, 0, 0.376);

    &-overlay {
      position: absolute;
      z-index: 1;
      width: 100%;
      height: 100%;
      left: 0;
      top: 0;
      background-color: rgba(0, 0, 0, 0.5);
    }
    &-block {
      position: absolute;
      z-index: 2;
      top: 30%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: #fff;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      &-title {
        text-align: center;
        font-size: 46px;
        font-weight: 600;
      }
      &-separator {
        width: 100px;
        height: 2px;
        background-color: #fff;
        margin-inline: auto;
      }
      &-link {
        font-size: 20px;
        text-transform: uppercase;
        color: #fff;
      }
    }
  }

  &__categories {
    &-title {
      margin-block: 100px 50px;
      color: #252525;
      font-size: 36px;
      font-weight: 300;
    }

    &-list {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 100px;

      &-item {
        position: relative;

        &-img {
          width: 100%;
        }

        &-value {
          position: absolute;
          bottom: 0;
          width: 100%;
          padding-block: 15px;
          text-align: center;
          font-size: 20px;
          font-weight: 400;
          color: #fff;
          background-color: #e0bea2c1;
        }
      }
    }
  }
}
</style>
