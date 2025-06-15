<script setup lang="ts">
interface IInputProps {
  placeholder?: string;
  error?: string;
  radius?: string;
}

const inputValue = defineModel<string | number>("textareaValue");

defineProps<IInputProps>();
</script>
<template>
  <label class="textarea-component">
    <textarea
      v-model="inputValue"
      :class="{ 'textarea-component__input--error': error }"
      class="textarea-component__input"
    />
    <span
      v-if="!inputValue"
      class="textarea-component__placeholder"
      :class="{ active: inputValue }"
    >
      {{ placeholder }}
    </span>
    <small v-if="error" class="textarea-component__error">
      {{ error }}
    </small>
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
    opacity: 0.8;

    &.active {
      top: 4px;
      font-size: 11px;
      opacity: 0;
    }
  }

  &__input {
    resize: vertical;
    border: none;
    background-color: transparent;
    padding: 16px 20px;
    width: 100%;
    min-height: 100px;
    max-height: 200px;
    height: 100px;
    border-radius: v-bind(radius);
    border: 1px solid rgba($txt, 0.3);
    transition: all 0.3s ease-in;

    &:focus {
      border-color: #e0bea2;
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
