<script lang="ts" setup>
import { HeroIcons } from "~/assets/icons/types/hero-icons";
const modalsStore = useModalsStore();
const route = useRoute();
const color = computed(() => {
  return route.name === "index" ? "#fff" : "#252525";
});

const routeName = ref<string | undefined>("");
const searchValue = ref(false);

watch(
  () => route.name,
  (newVal) => {
    console.log("route.name changed:", newVal);
    routeName.value = typeof newVal === "string" ? newVal : undefined;
  },
  { immediate: true }
);
</script>
<template>
  <div class="header-component">
    <div class="container">
      <div class="header-component__wraper">
        <button
          class="header-component__wraper-logo"
          @click="modalsStore.openModal('menu')"
        >
          <Icon
            class="header-component__wraper-logo-icon"
            :name="HeroIcons.MENU_SOLID"
            size="40"
          />
        </button>
        <nav class="header-component__wraper-nav">
          <ul class="header-component__wraper-nav-list">
            <NuxtLink class="header-component__wraper-nav-list-link" to="/"
              >Главная</NuxtLink
            >
            <NuxtLink
              class="header-component__wraper-nav-list-link"
              to="/catalog"
              >Каталог</NuxtLink
            >
            <!-- <CurvedLogo /> -->
            <NuxtLink class="header-component__wraper-nav-list-link" to="/about"
              >О нас</NuxtLink
            >
            <NuxtLink
              class="header-component__wraper-nav-list-link"
              to="/contacts"
              >Контакты</NuxtLink
            >
          </ul>
        </nav>

        <div class="header-component__wraper-actions">
          <Icon
            class="header-component__wraper-actions-icon"
            :name="HeroIcons.SEARCH_SOLID"
            size="28"
            @click="searchValue = !searchValue"
          />
          <NuxtLink to="/account">
            <Icon
              class="header-component__wraper-actions-icon"
              :name="HeroIcons.user"
              size="28"
            />
          </NuxtLink>
          <NuxtLink to="/favorite">
            <Icon
              class="header-component__wraper-actions-icon"
              :name="HeroIcons.heart"
              size="28"
          /></NuxtLink>
          <NuxtLink to="/basket">
            <Icon
              class="header-component__wraper-actions-icon"
              :name="HeroIcons.basket"
              size="28"
            />
          </NuxtLink>
        </div>
      </div>
      <BaseSearchComponent v-if="searchValue" @close="searchValue = false" />
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
  padding-block: 25px;
  // background-color: rgba(255, 0, 0, 0.487);

  &__wraper {
    display: flex;
    justify-content: space-between;
    align-items: center;

    &-nav {
      &-list {
        list-style: none;
        display: none;
        gap: 30px;
        align-items: center;
        @include mediaTablet {
          display: flex;
        }
        &-link {
          color: v-bind(color) !important;
          &:hover {
            color: $accent;
          }
        }
      }
    }

    &-actions {
      display: flex;
      gap: 15px;

      &-icon {
        @include header_link;
        font-weight: 700;
        color: v-bind(color);
        cursor: pointer;
      }
    }

    &-logo {
      @include header_link;
      &-icon {
        cursor: pointer;
        color: v-bind(color);
        font-weight: 900;
      }
    }
  }
}
</style>
