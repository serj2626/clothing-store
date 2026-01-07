<script lang="ts" setup>
const { label = "1", disabled = false } = defineProps<{
  label?: string;
  disabled?: boolean;
}>();
</script>

<template>
  <button :disabled="disabled" class="pagination__btn">{{ label }}</button>
</template>

<style scoped lang="scss">
.pagination__btn {
  background-color: $accent;
  color: $txt;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease;
  line-height: 40px;
  text-align: center;

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  &:hover {
    background-color: $accent-dark;
  }
}
</style>
