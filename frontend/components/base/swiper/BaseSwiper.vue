<script setup lang="ts">
export interface IContactsImage {
  path: string;
  alt: string;
}

const {
  images = [],
  mobileCount = 1,
  mobileBetween = 40,
  tabletCount = 4,
  tabletBetween = 30,
  laptopCount = 6,
  laptopBetween = 20,
  desctopCount = 8,
  desctopBetween = 20,
} = defineProps<{
  images: IContactsImage[];
  mobileCount?: number;
  mobileBetween?: number;
  tabletCount?: number;
  tabletBetween?: number;
  laptopCount?: number;
  laptopBetween?: number;
  desctopCount?: number;
  desctopBetween?: number;
}>();

const containerRef = ref(null);
const swiper = useSwiper(containerRef, {
  slidesPerView: 1,
  spaceBetween: 15,
  loop: true,
  autoplay: {
    delay: 1500,
  },
  breakpoints: {
    0: {
      slidesPerView: mobileCount,
      spaceBetween: mobileBetween,
    },
    768: {
      slidesPerView: tabletCount,
      spaceBetween: tabletBetween,
    },
    1024: {
      slidesPerView: laptopCount,
      spaceBetween: laptopBetween,
    },
    1200: {
      slidesPerView: desctopCount,
      spaceBetween: desctopBetween,
    },
  },
});

onMounted(() => {
  console.log(swiper.instance);
});
</script>

<template>
  <div class="main-partners container">
    <ClientOnly>
      <swiper-container ref="containerRef" :init="false">
        <BaseSwiperSlider
          v-if="Array.isArray(images) && images.length"
          :images="images"
        />
      </swiper-container>
    </ClientOnly>
  </div>
</template>

<style lang="css">
.main-partners {
  padding-block: 48px 140px;
}

swiper-slide {
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  width: 170px;
  height: 45px;
}
</style>
