<script setup lang="ts">
const { currentImg, allImages } = defineProps<{
  currentImg: string;
  allImages: { id: number | string; image: string }[];
}>();

defineEmits(["check-new-image"]);

const showZoom = ref(false);
const lensX = ref(0);
const lensY = ref(0);

/**
 * Функция, которая
 * @param {MouseEvent} e - Событие мыши.
 * @returns {void} - Изменяет значения lensX и lensY.
 */
function moveLens(e: MouseEvent) {
  const container = e.currentTarget as HTMLElement;
  const rect = container.getBoundingClientRect();

  // координаты мыши внутри блока
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  // проценты для background-position
  lensX.value = (x / rect.width) * 100;
  lensY.value = (y / rect.height) * 100;
}


</script>
<template>
  <div class="product-detail-images">
    <div class="product-detail-images__thumbnails">
      <div
        v-for="image in allImages"
        :key="image.id"
        class="product-detail-images__thumbnails-item"
        :class="{ active: currentImg === image.image }"
        @click="$emit('check-new-image', image.image)"
      >
        <NuxtImg
          :src="getMedia(image.image ?? '')"
          format="webp"
          loading="lazy"
          quality="30"
          class="product-detail-images__thumbnails-item-img"
        />
      </div>
    </div>

    <div
      class="product-detail-images__main"
      data-clickable
      @mousemove="
        moveLens;
        showZoom = true;
      "
      @mouseenter="showZoom = true"
      @mouseleave="showZoom = false"
      @touchstart.prevent="console.log('touchstart')"
      @touchend.prevent="console.log('touchend')"
    >
      <div
        class="product-detail-images__main-bg"
        :style="{ backgroundImage: `url(${getMedia(currentImg ?? '')})` }"
      />
      <!-- <div
        v-if="showZoom"
        class="product-detail-images__main-zoom"
        :style="{
          backgroundImage: `url(${getMedia(currentImg ?? '')})`,
          backgroundPosition: `${lensX}% ${lensY}%`,
          backgroundSize: '200%', // увеличиваем в 2 раза
        }"
      /> -->
    </div>
  </div>

  <div class="img-magnifier-container">
    <img id="myimage" :src="getMedia(currentImg ?? '')" width="600" height="400" alt="Girl" />
  </div>
</template>
<style scoped lang="scss">
.img-magnifier-container {
  position: relative;
}

.img-magnifier-glass {
  position: absolute;
  border: 3px solid #000;
  border-radius: 50%;
  cursor: none;
  /*Set the size of the magnifier glass:*/
  width: 100px;
  height: 100px;
}

.product-detail-images {
  display: grid;
  grid-template-columns: 150px 1fr;
  height: 650px;
  gap: 40px;

  @media (max-width: 768px) {
    grid-template-columns: 80px 1fr;
    height: 500px;
  }

  @media (max-width: 480px) {
    grid-template-columns: 1fr;
    grid-template-rows: auto 1fr;
    height: auto;
    gap: 15px;
  }
}
.product-detail-images__thumbnails {
  display: flex;
  flex-direction: column;
  gap: 12px;
  height: 100%;
  overflow-y: auto;
  padding-right: 8px;

  // Кастомный скроллбар
  &::-webkit-scrollbar {
    width: 4px;
  }

  &::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 2px;
  }

  &::-webkit-scrollbar-thumb {
    background: $accent-dark;
    border-radius: 2px;

    &:hover {
      background: #794545;
    }
  }

  @media (max-width: 480px) {
    flex-direction: row;
    height: 80px;
    overflow-x: auto;
    overflow-y: hidden;
    padding-right: 0;
    padding-bottom: 8px;
  }
}
.product-detail-images__thumbnails-item {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  border: 2px solid transparent;
  transition: all 0.2s ease;
  flex-shrink: 0;
  background-color: $bg;

  &:hover {
    border-color: $accent-dark;
  }

  &.active {
    border-color: $accent-dark;
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
  }

  &-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 6px;
  }

  @media (max-width: 480px) {
    width: 70px;
    height: 70px;
  }
}
.product-detail-images__main {
  height: 100%;
  background-color: $bg;
  position: relative;
  cursor: crosshair;

  &-zoom {
    position: absolute;
    z-index: 1000;
    top: 0;
    left: 100%;
    width: 100%;
    height: 100%;
    background-color: $white;
    cursor: zoom-in;
    border: 1px solid rgba(0, 0, 0, 0.166);
    pointer-events: none;
    border-radius: 8px;
  }

  &-bg {
    width: 100%;
    height: 100%;
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    border-radius: 12px;
    transition: all 0.3s ease;
  }
}
.product-detail-images__main-zoom {
  position: absolute;
  z-index: 1000;
  top: 0;
  left: 100%; // справа от основного изображения
  width: 300px; // ширина лупы
  height: 300px; // высота лупы
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  pointer-events: none;
  background-repeat: no-repeat;
  background-size: 200%; // увеличиваем в 2 раза
}
</style>
