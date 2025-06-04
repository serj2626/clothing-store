<script lang="ts" setup>
import { HeroIcons } from "~/assets/icons/types/hero-icons";
</script>
<template>
  <div class="home-page">
    <section class="home-page__hero">
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

    <section class="home-page__subscribe">
      <div class="container">
        <h2 class="home-page__subscribe-title">Узнайте первым о новинках</h2>
        <form action="" class="home-page__subscribe-form">
          <input
            class="home-page__subscribe-form-input"
            type="email"
            placeholder="Введите ваш email"
          />
          <button class="home-page__subscribe-form-btn" type="submit">
            Подписаться
          </button>
          <p class="home-page__subscribe-form-text">
            Нажимая на кнопку «Подписаться», я соглашаюсь на обработку моих
            персональных данных и ознакомлен(а) с условиями конфиденциальности.
          </p>
        </form>
      </div>
    </section>
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
    // filter: contrast(0.5);

    &-block {
      position: absolute;
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

  &__subscribe {
    margin-block: 100px 50px;

    &-title {
      text-align: center;
      color: #252525;
      font-size: 36px;
      font-weight: 300;
      margin-bottom: 50px;
    }

    &-form {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      max-width: 600px;
      width: 100%;
      margin: 0 auto;

      &-input {
        padding-block: 16px;
        border-radius: 5px;
        border: 1px solid #252525;
        color: #252525;
        opacity: 0.5;
        width: 100%;

        &::placeholder {
          text-align: center;
        }
      }

      &-btn {
        padding-block: 16px;
        border-radius: 5px;
        border: none;
        background-color: #e0bea2;
        color: #fff;
        cursor: pointer;
        width: 100%;
      }

      &-text {
        text-align: center;
        font-size: 16px;
        color: #252525;
        font-weight: 200;
      }
    }
  }
}
</style>
