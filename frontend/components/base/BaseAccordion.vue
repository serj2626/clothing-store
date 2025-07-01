<script setup lang="ts">
const { isOpen = false } = defineProps<{ isOpen?: boolean }>();
</script>
<template>
  <div
    class="base-accordion-component"
    :class="{ 'base-accordion-component_open': isOpen }"
  >
    <div class="base-accordion-component__summary">
      <slot name="summary" />
    </div>
    <div class="base-accordion-component__content">
      <slot />
    </div>
  </div>
</template>
<style lang="scss" scoped>
.base-accordion-component {
  display: flex;
  flex-direction: column;
  width: 100%;
  background-color: var(--bg-color-accordion);
  padding: 15px 15px 15px 30px;
  border-radius: 15px;
  border: 1px solid rgba(#e0bea2, 0.4);
  cursor: pointer;

  &__content {
    overflow: hidden;
    max-height: 0;
    transition: max-height 0.5s cubic-bezier(0, 1, 0, 1);
  }

  &_open {
    transition: all 0.3s ease-in;
    box-shadow: 0 5px 15px $accent;
    gap: 15px;
    &:deep(.base-accordion-component__content) {
      max-height: 1000px;
      transition: max-height 0.3s cubic-bezier(1, 0, 1, 0);
    }
  }
}
</style>
