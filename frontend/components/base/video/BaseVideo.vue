<script setup lang="ts">


interface IVideoComponentProps {
  video: IBaseMediaProperty | any;
}

defineProps<IVideoComponentProps>();

const elButtonPlay = ref<HTMLElement>();
const elVideo = ref<HTMLVideoElement>();
const isPlaying = ref<boolean>();

const handlePlayVideo = () => {
  if (elVideo.value && elButtonPlay.value) {
    elVideo.value.play();
    elButtonPlay.value.style.display = "none";

    setTimeout(() => {
      if (elButtonPlay.value) {
        elButtonPlay.value.style.display = "block";
      }
    }, convertToMiliseconds(elVideo.value.duration));
  }
};
</script>
<template>
  <div class="video-component">
    <CommonButtonVideoPlay
      v-show="!isPlaying"
      @click="handlePlayVideo"
      ref="elButtonPlay"
      class="video-component-button"
    />
    <video
      @ended="isPlaying = false"
      @play="isPlaying = true"
      :controls="isPlaying"
      ref="elVideo"
      class="video-component-video"
      playsinline
    >
      <source :src="video.contentUrl" :type="video?.mimeType || 'video/mp4'" />
    </video>
  </div>
</template>

<style lang="scss" scoped>
.video-component {
  position: relative;
  border-radius: 30px;
  height: 385px;

  &-button {
    z-index: $z-index-after-content;
    @include positionCenterVericalHorizontal($position: absolute);
  }

  &-video {
    border-radius: inherit;
    height: inherit;
    object-fit: cover;
    width: 100%;
  }

  @include mediaTablet {
    height: 295px;
  }

  @include mediaDesktop {
    height: 500px;
  }
}
</style>
