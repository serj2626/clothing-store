<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const isDragging = ref(false)
const startX = ref(0)
const startY = ref(0)
const translateX = ref(0)
const translateY = ref(0)

const parallaxImage = ref<HTMLElement | null>(null)

// Обработчик начала перетаскивания
const startDrag = (e: MouseEvent | TouchEvent) => {
  isDragging.value = true
  const clientX = e instanceof MouseEvent ? e.clientX : e.touches[0].clientX
  const clientY = e instanceof MouseEvent ? e.clientY : e.touches[0].clientY
  
  startX.value = clientX - translateX.value
  startY.value = clientY - translateY.value
  
  document.body.style.cursor = 'grabbing' // Меняем курсор
}

// Обработчик перемещения
const drag = (e: MouseEvent | TouchEvent) => {
  if (!isDragging.value) return
  
  const clientX = e instanceof MouseEvent ? e.clientX : e.touches[0].clientX
  const clientY = e instanceof MouseEvent ? e.clientY : e.touches[0].clientY
  
  translateX.value = clientX - startX.value
  translateY.value = clientY - startY.value
  
  if (parallaxImage.value) {
    parallaxImage.value.style.transform = `translate3d(${translateX.value}px, ${translateY.value}px, 0)`
  }
}

// Обработчик окончания перетаскивания
const endDrag = () => {
  isDragging.value = false
  document.body.style.cursor = '' // Возвращаем курсор
}

// Добавляем/удаляем обработчики
onMounted(() => {
  if (parallaxImage.value) {
    parallaxImage.value.addEventListener('mousedown', startDrag)
    parallaxImage.value.addEventListener('touchstart', startDrag, { passive: false })
  }
  document.addEventListener('mousemove', drag)
  document.addEventListener('touchmove', drag, { passive: false })
  document.addEventListener('mouseup', endDrag)
  document.addEventListener('touchend', endDrag)
})

onUnmounted(() => {
  if (parallaxImage.value) {
    parallaxImage.value.removeEventListener('mousedown', startDrag)
    parallaxImage.value.removeEventListener('touchstart', startDrag)
  }
  document.removeEventListener('mousemove', drag)
  document.removeEventListener('touchmove', drag)
  document.removeEventListener('mouseup', endDrag)
  document.removeEventListener('touchend', endDrag)
})
</script>

<template>
  <div class="parallax-container">
    <div
      ref="parallaxImage"
      class="parallax-image"
      :style="{ transform: `translate3d(${translateX}px, ${translateY}px, 0)` }"
    ></div>
  </div>
</template>

<style scoped lang="scss">
.parallax-container {
  height: 70vh;
  overflow: hidden;
  position: relative;
  touch-action: none; /* Отключаем стандартное поведение касаний */
}

.parallax-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 120%;
  background-size: cover;
  background-position: center;
  will-change: transform;
  cursor: grab; /* Курсор "рука" */
  user-select: none; /* Запрет выделения текста */
  background-image: url("store.jpg");
  
  &:active {
    cursor: grabbing; /* Курсор при перетаскивании */
  }
}
</style>