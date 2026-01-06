<script setup lang="ts">
interface IProps {
  name: string;
  verified: boolean;
  date: string;
  rating: number;
  text: string;
  advantages: string;
  disadvantages: string;
}

defineProps<{ comment: IProps }>();

const generateStars = (rating: number) => {
  return Array.from({ length: 5 }, (_, i) => i < rating);
};
</script>

<template>
  <div class="product-detail-comments-card">
    <div class="product-detail-comments-card__header">
      <div class="product-detail-comments-card__user">
        <div class="product-detail-comments-card__avatar">
          {{ comment.name.charAt(0) }}
        </div>
        <div class="product-detail-comments-card__user-info">
          <div class="product-detail-comments-card__user-name">
            {{ comment.name }}
            <span
              v-if="comment.verified"
              class="product-detail-comments-card__verified"
              title="Проверенный покупатель"
            >
              ✓
            </span>
          </div>
          <div class="product-detail-comments-card__date">
            {{ comment.date }}
          </div>
        </div>
      </div>

      <div class="product-detail-comments-card__rating">
        <div class="product-detail-comments-card__stars">
          <Star
            v-for="(filled, index) in generateStars(comment.rating)"
            :key="index"
            :size="16"
            :class="[
              'product-detail-comments-card__star',
              filled
                ? 'product-detail-comments-card__star--filled'
                : 'product-detail-comments-card__star--empty'
            ]"
          />
        </div>
        <div class="product-detail-comments-card__rating-value">
          {{ comment.rating }}/5
        </div>
      </div>
    </div>

    <div class="product-detail-comments-card__content">
      <p class="product-detail-comments-card__text">
        {{ comment.text }}
      </p>

      <div class="product-detail-comments-card__pros-cons">
        <div class="product-detail-comments-card__pros">
          <span class="product-detail-comments-card__label product-detail-comments-card__label--positive">
            👍 Плюсы:
          </span>
          <span class="product-detail-comments-card__value">
            {{ comment.advantages }}
          </span>
        </div>
        <div class="product-detail-comments-card__cons">
          <span class="product-detail-comments-card__label product-detail-comments-card__label--negative">
            👎 Минусы:
          </span>
          <span class="product-detail-comments-card__value">
            {{ comment.disadvantages }}
          </span>
        </div>
      </div>
    </div>

    <div class="product-detail-comments-card__footer">
      <button class="product-detail-comments-card__helpful-button">
        <span class="product-detail-comments-card__helpful-text">Полезно?</span>
        <span class="product-detail-comments-card__helpful-count">12</span>
      </button>
      <button class="product-detail-comments-card__reply-button">
        Ответить
      </button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.product-detail-comments-card {
  background: $white;
  border-radius: 16px;
  padding: 24px;
  height: 100%;
  display: flex;
  flex-direction: column;
  border: 1px solid #e2e8f0;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
      0 10px 10px -5px rgba(0, 0, 0, 0.04);
    border-color: #cbd5e1;
  }
}

.product-detail-comments-card__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
}

.product-detail-comments-card__user {
  display: flex;
  align-items: center;
  gap: 12px;
}

.product-detail-comments-card__avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: $accent;
  color: $white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.125rem;
}

.product-detail-comments-card__user-info {
  display: flex;
  flex-direction: column;
}

.product-detail-comments-card__user-name {
  font-weight: 600;
  color: #0f172a;
  display: flex;
  align-items: center;
  gap: 4px;
}

.product-detail-comments-card__verified {
  color: #10b981;
  font-size: 0.875rem;
}

.product-detail-comments-card__date {
  font-size: 0.875rem;
  color: #64748b;
}

.product-detail-comments-card__rating {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.product-detail-comments-card__stars {
  display: flex;
  gap: 2px;
}

.product-detail-comments-card__star {
  &--filled {
    fill: #fbbf24;
    stroke: #fbbf24;
  }

  &--empty {
    fill: #e2e8f0;
    stroke: #cbd5e1;
  }
}

.product-detail-comments-card__rating-value {
  font-size: 0.875rem;
  font-weight: 600;
  color: #475569;
}

.product-detail-comments-card__content {
  flex: 1;
  margin-bottom: 20px;
}

.product-detail-comments-card__text {
  color: $txt;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 0.9375rem;
}

.product-detail-comments-card__pros-cons {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.product-detail-comments-card__pros,
.product-detail-comments-card__cons {
  display: flex;
  gap: 8px;
  font-size: 0.875rem;
  line-height: 1.5;
}

.product-detail-comments-card__label {
  font-weight: 600;
  white-space: nowrap;

  &--positive {
    color: #10b981;
  }

  &--negative {
    color: #ef4444;
  }
}

.product-detail-comments-card__value {
  color: #475569;
}

.product-detail-comments-card__footer {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-top: 16px;
  border-top: 1px solid #f1f5f9;
}

.product-detail-comments-card__helpful-button {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  font-size: 0.875rem;
  color: #64748b;
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover {
    background: #f1f5f9;
    border-color: #cbd5e1;
  }
}

.product-detail-comments-card__helpful-text {
  color: inherit;
}

.product-detail-comments-card__helpful-count {
  font-weight: 600;
  color: #475569;
}

.product-detail-comments-card__reply-button {
  padding: 6px 12px;
  background: transparent;
  border: none;
  font-size: 0.875rem;
  color: #3b82f6;
  cursor: pointer;
  transition: color 0.2s ease;

  &:hover {
    color: #2563eb;
    text-decoration: underline;
  }
}
</style>