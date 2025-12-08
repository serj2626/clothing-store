<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Autoplay } from "swiper/modules";
import type { Swiper as SwiperType } from "swiper";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const swiperInstance = ref<SwiperType | null>(null);
const currentSlideIndex = ref(0);
const totalSlides = ref(0);

// вызывается когда swiper инициализирован
const onSwiper = (swiper: SwiperType) => {
  swiperInstance.value = swiper;
  totalSlides.value = swiper.slides.length;
};

// вызывается на смене слайда
const onSlideChange = () => {
  currentSlideIndex.value = swiperInstance.value?.activeIndex || 0;
};

// методы управления
const goNext = () => swiperInstance.value?.slideNext();
const goPrev = () => swiperInstance.value?.slidePrev();

const comments = ref([
  {
    id: 1,
    name: "Иван Иванович",
    text: "Все очень хорошо! Качество превзошло ожидания, ткань приятная к телу, не мнется. Буду заказывать еще!",
    advantages: "Отлично сидит",
    disadvantages: "Цена",
    rating: 5,
    date: "2 дня назад",
    verified: true,
  },
  {
    id: 2,
    name: "Мария Петрова",
    text: "Качество ткани порадовало, приятный цвет, хорошо тянется. Очень довольна покупкой!",
    advantages: "Мягкая и приятная ткань",
    disadvantages: "Долго ждала доставку",
    rating: 4,
    date: "1 неделю назад",
    verified: true,
  },
  {
    id: 3,
    name: "Алексей Смирнов",
    text: "Размер совпал идеально, как по меркам. Сидит как влитой, рекомендую!",
    advantages: "Соответствие размеру",
    disadvantages: "Нет ярких расцветок",
    rating: 5,
    date: "3 дня назад",
    verified: false,
  },
  {
    id: 4,
    name: "Екатерина Кузнецова",
    text: "Стильная и удобная одежда для повседневной носки. Носится хорошо, не выцветает.",
    advantages: "Современно выглядит",
    disadvantages: "Скользит на гладкой поверхности",
    rating: 4,
    date: "2 недели назад",
    verified: true,
  },
  {
    id: 5,
    name: "Дмитрий Орлов",
    text: "Товар соответствует описанию на 100%. Качественные материалы и хороший пошив.",
    advantages: "Приятная цена",
    disadvantages: "Швы немного торчат",
    rating: 4,
    date: "5 дней назад",
    verified: true,
  },
  {
    id: 6,
    name: "Ольга Соколова",
    text: "Хорошо подошло на подарок. Получатель был доволен, выглядит стильно и современно.",
    advantages: "Красивый цвет",
    disadvantages: "Не очень плотная ткань",
    rating: 3,
    date: "1 месяц назад",
    verified: false,
  },
  {
    id: 7,
    name: "Никита Волков",
    text: "Супер качество за свои деньги. Рекомендую к покупке, не пожалеете!",
    advantages: "Надёжный материал",
    disadvantages: "Нет вариантов размера XL",
    rating: 5,
    date: "2 недели назад",
    verified: true,
  },
  {
    id: 8,
    name: "Алина Федорова",
    text: "Очень комфортно носить каждый день. Не сковывает движения, приятная ткань.",
    advantages: "Удобная посадка",
    disadvantages: "Цвет отличается от фото",
    rating: 4,
    date: "3 дня назад",
    verified: true,
  },
  {
    id: 9,
    name: "Сергей Павлов",
    text: "Покупкой доволен полностью. Соотношение цена/качество на высоте.",
    advantages: "Простая стирка, не садится",
    disadvantages: "Маленький выбор моделей",
    rating: 5,
    date: "1 неделю назад",
    verified: false,
  },
  {
    id: 10,
    name: "Елена Никитина",
    text: "Заказ пришёл быстро, упаковка целая. Очень приятный на ощупь материал.",
    advantages: "Красиво смотрится",
    disadvantages: "Ткань могла бы быть плотнее",
    rating: 4,
    date: "4 дня назад",
    verified: true,
  },
]);

// Генерация звезд рейтинга
const generateStars = (rating: number) => {
  return Array.from({ length: 5 }, (_, i) => i < rating);
};
</script>

<template>
  <div class="comments-section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Отзывы покупателей</h2>
        <div class="section-subtitle">Что говорят наши клиенты о товаре</div>
      </div>

      <div class="swiper-container">
        <button
          aria-label="Предыдущий слайд"
          class="swiper-button swiper-btn-prev"
          @click="goPrev"
        >
          <Icon
            :name="HeroIcons.ARROW_LEFT_SOLID"
            class="swiper-button--icon"
          />
        </button>
        <Swiper
          class="swiper-wrapper"
          :modules="[Navigation, Autoplay]"
          :autoplay="{ delay: 4000, disableOnInteraction: false }"
          :slides-per-view="4"
          :space-between="24"
          :loop="true"
          :navigation="{
            nextEl: '.swiper-btn-next',
            prevEl: '.swiper-btn-prev',
          }"
          :breakpoints="{
            320: { slidesPerView: 1, spaceBetween: 16 },
            480: { slidesPerView: 1.2, spaceBetween: 16 },
            640: { slidesPerView: 2, spaceBetween: 20 },
            768: { slidesPerView: 2.5, spaceBetween: 20 },
            1024: { slidesPerView: 3, spaceBetween: 24 },
            1280: { slidesPerView: 4, spaceBetween: 24 },
          }"
          @slide-change="onSlideChange"
          @swiper="onSwiper"
        >
          <SwiperSlide
            v-for="comment in comments"
            :key="comment.id"
            class="swiper-slide"
          >
            <div class="comment-card">
              <div class="comment-card__header">
                <div class="user-info">
                  <div class="user-avatar">
                    {{ comment.name.charAt(0) }}
                  </div>
                  <div class="user-details">
                    <div class="user-name">
                      {{ comment.name }}
                      <span
                        v-if="comment.verified"
                        class="verified-badge"
                        title="Проверенный покупатель"
                      >
                        ✓
                      </span>
                    </div>
                    <div class="comment-date">{{ comment.date }}</div>
                  </div>
                </div>

                <div class="rating-display">
                  <div class="stars">
                    <Star
                      v-for="(filled, index) in generateStars(comment.rating)"
                      :key="index"
                      :size="16"
                      :class="['star', filled ? 'filled' : 'empty']"
                    />
                  </div>
                  <div class="rating-value">{{ comment.rating }}/5</div>
                </div>
              </div>

              <div class="comment-card__content">
                <p class="comment-text">{{ comment.text }}</p>

                <div class="pros-cons">
                  <div class="pros">
                    <span class="label positive">👍 Плюсы:</span>
                    <span class="value">{{ comment.advantages }}</span>
                  </div>
                  <div class="cons">
                    <span class="label negative">👎 Минусы:</span>
                    <span class="value">{{ comment.disadvantages }}</span>
                  </div>
                </div>
              </div>

              <div class="comment-card__footer">
                <button class="helpful-btn">
                  <span>Полезно?</span>
                  <span class="count">12</span>
                </button>
                <button class="reply-btn">Ответить</button>
              </div>
            </div>
          </SwiperSlide>
        </Swiper>
        <button
          class="swiper-button swiper-btn-next"
          aria-label="Следующий слайд"
          @click="goNext"
        >
          <Icon
            :name="HeroIcons.ARROW_RIGHT_SOLID"
            class="swiper-button--icon"
          />
        </button>
      </div>
      <BaseButton
        class="comments-section__all-views"
        size="lg"
        :outline="true"
        label="Смотреть все отзывы"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.swiper-button {
  position: absolute;
  top: 50%;

  z-index: 20;

  cursor: pointer;
  padding: 8px 12px;
  background-color: $accent-dark;
  color: #fff;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: $accent;
  }

  &--icon {
    font-size: 26px;
  }
}

.swiper-btn-prev {
  left: -70px;
}

.swiper-btn-next {
  right: -70px;
}

.comments-section {
  padding: 80px 0;
  position: relative;

  &__all-views {
    margin-inline: auto;
  }
}

.section-header {
  text-align: center;
  margin-bottom: 48px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #0f172a 0%, #475569 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 12px;
  letter-spacing: -0.025em;
}

.section-subtitle {
  font-size: 1.125rem;
  color: #64748b;
  font-weight: 500;
}

.swiper-container {
  position: relative;
  margin: 0 -12px;
  padding: 0 12px;
}

.swiper-wrapper {
  padding: 20px 0;
}

.comment-card {
  background: white;
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

.comment-card__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-avatar {
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

.user-details {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-weight: 600;
  color: #0f172a;
  display: flex;
  align-items: center;
  gap: 4px;
}

.verified-badge {
  color: #10b981;
  font-size: 0.875rem;
}

.comment-date {
  font-size: 0.875rem;
  color: #64748b;
}

.rating-display {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.stars {
  display: flex;
  gap: 2px;
}

.star.filled {
  fill: #fbbf24;
  stroke: #fbbf24;
}

.star.empty {
  fill: #e2e8f0;
  stroke: #cbd5e1;
}

.rating-value {
  font-size: 0.875rem;
  font-weight: 600;
  color: #475569;
}

.comment-card__content {
  flex: 1;
  margin-bottom: 20px;
}

.comment-text {
  color: $txt;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 0.9375rem;
}

.pros-cons {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.pros,
.cons {
  display: flex;
  gap: 8px;
  font-size: 0.875rem;
  line-height: 1.5;
}

.label {
  font-weight: 600;
  white-space: nowrap;

  &.positive {
    color: #10b981;
  }

  &.negative {
    color: #ef4444;
  }
}

.value {
  color: #475569;
}

.comment-card__footer {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-top: 16px;
  border-top: 1px solid #f1f5f9;
}

.helpful-btn {
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

  .count {
    font-weight: 600;
    color: #475569;
  }
}

.reply-btn {
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

.view-all-container {
  text-align: center;
  margin-top: 40px;
}

@media (max-width: 768px) {
  .comments-section {
    padding: 48px 0;
  }

  .section-title {
    font-size: 2rem;
  }

  .swiper-button {
    display: none;
  }

  .swiper-container {
    margin: 0;
    padding: 0;
  }

  .comment-card {
    padding: 20px;
  }
}
</style>
