<script setup lang="ts">
import { HeroIcons } from '~/assets/icons/types/hero-icons';

const modalsStore = useModalsStore();
const closeMenu = ref(false);

interface IModalMenu {
  title: string;
  url: string;
  icon?: string;
}

const menuModalLinks: IModalMenu[] = [
  { title: "Главная", url: "/", icon: "i-heroicons-home" },
  { title: "Каталог", url: "/catalog", icon: "i-heroicons-squares-2x2" },
  { title: "О нас", url: "/about", icon: "i-heroicons-information-circle" },
  { title: "Контакты", url: "/contacts", icon: "i-heroicons-phone" },
  { title: "Личный кабинет", url: "/account", icon: "i-heroicons-user" },
  { title: "Избранное", url: "/favorite", icon: "i-heroicons-heart" },
  { title: "Корзина", url: "/basket", icon: "i-heroicons-shopping-cart" },
];

const goToLink = (link: string) => {
  closeMenu.value = true;
  setTimeout(() => {
    navigateTo(link);
    modalsStore.closeModal("menu");
  }, 500);
};

const closeMenuHandler = () => {
  closeMenu.value = true;
  setTimeout(() => {
    modalsStore.closeModal("menu");
  }, 500);
};
</script>

<template>
  <Teleport to="body">
    <div class="modal-menu__overlay" @click.self="closeMenuHandler()">
      <div class="modal-menu" :class="{ 'modal-menu--closing': closeMenu }">
        <div class="modal-menu__header">
          <div class="modal-menu__header-logo">ClothCrash</div>
          <button
            class="modal-menu__header-close"
            @click="closeMenuHandler()"
          >
            <Icon :size="30" :name="HeroIcons.CLOSE" />
          </button>
        </div>

        <nav class="modal-menu__nav">
          <ul class="modal-menu__list">
            <li
              v-for="link in menuModalLinks"
              :key="link.url"
              class="modal-menu__item"
            >
              <NuxtLink
                :to="link.url"
                class="modal-menu__link"
                @click="goToLink(link.url)"
              >
                <span v-if="link.icon" class="link-icon" :class="link.icon"
                  ><Icon :size="20" :name="link.icon" />
                </span>
                <span class="link-text">{{ link.title }}</span>
                <span class="link-arrow">→</span>
              </NuxtLink>
            </li>
          </ul>
        </nav>

        <div class="modal-menu__footer">
          <div class="social-links">
            <a href="#" class="social-link">Instagram</a>
            <a href="#" class="social-link">Telegram</a>
            <a href="#" class="social-link">VK</a>
          </div>
          <div class="copyright">© 2025 Все права защищены</div>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<style scoped lang="scss">
.modal-menu__overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(5px);
  z-index: 110;
  display: flex;
  animation: fadeIn 0.3s ease forwards;
}

.modal-menu {
  position: relative;
  width: 90vw;
  max-width: 380px;
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  height: 100vh;
  padding: 30px;
  box-shadow: 10px 0 30px rgba(0, 0, 0, 0.3);
  animation: slideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  display: flex;
  flex-direction: column;
  color: #fff;
  border-right: 1px solid rgba(255, 255, 255, 0.1);

  &--closing {
    animation: slideOut 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }

  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);

    &-logo {
      font-size: 24px;
      font-weight: 700;
      background: linear-gradient(90deg, #e0bea2 0%, #d8a675 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    &-close {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.3s ease;

      &:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: rotate(90deg);
      }
    }
  }

  &__nav {
    margin-top: 40px;
    flex-grow: 1;
  }

  &__list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  &__item {
    position: relative;
    overflow: hidden;
    border-radius: 8px;

    &:hover {
      background: rgba(255, 255, 255, 0.05);
    }

    &::before {
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      width: 3px;
      background: linear-gradient(to bottom, #e0bea2, #d8a675);
      transform: translateX(-100%);
      transition: transform 0.3s ease;
    }

    &:hover::before {
      transform: translateX(0);
    }
  }

  &__link {
    text-decoration: none;
    font-size: 16px;
    color: #fff;
    font-weight: 400;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    gap: 15px;
    transition: all 0.3s ease;
    position: relative;

    &:hover {
      color: #e0bea2;
      padding-left: 25px;

      .link-arrow {
        opacity: 1;
        transform: translateX(0);
      }
    }
  }

  &__footer {
    margin-top: auto;
    padding-top: 30px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }

  .link-icon {
    font-size: 20px;
    color: #e0bea2;
    width: 24px;
    display: flex;
    justify-content: center;
  }

  .link-text {
    flex-grow: 1;
  }

  .link-arrow {
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.3s ease;
    color: #d8a675;
  }

  .social-links {
    display: flex;
    gap: 15px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }

  .social-link {
    color: rgba(255, 255, 255, 0.6);
    font-size: 14px;
    text-decoration: none;
    transition: color 0.3s ease;

    &:hover {
      color: #e0bea2;
    }
  }

  .copyright {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.4);
  }

  .close-icon {
    width: 20px;
    height: 20px;
    position: relative;

    span {
      position: absolute;
      height: 2px;
      width: 100%;
      background: #fff;
      top: 50%;
      left: 0;

      &:first-child {
        transform: rotate(45deg);
      }

      &:last-child {
        transform: rotate(-45deg);
      }
    }
  }
}

@keyframes slideIn {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideOut {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(-100%);
    opacity: 0;
  }
}

@keyframes fadeIn {
  from {
    background-color: rgba(0, 0, 0, 0);
    backdrop-filter: blur(0);
  }
  to {
    background-color: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(5px);
  }
}
</style>
