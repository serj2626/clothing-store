<!-- <script setup lang="ts">
import { ref } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Navigation, Thumbs, FreeMode } from 'swiper/modules'

// CSS
import 'swiper/css'
import 'swiper/css/free-mode'
import 'swiper/css/navigation'
import 'swiper/css/thumbs'

const thumbsSwiper = ref(null)

const images = [
  '/favorites/one.png',
  '/favorites/two.png',
  '/favorites/three.png',
  '/favorites/one.png',
  '/favorites/two.png',
  '/favorites/three.png'
]

const onThumbsSwiper = (swiper: any) => {
  thumbsSwiper.value = swiper
}
</script>

<template>
  <div class="product-gallery">
    <Swiper
      class="thumbs-swiper"
      direction="vertical"
      :spaceBetween="10"
      :slidesPerView="4"
      :freeMode="true"
      :watchSlidesProgress="true"
      :modules="[FreeMode, Thumbs]"
      @swiper="onThumbsSwiper"
    >
      <SwiperSlide v-for="(img, idx) in images" :key="idx">
        <img :src="img" alt="preview" />
      </SwiperSlide>
    </Swiper>

    <Swiper
      class="main-swiper"
      :thumbs="{ swiper: thumbsSwiper }"
      :navigation="true"
      :modules="[Navigation, Thumbs]"
    >
      <SwiperSlide v-for="(img, idx) in images" :key="idx">
        <img :src="img" alt="main" />
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<style scoped lang="scss">
.product-gallery {
  display: flex;
  gap: 20px;
  align-items: flex-start;

  .thumbs-swiper {
    width: 100px;
    height: 500px;

    .swiper-slide {
      height: auto !important;
    }

    img {
      width: 100%;
      cursor: pointer;
      border: 2px solid transparent;
      transition: border-color 0.2s;

      &:hover {
        border-color: #e0bea2;
      }
    }
  }

  .main-swiper {
    flex: 1;

    img {
      width: 100%;
      height: auto;
      object-fit: contain;
    }
  }
}
</style>
 -->





 <script setup lang="ts">
// Create 10 slides
const containerRef = ref(null)
const slides = ref(Array.from({ length: 10 }))

const swiper = useSwiper(containerRef)

onMounted(() => {
  // Access Swiper instance
  // Read more about Swiper instance: https://swiperjs.com/swiper-api#methods--properties
  console.log(swiper.instance)
})
</script>

<template>
  <ClientOnly>
    <swiper-container ref="containerRef">
      <swiper-slide
        v-for="(slide, idx) in slides"
        :key="idx"
        style="background-color: rgb(32, 233, 70); color: white;"
      >
        Slide {{ idx + 1 }}
      </swiper-slide>
    </swiper-container>
  </ClientOnly>

  <!-- Go back one slide -->
  <button @click="swiper.prev()">
    Prev
  </button>
  <!-- Go forward one slide -->
  <button @click="swiper.next()">
    Next
  </button>
</template>

<style lang="css">
swiper-slide {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
  height: 20vh;
  font-size: 4rem;
  font-weight: bold;
  font-family: 'Roboto', sans-serif;
}
</style>