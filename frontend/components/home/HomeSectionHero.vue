<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
</script>
<template>
  <section class="home-section-hero">
    <div class="home-section-hero-overlay" />
    <div class="home-section-hero-block">
      <h2 class="home-section-hero-block-title">Новая коллекция</h2>
      <div class="home-section-hero-block-separator" />
      <NuxtLink class="home-section-hero-block-link" to="/news">
        <div class="hero-link-content">
          <span>Смотреть Новинки</span>
          <Icon :name="HeroIcons.ARROW_RIGHT_SOLID" size="22" />
        </div>
      </NuxtLink>
    </div>
  </section>
</template>
<style scoped lang="scss">
.home-section-hero {
  position: relative;
  width: 100%;
  height: 130vh;
  background-image: url("/store.jpg");
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
      text-decoration: none;
      display: inline-flex;
      align-items: center;

      .hero-link-content {
        display: flex;
        align-items: center;
        gap: 10px;
      }
    }
  }
}
</style>
