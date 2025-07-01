<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IReview } from "~/types";

const modalsStore = useModalsStore();

const props = defineProps<{
  reviews: IReview[];
}>();

const countReviews = computed(() => {
  return props.reviews.length;
});
</script>
<template>
  <div class="comment-list">
    <div class="comment-list__header">
      <div class="comment-list__header-top">
        <h3 class="comment-list__header-top-title">
          Отзывы о товаре ({{ countReviews }})
        </h3>
      </div>
      <BaseButtonWithIcon
        :icon="HeroIcons.PLUS"
        label="Написать отзыв"
        @click="modalsStore.openModal('review')"
      />
    </div>

    <div v-if="countReviews === 0" class="comments-list">
      <BaseAlert type="reviews" />
    </div>

    <div v-else class="comments-list">
      <CommentCard v-for="comment in reviews" :key="comment.id" :comment />
    </div>
    <BasePaginationComponent v-if="countReviews > 0" />
  </div>
</template>
<style scoped lang="scss">
.comment-list {
  border-radius: 12px;
  padding: 24px;
  box-shadow: var(--shadow-reviews-list);
  margin-bottom: 100px;

  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    align-items: center;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba($txt, 0.1);
    &-top {
      display: flex;
      align-items: center;
      gap: 20px;
      &-title {
        font-size: 22px;
        font-weight: 700;
        color: var(--color-section-title);
        margin: 0;
      }
    }
  }
}
</style>
