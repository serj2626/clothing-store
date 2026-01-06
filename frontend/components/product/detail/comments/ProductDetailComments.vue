<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Autoplay } from "swiper/modules";
import type { Swiper as SwiperType } from "swiper";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
import { comments } from "~/api/data/comments";

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
</script>

<template>
  <div class="comments-section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Отзывы покупателей</h2>
        <div class="section-subtitle">Что говорят наши клиенты о товаре</div>
      </div>
      <div class="swiper-container">
        <BaseButtonSwiper
          class="swiper-button swiper-btn-prev"
          type="prev"
          @go-prev="goPrev"
        />
        <Swiper
          class="swiper-wrapper"
          :modules="[Navigation, Autoplay]"
          :autoplay="{
            delay: 4000,
            disableOnInteraction: false,
            pauseOnMouseEnter: true,
          }"
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
            <ProductDetailCommentsCard :comment />
          </SwiperSlide>
        </Swiper>
        <BaseButtonSwiper
          class="swiper-button swiper-btn-next"
          type="next"
          @go-next="goNext"
        />
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
}

.swiper-btn-prev {
  left: -50px;
}

.swiper-btn-next {
  right: -50px;
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

.swiper-slide {
  height: auto;
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
