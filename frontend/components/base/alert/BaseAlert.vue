<script setup lang="ts">
interface IProps {
  type?: "basket" | "favorite" | "reviews" | "orders" | "search";
}

const { type = "basket" } = defineProps<IProps>();

const alertConfig = computed(() => {
  const configs = {
    basket: {
      title: "Ваша корзина пуста",
      description: "Добавьте товары, чтобы сделать заказ",
      icon: "ph:shopping-cart-simple-bold",
      buttonText: "В каталог",
      route: "/catalog",
    },
    favorite: {
      title: "Избранное пустое",
      description: "Сохраняйте понравившиеся товары здесь",
      icon: "ph:heart-bold",
      buttonText: "Найти товары",
      route: "/catalog",
    },
    reviews: {
      title: "Отзывов пока нет",
      description: "Будьте первым, кто оставит свой комментарий",
      icon: "ph:chat-centered-text-bold",
      buttonText: "",
      route: "",
    },
    orders: {
      title: "У вас нет заказов",
      description: "После оформления заказа он появится здесь",
      icon: "ph:package-bold",
      buttonText: "В каталог",
      route: "/catalog",
    },
    search: {
      title: "Ничего не найдено",
      description: "Попробуйте изменить параметры поиска",
      icon: "ph:magnifying-glass-bold",
      buttonText: "Сбросить фильтры",
      route: "",
    },
  };

  return configs[type];
});
</script>

<template>
  <div class="base-alert">
    <div class="base-alert__content">
      <Icon :name="alertConfig.icon" class="base-alert__icon" />

      <h3 class="base-alert__title">
        {{ alertConfig.title }}
      </h3>

      <p class="base-alert__description">
        {{ alertConfig.description }}
      </p>

      <NuxtLink
        v-if="alertConfig.buttonText"
        :to="alertConfig.route"
        class="base-alert__button"
      >
        {{ alertConfig.buttonText }}
      </NuxtLink>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.base-alert {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  max-width: 500px;
  margin: 0 auto;

  &__content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  &__icon {
    font-size: 3rem;
    color: $accent;
    margin-bottom: 1rem;
  }

  &__title {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--color-text);
    margin: 0;
  }

  &__description {
    font-size: 1rem;
   color: var(--color-text);
    margin: 0;
    line-height: 1.5;
  }

  &__button {
    margin-top: 1.5rem;
    padding: 0.75rem 1.5rem;
    background: var(--color-primary);
    color: white;
    border-radius: 8px;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.2s ease;

    &:hover {
      background: var(--color-primary-hover);
      transform: translateY(-2px);
    }
  }
}
</style>
