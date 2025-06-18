<script setup lang="ts">
import { menuModalLinks } from "~/assets/data/header.data";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const modalsStore = useModalsStore();
const closeMenu = ref(false);

// Обработчик клавиши ESC
const handleKeydown = (e: KeyboardEvent) => {
  if (e.key === "Escape" && !closeMenu.value) {
    closeMenuHandler();
  }
};

// Вешаем обработчик при монтировании
onMounted(() => {
  window.addEventListener("keydown", handleKeydown);
});

// Удаляем при демонтировании
onBeforeUnmount(() => {
  window.removeEventListener("keydown", handleKeydown);
});

const goToLink = (link: string) => {
  closeMenu.value = true;
  setTimeout(() => {
    navigateTo(link);
    modalsStore.closeModal("menu");
  }, 300);
};

const closeMenuHandler = () => {
  if (closeMenu.value) return;

  closeMenu.value = true;
  setTimeout(() => {
    modalsStore.closeModal("menu");
  }, 300);
};
</script>

<template>
  <Teleport to="body">
    <div
      class="modal-menu__overlay"
      :class="{ 'modal-menu__overlay--closing': closeMenu }"
      @click.self="closeMenuHandler()"
    >
      <div class="modal-menu" :class="{ 'modal-menu--closing': closeMenu }">
        <div class="modal-menu__header">
          <div class="modal-menu__header-logo">ClothCrash</div>
          <button
            class="modal-menu__header-close"
            @click="closeMenuHandler()"
            aria-label="Закрыть меню"
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
                <span v-if="link.icon" class="link-icon">
                  <Icon :size="20" :name="link.icon" />
                </span>
                <span class="link-text">{{ link.title }}</span>
                <span class="link-arrow">→</span>
              </NuxtLink>
            </li>
          </ul>
        </nav>

        <div class="modal-menu__footer">
          <div class="modal-menu__footer-data">
            <div class="modal-menu__footer-data-social-links">
              <a href="#" class="modal-menu__footer-data-social-links-link"
                >Instagram</a
              >
              <a href="#" class="modal-menu__footer-data-social-links-link"
                >Telegram</a
              >
              <a href="#" class="modal-menu__footer-data-social-links-link"
                >VK</a
              >
            </div>
            <div class="modal-menu__footer-data-copyright">
              © 2025 Все права защищены
            </div>
          </div>
          <div class="modal-menu__footer-actions">
            <button
              class="modal-menu__footer-actions-login"
              @click="goToLink('/auth/login')"
            >
              <Icon :name="HeroIcons.user" :size="26" />
            </button>
            <button class="modal-menu__footer-actions-color">
              <Icon :name="HeroIcons.NIGHT" :size="26" />
            </button>
          </div>
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

  &--closing {
    pointer-events: none;
  }
}

.modal-menu {
  position: relative;
  width: 100%;
  max-width: 380px;
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  height: 100vh;
  padding: 30px;
  box-shadow: 10px 0 30px rgba(0, 0, 0, 0.3);
  animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  display: flex;
  flex-direction: column;
  color: #fff;
  border-right: 1px solid rgba(255, 255, 255, 0.1);
  will-change: transform, opacity;

  @include mediaLaptop {
    width: 90vw;
  }

  &--closing {
    animation: slideOut 0.3s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    pointer-events: none;
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
      padding: 10px;
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
    display: flex;
    align-items: center;
    justify-content: space-between;
    &-actions {
      display: flex;
      align-items: center;
      gap: 10px;

      &-login,
      &-color {
        padding: 10px;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.1);
        border: none;
        cursor: pointer;
        padding: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.8s ease;

        &:hover {
          background: rgba(255, 255, 255, 0.2);
        }
      }
    }
    &-data {
      display: flex;
      flex-direction: column;
      gap: 10px;
      &-copyright {
        font-size: 14px;
        color: rgba(255, 255, 255, 0.4);
      }
      &-social-links {
        color: rgba(255, 255, 255, 0.6);
        font-size: 14px;
        text-decoration: none;
        transition: color 0.3s ease;
        display: flex;
        gap: 10px;

        &-link {
          color: $white;
        }

        &:hover {
          color: #e0bea2;
        }
      }
    }
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
</style>
