<script setup lang="ts">
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
]);

const openGallery = (photos, index) => {
  // Здесь будет логика открытия галереи
  console.log("Open gallery at index:", index);
};
</script>
<template>
  <div class="ozon-comments">
    <div class="comments-header">
      <h3 class="comments-title">Отзывы о товаре</h3>
      <div class="likes-block">
        <button class="like-btn" :class="{ liked: isLiked }">
          <Icon name="ph:heart" class="like-icon" />
          <span @click="modalsStore.openModal('review')" class="likes-count"
            >{{ likesCount }} человеку понравился товар</span
          >
        </button>
      </div>
    </div>

    <div class="comments-list">
      <div v-for="comment in comments" :key="comment.id" class="comment-item">
        <div class="comment-user">
          <div class="user-avatar">
            <Icon name="ph:user-circle" />
          </div>
          <div class="user-info">
            <span class="user-name">{{ comment.userName }}</span>
            <span class="comment-date">{{ comment.date }}</span>
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

        <div class="comment-text">{{ comment.text }}</div>

        <div v-if="comment.photos.length" class="comment-photos">
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
        </div>

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
  </div>
</template>
<style scoped lang="scss">
.ozon-comments {
  background: $white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.comments-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba($txt, 0.1);
}

.comments-title {
  font-family: $ff_title;
  font-size: 22px;
  font-weight: 700;
  color: $txt;
  margin: 0;
}

.likes-block {
  display: flex;
  align-items: center;
}

.like-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px 12px;
  border-radius: 6px;
  transition: $default_transition;
  font-family: $ff_second;
  color: $txt;

  &:hover {
    background: rgba($accent, 0.1);
  }

  &.liked {
    .like-icon {
      color: $error;
    }
  }
}

.like-icon {
  font-size: 20px;
  transition: $default_transition;
}

.likes-count {
  font-size: 14px;
  color: rgba($txt, 0.7);
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
  .ozon-comments {
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
