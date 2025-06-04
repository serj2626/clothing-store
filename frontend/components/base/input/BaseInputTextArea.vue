<script setup lang="ts">
interface IInputProps {
  placeholder?: string;
  error?: string;
}

const inputValue = defineModel<string | number>("inputValue");

defineProps<IInputProps>();
</script>
<template>
  <label class="textarea-component">
    <textarea
      v-model="inputValue"
      :class="{ 'textarea-component__input--error': error }"
      class="textarea-component__input"
    />
    <span v-if="!inputValue" class="textarea-component__placeholder">{{
      placeholder
    }}</span>
    <small v-if="error" class="textarea-component__error">{{ error }}</small>
  </label>
</template>

<style lang="scss" scoped>
.textarea-component__input:focus {
  .textarea-component__placeholder {
    left: 20px;
  }
}
.textarea-component {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 5px;

  &__placeholder {
    position: absolute;
    left: 20px;
    top: 20px;
  }

  &__input {
    resize: vertical;
    border: none;
    background-color: transparent;
    padding: 16px 20px;
    max-height: 300px;
    min-height: 300px;
    min-width: 100%;
    box-shadow: 10px 14px 20px rgba(252, 252, 252, 0.469);
    border-radius: 5px;

    &:focus {
      outline: none;
    }

    // &--error {
    //   border-bottom: 1px solid $error;
    // }
  }

  &__error {
    color: rgb(255, 0, 0);
    text-transform: uppercase;
    font-weight: 500;
    letter-spacing: 1.5px;
  }
}
</style>
