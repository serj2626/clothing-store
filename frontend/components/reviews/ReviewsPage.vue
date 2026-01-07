<script lang="ts" setup>
import { comments } from "~/api/data/comments";
const { id } = useRoute().params;
</script>

<template>
  <div class="reviews-page">
    <div class="container">
      <BaseButton
        label="Назад"
        size="xs"
        color="teal"
        radius="4px"
        @click="$router.back()"
      />
      <div class="reviews-page__content">
        <h2 class="reviews-page__title">Отзывы покупателей</h2>
        <div class="reviews-page__subtitle">
          Что говорят наши клиенты о товаре
        </div>
        <ul class="reviews-page__list">
          <li
            class="reviews-page__list-item"
            v-for="comment in comments.slice(0, 4)"
            :key="comment.id"
          >
            <ProductDetailCommentsCard :comment="comment" />
          </li>
        </ul>
        <PaginationComponent class="reviews-page__pagination" />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.reviews-page__content {
  max-width: 1100px;
  margin-inline: auto;
}
.reviews-page {
  margin-top: 150px;
  &__title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #0f172a 0%, #475569 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
    letter-spacing: -0.025em;
  }
  &__subtitle {
    text-align: center;
    font-size: 1.125rem;
    color: #64748b;
    font-weight: 500;
  }
  &__list {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    gap: 24px;
  }
  &__pagination {
    margin-block: 40px;
  }
}
</style>
