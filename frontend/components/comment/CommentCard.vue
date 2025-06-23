<script setup lang="ts">
import type { IReview } from "~/types";

defineProps<{ comment: IReview }>();

const openGallery = (photos, index) => {
  // Здесь будет логика открытия галереи
  console.log("Open gallery at index:", index);
};
</script>
<template>
  <div class="comment-card">
    <div class="comment-card__user">
      <div class="comment-card__user-avatar">
        <Icon name="ph:user-circle" />
      </div>
      <div class="comment-card__user-info">
        <span class="comment-card__user-info-name">{{ comment.email }}</span>
        <span class="comment-card__user-info-date"
          >{{ comment.time_age }} - {{ formatDate(comment.created_at) }}</span
        >
      </div>
    </div>

    <div class="comment-card__rating">
      <div class="comment-card__rating-stars">
        <Icon
          v-for="star in 5"
          :key="star"
          name="ph:star-fill"
          :class="{
            'comment-card__rating-stars_active': star <= comment.rating,
          }"
        />
      </div>
      <span class="comment-card__rating-value">{{ comment.rating }} из 5</span>
    </div>

    <div class="comment-card__text">{{ comment.description }}</div>

    <div v-if="comment.photos.length" class="comment-card__photos">
      <div
        v-for="(photo, idx) in comment.photos"
        :key="idx"
        class="comment-card__photos-item"
        @click="openGallery(comment.photos, idx)"
      >
        <NuxtImg
          :src="photo.image"
          :alt="photo.alt"
          loading="lazy"
          format="webp"
          width="100"
          height="100"
        />
      </div>
    </div>

    <div v-if="comment.advantages" class="comment-card__advantages">
      <div class="comment-card__advantages-item">
        <span class="comment-card__advantages-item-label">Достоинства:</span>
        <span class="comment-card__advantages-item-value">{{
          comment.advantages
        }}</span>
      </div>
    </div>

    <div v-if="comment.disadvantages" class="comment-card__disadvantages">
      <div class="comment-card__disadvantages-item">
        <span class="comment-card__disadvantages-item-label">Недостатки:</span>
        <span class="comment-card__disadvantages-item-value">{{
          comment.disadvantages
        }}</span>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.comment-card {
  padding: 20px 0;
  border-bottom: 1px solid rgba($txt, 0.1);
  &__user {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
    &-avatar {
      .icon {
        font-size: 40px;
        color: rgba($txt, 0.5);
      }
    }
    &-info {
      display: flex;
      flex-direction: column;
      &-name {
        font-family: $ff_second;
        font-weight: 500;
        font-size: 15px;
        color: $txt;
      }
      &-date {
        font-family: $ff_second;
        font-size: 13px;
        color: rgba($txt, 0.5);
      }
    }
  }
  &__rating {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
    &-stars {
      display: flex;
      gap: 2px;
      &_active {
        // color: rgb(236, 196, 51);
        color: $accent;
      }
    }
    &-value {
      font-family: $ff_second;
      font-size: 14px;
      color: rgba($txt, 0.7);
    }
  }
  &__text {
    font-size: 15px;
    line-height: 1.5;
    color: $txt;
    margin-bottom: 16px;
  }
  &__photos {
    display: flex;
    gap: 12px;
    margin-bottom: 16px;
    flex-wrap: wrap;
    &-item {
      width: 80px;
      height: 80px;
      border-radius: 6px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.2s ease;

      &:hover {
        transform: scale(1.05);
      }

      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }
  }
  &__advantages {
    margin-bottom: 12px;
    &-item {
      display: flex;
      gap: 8px;
      font-size: 14px;
      line-height: 1.4;
      &-label {
        color: $success;
      }
      &-value {
        color: rgba($txt, 0.8);
      }
    }
  }
  &__disadvantages {
    margin-bottom: 12px;
    &-item {
      display: flex;
      gap: 8px;
      font-size: 14px;
      line-height: 1.4;
      &-label {
        color: $error;
      }
      &-value {
        color: rgba($txt, 0.8);
      }
    }
  }
}
</style>
