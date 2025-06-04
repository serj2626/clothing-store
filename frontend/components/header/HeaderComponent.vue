<script lang="ts" setup>
import { HeroIcons } from "~/assets/icons/types/hero-icons";
</script>
<template>
  <div class="header-component">
    <div class="container">
      <div class="header-component__wraper">
        <button class="header-component__wraper-logo">
          <Icon
            class="header-component__wraper-logo-icon"
            :name="HeroIcons.MENU_SOLID"
            size="40"
          />
        </button>
        <nav class="nav">
          <ul>
            <li><a href="#">Главная</a></li>
            <li><a href="#">Каталог</a></li>
            <li><a href="#">О нас</a></li>
            <li><a href="#">Контакты</a></li>
          </ul>
        </nav>
        <div class="header-component__wraper-actions">
          <Icon
            class="header-component__wraper-actions-icon"
            :name="HeroIcons.SEARCH_SOLID"
            size="28"
          />
          <Icon
            class="header-component__wraper-actions-icon"
            :name="HeroIcons.USER_SOLID"
            size="28"
          />
          <Icon
            class="header-component__wraper-actions-icon"
            :name="HeroIcons.HEART_SOLID"
            size="28"
          />
          <Icon
            class="header-component__wraper-actions-icon"
            :name="HeroIcons.BASKET_SOLID"
            size="28"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
@mixin header-link {
  transition: all 0.3s ease-in-out;

  &:hover {
    scale: 1.1;
  }
  &:active {
    scale: 0.8;
  }
}

.header-component {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 100;

  background-color: transparent;
  width: 100%;
  padding-block: 20px;

  &__wraper {
    display: flex;
    justify-content: space-between;
    align-items: center;

    &-actions {
      display: flex;
      gap: 15px;

      &-icon {
        @include header_link;
        font-weight: 700;
        color: white;
        cursor: pointer;
      }
    }

    &-logo {
      @include header_link;
      &-icon {
        cursor: pointer;
        color: white;
        font-weight: 900;
      }
    }
  }
}

.nav ul {
  list-style: none;
  display: flex;
  gap: 30px;
  margin: 0;
  padding: 0;
}
</style>
