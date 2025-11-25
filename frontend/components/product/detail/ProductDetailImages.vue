<script setup lang="ts">
const { currentImg, allImages } = defineProps<{
  currentImg: string;
  allImages: { id: number | string; image: string }[];
}>();

defineEmits(["check-new-image"]);
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

    <div class="product-detail-images__main">
      <div
        class="product-detail-images__main-bg"
        :style="{ backgroundImage: `url(${getMedia(currentImg ?? '')})` }"
      />
    </div>
  </div>
</template>
<style scoped lang="scss">
.product-detail-images {
  display: grid;
  grid-template-columns: 150px 1fr;
  height: 650px;

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
  // display: flex;
  // align-items: center;
  // justify-content: center;

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
</style>
