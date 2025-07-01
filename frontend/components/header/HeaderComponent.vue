<script lang="ts" setup>
import { headerIconLinks, headerLinks } from "~/assets/data/header.data";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const modalsStore = useModalsStore();
const route = useRoute();
const isHomePage = computed(() => {
  return route.name === "index";
});

const routeName = ref<string | undefined>("");
const searchValue = ref(false);

watch(
  () => route.name,
  (newVal) => {
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
            size="50"
          />
        </button>
        <nav class="header-component__wraper-nav">
          <ul class="header-component__wraper-nav-list">
            <NuxtLink
              v-for="link in headerLinks"
              :key="link.name"
              class="header-component__wraper-nav-list-link"
              :class="{ active: link.name === routeName }"
              :to="link.to"
              :style="{ color: isHomePage ? '#fff' : '' }"
            >
              {{ link.title }}
            </NuxtLink>
          </ul>
        </nav>

        <div class="header-component__wraper-actions">
          <Icon
            class="header-component__wraper-actions-icon"
            :name="HeroIcons.SEARCH_SOLID"
            size="28"
            :style="{ color: isHomePage ? '#fff' : '' }"
            @click="searchValue = !searchValue"
          />
          <NuxtLink
            v-for="item in headerIconLinks"
            :key="item.name"
            :to="item.to"
          >
            <Icon
              class="header-component__wraper-actions-icon"
              :class="{ active: item.name === routeName }"
              :style="{ color: isHomePage ? '#fff' : '' }"
              :name="item.icon"
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
  padding-block: 35px;

  &__wraper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;

    &-nav {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      &-list {
        list-style: none;
        display: none;
        gap: 30px;
        align-items: center;
        @include mediaTablet {
          display: flex;
        }
        &-link {
          // color: v-bind(color);
          color: var(--color-header-link);
          &:hover {
            color: $accent;
          }
          &.active {
            color: $accent;
            font-weight: bold;
            text-shadow: 0 1px 0 rgba(0, 0, 0, 0.479),
              0 2px 3px rgba(0, 0, 0, 0.076), 0 0 10px rgba($accent, 0.4);
          }
        }
      }
    }

    &-actions {
      display: flex;
      gap: 15px;
      margin-left: auto;

      &-icon {
        @include header_link;

        // color: v-bind(color);
        color: var(--color-header-link);
        cursor: pointer;
        &.active {
          color: $accent-dark;
          font-weight: bold;
          text-shadow: 0 1px 0 rgba(0, 0, 0, 0.479),
            0 2px 3px rgba(0, 0, 0, 0.076), 0 0 10px rgba($accent, 0.4);
        }
      }
    }

    &-logo {
      @include header_link;
      position: fixed;
      top: 26px;
      left: 100px;
      &-icon {
        cursor: pointer;
        color: var(--color-header-link);
        font-weight: 900;
      }
    }
  }
}
</style>
