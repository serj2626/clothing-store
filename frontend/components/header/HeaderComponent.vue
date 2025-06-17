<script lang="ts" setup>
import { headerIconLinks, headerLinks } from "~/assets/data/header.data";
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
            <NuxtLink
              v-for="link in headerLinks"
              :key="link.name"
              class="header-component__wraper-nav-list-link"
              :class="{ active: link.name === routeName }"
              :to="link.to"
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
          color: v-bind(color);
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

      &-icon {
        @include header_link;
      
        color: v-bind(color);
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
      &-icon {
        cursor: pointer;
        color: v-bind(color);
        font-weight: 900;
      }
    }
  }
}
</style>
