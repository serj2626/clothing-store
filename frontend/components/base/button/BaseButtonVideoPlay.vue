<script setup lang="ts">
// const clinicDirection = useClinicDirection()
</script>
<template>
  <!-- <button
    :class="{'button-video-play-component--kids': !clinicDirection.isAdultClinic}"
    class="button-video-play-component"
    aria-label="Воспроизвести видео"
  >
    <div
      class="button-video-play-component__main"
    >
      <NuxtIcon
        class="button-video-play-component__main-icon"
        name="videoPlay"
        filled
      />
    </div>
  </button> -->
</template>
<style lang="scss" scoped>
.button-video-play-component {
  display: flex;
  justify-self: center;
  align-items: center;
  width: var(--btn-video-play-width, 80px);
  height: var(--btn-video-play-width, 80px);
  border: 1px solid $white;
  border-radius: 15px;
  padding: 6px;

  &--kids {
    .button-video-play-component__main:hover {
      background-color: $kids_accent !important;
    }
  }

  &__main {
    display: flex;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(7.5px);
    background-color: rgba(255, 255, 255, 0.4);
    border-radius: 12px;
    width: 100%;
    height: 100%;

    &-icon {
      width: 25px;

      @include mediaTablet {
        width: 44px;
      }
    }

    @include mediaDesktop {
      border-radius: 15px;
    }
  }

  @include mediaDesktop {
    border-radius: 20px;
  }
}

.button-video-play-component:hover {
  .button-video-play-component__main {
    background-color: $brand_color;
    transition: background-color 0.8s ease;
  }

  .button-video-play-component__main-icon {
    rotate: 120deg;
    transition: rotate 0.8s ease;
  }
}

.button-video-play-component:not(:hover) {
  .button-video-play-component__main {
    background-color: rgba(255, 255, 255, 0.4);
    transition: background-color 0.8s ease;
  }

  .button-video-play-component__main-icon {
    rotate: 0deg;
    transition: rotate 0.8s ease;
  }
}
</style>
