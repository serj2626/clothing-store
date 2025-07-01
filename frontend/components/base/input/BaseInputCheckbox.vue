<script lang="ts" setup>
defineProps<{
  label: string;
  disabled?: boolean;
}>();

const agreeValue = defineModel<boolean>("agreeValue");
</script>

<template>
  <div
    class="base-input-checkbox"
    :class="{ 'is-checked': agreeValue, 'is-disabled': disabled }"
  >
    <input
      id="brand-check"
      v-model="agreeValue"
      type="checkbox"
      class="base-input-checkbox__input"
      :disabled="disabled"
    />
    <label for="brand-check" class="base-input-checkbox__label">
      <span class="base-input-checkbox__checkmark">
        <svg
          width="15"
          height="14"
          viewBox="0 0 12 10"
          class="base-input-checkbox__checkmark-icon"
        >
          <path d="M1 5L4.5 8.5L11 1" stroke-width="2" stroke-linecap="round" />
        </svg>
      </span>
      <span class="base-input-checkbox__text">
        {{ label }}
      </span>
    </label>
  </div>
</template>

<style lang="scss" scoped>
.base-input-checkbox {
  display: inline-flex;
  align-items: center;
  position: relative;
  cursor: pointer;
  user-select: none;
  margin-bottom: 10px;

  &__input {
    position: absolute;
    opacity: 0;
    height: 0;
    width: 0;

    &:focus-visible ~ .base-input-checkbox__label .base-input-checkbox__checkmark {
      box-shadow: 0 0 0 3px rgba($accent, 0.2);
      border-color: $accent;
    }
  }

  &__label {
    display: flex;
    align-items: center;
    gap: 12px;
    padding-left: 2px;
  }

  &__checkmark {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 25px;
    height: 25px;
    border: 1px solid $accent;
    border-radius: 4px;
    background-color: orange;
    transition: var(--transition);
    flex-shrink: 0;

    .base-input-checkbox:hover & {
      border-color: blue;
    }

    .is-checked & {
      background-color: var(--primary);
      border-color: var(--primary);
    }

    .is-disabled & {
      background-color: var(--disabled);
      border-color: var(--disabled);
    }
  }

  &__checkmark-icon {
    opacity: 0;
    stroke: $white;
    stroke-dasharray: 18;
    stroke-dashoffset: 18;
    transition: var(--transition);

    .is-checked & {
      opacity: 1;
      stroke-dashoffset: 0;
      transition: opacity 0.1s ease, stroke-dashoffset 0.3s $default_cubic;
    }
  }

  &__text {
    font-size: 15px;
    line-height: 1.4;
    color: var(--color-text);
    transition: var(--transition);
    font-weight: 400;

    .is-disabled & {
      color: var(--disabled-text);
    }
  }

  &.is-disabled {
    cursor: not-allowed;
  }

  @media (hover: hover) {
    &:hover:not(.is-disabled) {
      .base-input-checkbox__checkmark:not(.is-checked) {
        border-color: $accent-dark;
      }
    }
  }
}
</style>
