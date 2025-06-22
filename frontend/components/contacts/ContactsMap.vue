<script setup>
import {
  YandexMap,
  YandexMapControls,
  YandexMapDefaultFeaturesLayer,
  YandexMapDefaultSchemeLayer,
  YandexMapZoomControl,
  YandexMapMarker,
} from "vue-yandex-maps";
import { ref } from 'vue';

const map = ref(null);

defineProps({
  mobHeight: {
    type: String,
    default: "500px",
  },
  tabHeight: {
    type: String,
    default: "500px",
  },
  lapHeight: {
    type: String,
    default: "600px",
  },
  deskHeight: {
    type: String,
    default: "600px",
  },
  mapWidth: {
    type: String,
    default: "59.8732",
  },
  mapLongitude: {
    type: String,
    default: "30.3301",
  },
});

// Кастомная цветовая схема "Cyber Dark"
const mapTheme = {
  theme: 'dark',
  features: {
    pmap: {
      colors: {
        generic: '#0a0a0a',     // Основной фон
        road: '#2a2a2a',        // Дороги
        text: '#e0e0e0',        // Текст
        water: '#121212',       // Вода
        poi: '#ff4757',         // Точки интереса (красный)
        area: '#1a1a1a',        // Зоны
        transit: '#3d3d3d',     // Транспорт
      },
      styles: {
        road: {
          width: 1.5,
          glow: {
            color: '#00fffc',
            radius: 1
          }
        }
      }
    }
  }
};
</script>

<template>
  <section 
    v-if="mapLongitude && mapWidth" 
    class="base-map"
    :style="{
      '--mob-height': mobHeight,
      '--tab-height': tabHeight,
      '--lap-height': lapHeight,
      '--desk-height': deskHeight
    }"
  >
    <ClientOnly>
      <YandexMap
        v-model="map"
        :settings="{
          ...mapTheme,
          coordorder: 'latlong',
          location: {
            center: [parseFloat(mapLongitude), parseFloat(mapWidth)],
            zoom: 15,
          },
          showScaleInCopyrights: true,
          behaviors: ['drag', 'dblClickZoom', 'multiTouch'],
          className: 'base-map__map',
          controls: [],
        }"
        width="100%"
        height="100%"
      >
        <YandexMapDefaultSchemeLayer />
        <YandexMapDefaultFeaturesLayer>
          <YandexMapControls :settings="{ position: 'right' }">
            <YandexMapZoomControl />
          </YandexMapControls>
          
          <YandexMapMarker
            :settings="{
              coordinates: [parseFloat(mapLongitude), parseFloat(mapWidth)],
            }"
          >
            <div class="base-map__marker">
              <Icon 
                name="fluent:location-28-filled" 
                class="marker-icon" 
              />
              <div class="pulse-effect"></div>
            </div>
          </YandexMapMarker>
        </YandexMapDefaultFeaturesLayer>
      </YandexMap>
    </ClientOnly>
  </section>
</template>

<style lang="scss" scoped>
.base-map {
  width: 100%;
  height: var(--mob-height);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
  background: #000;

  @media (min-width: 768px) {
    height: var(--tab-height);
  }
  @media (min-width: 1024px) {
    height: var(--lap-height);
  }
  @media (min-width: 1280px) {
    height: var(--desk-height);
  }

  &__map {
    border-radius: 0 !important;
  }

  &__marker {
    position: relative;
    font-size: 2.5rem;
    color: #00fffc;
    filter: 
      drop-shadow(0 0 8px #00fffc80)
      drop-shadow(0 0 16px #00fffc40);
    z-index: 1;

    .pulse-effect {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: #00fffc;
      border-radius: 50%;
      opacity: 0.4;
      transform: scale(0);
      animation: pulse 2s infinite;
      z-index: -1;
    }
  }
}

:deep(.ymaps-2-1-79-copyright__content) {
  filter: invert(1) brightness(2);
}

@keyframes pulse {
  0% {
    transform: scale(0.5);
    opacity: 0.4;
  }
  70% {
    transform: scale(1.5);
    opacity: 0;
  }
  100% {
    transform: scale(1.9);
    opacity: 0;
  }
}
</style>