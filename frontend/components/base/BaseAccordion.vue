<script setup>
defineProps({
  isOpen: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["update:isOpen"]);

const toggle = () => {
  emit("update:isOpen");
};
</script>
<template>
  <div class="accordion" :class="{ accordion_open: isOpen }" @click="toggle">
    <div class="accordion__summary">
      <slot name="summary" />
    </div>
    <div class="accordion__content">
      <slot name="content" />
    </div>
  </div>
</template>
<style lang="scss" scoped>
.accordion {
  display: flex;
  flex-direction: column;
  padding: 10px;
  width: 100%;
  cursor: pointer;
  position: relative;

  // &::before {
  //   content: "";
  //   position: absolute;
  //   left: 0;
  //   top: 0;
  //   bottom: 0;
  //   width: 3px;
  //   background: $accent-dark;
  //   transform: scaleY(.08);
  //   transition: transform 0.3s ease;
  // }

  &__content {
    overflow: hidden;
    max-height: 0;
    color: rgb(96, 94, 94);
    font-size: 15px;

    padding-top: 0;
    transition: max-height 0.2s cubic-bezier(0, 1, 0, 1), padding-top 0.2s ease;
  }

  &_open {
    // &::before {
    //   transform: scaleY(1);
    // }
    &:deep(.accordion__content) {
      padding-right: 30px;
      max-height: 1000px;
      padding-top: 15px;
      transition: max-height 0.2s cubic-bezier(1, 0, 1, 0),
        padding-top 0.2s ease;
    }
  }
}
</style>
