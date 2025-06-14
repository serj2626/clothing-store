<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
// import { MaskInputOptions } from "maska";

type TInputTypes =
  | "button"
  | "checkbox"
  | "color"
  | "date"
  | "datetime-local"
  | "email"
  | "file"
  | "hidden"
  | "image"
  | "month"
  | "number"
  | "password"
  | "radio"
  | "range"
  | "reset"
  | "search"
  | "submit"
  | "tel"
  | "text"
  | "time"
  | "url"
  | "week";

interface IInputProps {
  placeholder?: string;
  type?: TInputTypes;
  radius?: string;
  animate?: boolean;
  // maskOptions?: MaskInputOptions;
}

const inputValue = defineModel<string>("inputValue");
const error = defineModel<string>("error");
const props = defineProps<IInputProps>();

const showPassword = ref(false);
const isFocused = ref(false);

const currentType = computed(() =>
  props.type === "password" && showPassword.value
    ? "text"
    : props.type ?? "text"
);
</script>

<template>
  <label class="base-input">
    <div class="base-input__wrapper">
      <input
        v-model="inputValue"
        :type="currentType"
        class="base-input__input"
        :class="{ 'base-input__input--error': !!error }"
        @focus="isFocused = true"
        @blur="isFocused = false"
      />
      <span
        class="base-input__placeholder"
        :class="{ active: isFocused  || inputValue }"
      >
        {{ props.placeholder }}
      </span>
      <Icon
        v-if="props.type === 'password'"
        :name="showPassword ? HeroIcons.EYE_CLOSE : HeroIcons.EYE"
        size="20"
        class="base-input__icon"
        @click="showPassword = !showPassword"
      />
    </div>
    <small v-if="error" class="base-input__error">{{ error }}</small>
  </label>
</template>

<style scoped lang="scss">
.base-input {
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: 100%;

  &__wrapper {
    position: relative;
    width: 100%;
  }

  &__input {
    width: 100%;
    padding-block: 16px;
    padding-left: 20px;
    border: 1px solid #25252584;
    font-size: 14px;
    color: $txt;
    background: white;
    border-radius: v-bind(radius);
    transition: border-color 0.3s;

    &:focus {
      border-color: green;
      outline: none;
    }

    &--error {
      border-color: red;
    }
  }

  &__placeholder {
    position: absolute;
    top: 16px;
    left: 16px;
    color: $txt;
    font-size: 14px;
    pointer-events: none;
    transition: 0.5s ease;
    background: white;
    padding: 0 4px;

    &.active {
      top: 4px;
      font-size: 11px;
      opacity: 0;
    }
  }

  &__icon {
    position: absolute;
    top: 50%;
    right: 12px;
    transform: translateY(-50%);
    cursor: pointer;
    opacity: 0.7;
    color: $txt;
  }

  &__error {
    color: red;
    font-size: 12px;
    text-transform: uppercase;
    font-weight: 500;
    letter-spacing: 0.5px;
  }
}
</style>
