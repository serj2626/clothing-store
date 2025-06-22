<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IReview } from "~/types";

const modalsStore = useModalsStore();
const likesCount = ref(128);
const isLiked = ref(false);

const comments = ref([
  {
    id: 1,
    userName: "Анна П.",
    date: "15 мая 2023",
    rating: 5,
    text: "Отличное качество, удобная посадка. Заказала свой обычный размер - подошел идеально.",
    photos: ["/favorites/one.png", "/favorites/two.png"],
    advantages: "Качество, посадка, материал",
    disadvantages: "Нет",
  },
  {
    id: 2,
    userName: "Иван С.",
    date: "10 мая 2023",
    rating: 4,
    text: "Хорошая куртка, но цвет немного отличается от фото на сайте. В жизни темнее.",
    photos: ["/favorites/three.png"],
    advantages: "Теплая, удобная",
    disadvantages: "Цвет отличается",
  },
  {
    id: 3,
    userName: "Иван С.",
    date: "10 мая 2023",
    rating: 4,
    text: "Хорошая куртка, но цвет немного отличается от фото на сайте. В жизни темнее.",
    photos: ["/favorites/three.png"],
    advantages: "Теплая, удобная",
    disadvantages: "Цвет отличается",
  },
  {
    id: 4,
    userName: "Иван С.",
    date: "10 мая 2023",
    rating: 4,
    text: "Хорошая куртка, но цвет немного отличается от фото на сайте. В жизни темнее.",
    photos: ["/favorites/three.png"],
    advantages: "Теплая, удобная",
    disadvantages: "Цвет отличается",
  },
  {
    id: 5,
    userName: "Иван С.",
    date: "10 мая 2023",
    rating: 4,
    text: "Хорошая куртка, но цвет немного отличается от фото на сайте. В жизни темнее.",
    photos: ["/favorites/three.png"],
    advantages: "Теплая, удобная",
    disadvantages: "Цвет отличается",
  },
]);

const openGallery = (photos, index) => {
  // Здесь будет логика открытия галереи
  console.log("Open gallery at index:", index);
};

const props = defineProps<{
  reviews: IReview[];
}>();

const countReviews = computed(() => {
  return props.reviews.length;
});
</script>
<template>
  <div class="product-detail-comments">
    <div class="product-detail-comments__header">
      <div class="product-detail-comments__header-top">
        <h3 class="product-detail-comments__header-top-title">
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

    <div v="else" class="comments-list">
      <div v-for="comment in reviews" :key="comment.id" class="comment-item">
        <div class="comment-user">
          <div class="user-avatar">
            <Icon name="ph:user-circle" />
          </div>
          <div class="user-info">
            <span class="user-name">{{ comment.email }}</span>
            <span class="comment-date"
              >{{ comment.time_age }} -
              {{ formatDate(comment.created_at) }}</span
            >
          </div>
        </div>

        <div class="comment-rating">
          <div class="stars">
            <Icon
              v-for="star in 5"
              :key="star"
              name="ph:star-fill"
              :class="{ active: star <= comment.rating }"
            />
          </div>
          <span class="rating-value">{{ comment.rating }} из 5</span>
        </div>

        <div class="comment-text">{{ comment.description }}</div>

        <!-- <div v-if="comment.photos.length" class="comment-photos">
          <div
            v-for="(photo, idx) in comment.photos"
            :key="idx"
            class="photo-thumb"
            @click="openGallery(comment.photos, idx)"
          >
            <NuxtImg
              :src="photo"
              loading="lazy"
              format="webp"
              width="100"
              height="100"
            />
          </div>
        </div> -->

        <div v-if="comment.advantages" class="comment-props">
          <div class="prop-item advantage">
            <span class="prop-label">Достоинства:</span>
            <span class="prop-value">{{ comment.advantages }}</span>
          </div>
        </div>

        <div v-if="comment.disadvantages" class="comment-props">
          <div class="prop-item disadvantage">
            <span class="prop-label">Недостатки:</span>
            <span class="prop-value">{{ comment.disadvantages }}</span>
          </div>
        </div>
      </div>
    </div>
    <BasePaginationComponent v-if="countReviews > 0" />
  </div>
</template>
<style scoped lang="scss">
.product-detail-comments {
  background: $white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
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
        font-family: $ff_title;
        font-size: 22px;
        font-weight: 700;
        color: $txt;
        margin: 0;
      }
    }
  }
}
.comment-item {
  padding: 20px 0;
  border-bottom: 1px solid rgba($txt, 0.1);

  &:last-child {
    border-bottom: none;
  }
}

.comment-user {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.user-avatar {
  .icon {
    font-size: 40px;
    color: rgba($txt, 0.5);
  }
}

.user-info {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-family: $ff_second;
  font-weight: 500;
  font-size: 15px;
  color: $txt;
}

.comment-date {
  font-family: $ff_second;
  font-size: 13px;
  color: rgba($txt, 0.5);
}

.comment-rating {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.stars {
  display: flex;
  gap: 2px;

  .icon {
    font-size: 18px;
    color: rgba($txt, 0.2);

    &.active {
      color: $accent-dark;
    }
  }
}

.rating-value {
  font-family: $ff_second;
  font-size: 14px;
  color: rgba($txt, 0.7);
}

.comment-text {
  font-family: $ff_second;
  font-size: 15px;
  line-height: 1.5;
  color: $txt;
  margin-bottom: 16px;
}

.comment-photos {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.photo-thumb {
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

.comment-props {
  margin-bottom: 12px;
}

.prop-item {
  display: flex;
  gap: 8px;
  font-family: $ff_second;
  font-size: 14px;
  line-height: 1.4;

  &.advantage {
    .prop-label {
      color: #0a7f41;
    }
  }

  &.disadvantage {
    .prop-label {
      color: #d23736;
    }
  }
}

.prop-label {
  font-weight: 500;
  white-space: nowrap;
}

.prop-value {
  color: rgba($txt, 0.8);
}

@include mediaTablet {
  .product-detail-comments {
    padding: 32px;
  }

  .comments-title {
    font-size: 24px;
  }

  .photo-thumb {
    width: 100px;
    height: 100px;
  }
}
</style>
