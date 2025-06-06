<script setup lang="ts">
const modalsStore = useModalsStore();
const closeMenu = ref(false);

interface IModalMenu {
  title: string;
  url: string;
}

const menuModalLinks: IModalMenu[] = [
  { title: "Главная", url: "/" },
  { title: "Каталог", url: "/catalog" },
  { title: "О нас", url: "/about" },
  { title: "Контакты", url: "/contacts" },
  { title: "Личный кабинет", url: "/account" },
  { title: "Избранное", url: "/favorite" },
  { title: "Корзина", url: "/basket" },
];

const goToLink = (link: string) => {
  closeMenu.value = true;
  setTimeout(() => {
    navigateTo(link);
    modalsStore.closeModal("menu");
  }, 500);
};
</script>

<template>
  <Teleport to="body">
    <div
      class="modal-menu__overlay"
      @click.self="modalsStore.closeModal('menu')"
    >
      <div class="modal-menu">
        <button
          class="modal-menu__close"
          @click="modalsStore.closeModal('menu')"
        >
          ×
        </button>
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
                {{ link.title }}
              </NuxtLink>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </Teleport>
</template>

<style scoped lang="scss">
.modal-menu__overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 110;
  display: flex;
  animation: fadeIn 0.3s ease forwards;
}

.modal-menu {
  position: relative;
  width: 80vw;
  max-width: 320px;
  background-color: #fff;
  height: 100vh;
  padding: 40px 24px;
  box-shadow: 4px 0 20px rgba(0, 0, 0, 0.1);
  animation: slideIn 0.4s ease-out forwards;

  @media (min-width: 768px) {
    width: 320px;
  }

  &__close {
    position: absolute;
    top: 2px;
    right: 10px;
    font-size: 58px;
    background: none;
    border: none;
    cursor: pointer;
    color: #aaa;
    transition: color 0.2s ease;

    &:hover {
      color: #e0bea2;
    }
  }

  &__nav {
    margin-top: 40px;
  }

  &__list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  &__item {
    border-bottom: 1px solid #b3a7a783;
    padding-bottom: 10px;
  }

  &__link {
    text-decoration: none;
    font-size: 18px;
    color: #252525;
    font-weight: 500;
    transition: color 0.2s ease;

    &:hover {
      color: #e0bea2;
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

@keyframes fadeIn {
  from {
    background-color: rgba(0, 0, 0, 0);
  }
  to {
    background-color: rgba(0, 0, 0, 0.4);
  }
}
</style>
