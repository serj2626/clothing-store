<script setup>
import {
  YandexMap,
  YandexMapControls,
  YandexMapDefaultFeaturesLayer,
  YandexMapDefaultSchemeLayer,
  YandexMapZoomControl,
  YandexMapMarker,
} from "vue-yandex-maps";
const map = shallowRef(null);

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
</script>

<template>
  <section v-if="mapLongitude && mapWidth" class="base-map">
    <ClientOnly>
      <YandexMap
        v-model="map"
        :settings="{
          coordorder: 'latlong',
          location: {
            center: [parseFloat(mapLongitude), parseFloat(mapWidth)],
            zoom: 15,
          },
          showScaleInCopyrights: true,
          behaviors: ['drag', 'dblClick'],
          theme: 'dark',
          className: 'base-map__map',
          // camera: {tilt: 45 * (Math.PI / 180), azimuth: 30 * (Math.PI / 180)}
        }"
        width="100%"
        height="100%"
      >
        <YandexMapDefaultSchemeLayer />
        <YandexMapDefaultFeaturesLayer>
          <yandex-map-controls :settings="{ position: 'right' }">
            <yandex-map-zoom-control />
          </yandex-map-controls>
          <YandexMapMarker
            :settings="{
              coordinates: [parseFloat(mapLongitude), parseFloat(mapWidth)],
            }"
            position="translate(-36%, -72%)"
          >
            <div class="base-map__map-marker">
              <Icon
                name="fluent-color:location-ripple-24"
                class="base-map__map-marker-icon"
              />
            </div>
          </YandexMapMarker>
        </YandexMapDefaultFeaturesLayer>
      </YandexMap>
    </ClientOnly>
  </section>
</template>

<style lang="scss" scoped>
.__ymap_container {
  height: 100%;
  background-color: #292626;
}

.base-map {
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.24);
  border-radius: 10px;
  position: relative;
  width: 100%;
  height: v-bind(mobHeight);
  background-color: black; // Устанавливаем черный фон для карты

  @include mediaTablet {
    height: v-bind(tabHeight);
  }

  @include mediaLaptop {
    height: v-bind(lapHeight);
  }

  @include mediaDesktop {
    height: v-bind(deskHeight);
  }

  &__map {
    // Убираем скругления углов карты
    border-radius: 0 !important;
    overflow: hidden;

    &-marker {
      font-size: 40px;
      @include mediaTablet {
        font-size: 44px;
      }
      @include mediaLaptop {
        font-size: 54px;
      }
    }
  }
}

.base-map__map {
  border-radius: 0 !important; // Убираем скругления
  overflow: hidden;
}
</style>
