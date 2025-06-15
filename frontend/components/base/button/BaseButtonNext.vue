<script setup lang="ts">
defineProps<{
  currentPage: number;
  totalPages: number;
}>();

const emit = defineEmits(["page-changed"]);
</script>
<template>
  <button
    class="base-button-next"
    :disabled="currentPage === totalPages"
    @click="emit('page-changed', currentPage + 1)"
  >
    <svg
      width="16"
      height="16"
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M9 6L15 12L9 18"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
  </button>
</template>
<style scoped lang="scss">
.base-button-next {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  border: 1px solid #e0e0e0;
  background-color: $white;
  color: $txt;
  cursor: pointer;
  transition: $default_transition;

  &:hover:not(:disabled) {
    border-color: $accent;
    color: $accent-dark;
    background-color: rgba($accent, 0.1);
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  svg {
    stroke: currentColor;
  }
}
</style>
