<script lang="ts" setup>

</script>
<template>
  <div class="modal-block-item">
    <div class="modal-clock-item__wraper">
      <slot />
    </div>
  </div>
</template>
<style lang="scss" scoped>
.modal-block-item {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);

  border-radius: 10px;
  box-shadow: 0 0 10px 10px rgba(0, 0, 0, 0.158);
  min-width: 330px;
  background-color: $white;

  &__wraper {
    position: relative;
    color: $txt;

    &::before {
      content: "";
      position: absolute;
      top: -2px;
      left: 50%;
      transform: translateX(-50%) rotate(45deg);
      width: 20px;
      height: 20px;
      background-color: $white;
      box-shadow: 0 0 20px rgb(240, 241, 241);
    }
  }
}
</style>
