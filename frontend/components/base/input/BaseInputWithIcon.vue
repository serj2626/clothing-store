<script setup lang="ts">
import type { MaskInputOptions } from 'maska';
import { HeroIcons } from '~/assets/icons/types/hero-icons';

type TInputTypes =
  | 'button'
  | 'checkbox'
  | 'color'
  | 'date'
  | 'datetime-local'
  | 'email'
  | 'file'
  | 'hidden'
  | 'image'
  | 'month'
  | 'number'
  | 'password'
  | 'radio'
  | 'range'
  | 'reset'
  | 'search'
  | 'submit'
  | 'tel'
  | 'text'
  | 'time'
  | 'url'
  | 'week';

interface IInputProps {
  placeholder?: string;
  error?: string;
  maskOptions?: MaskInputOptions;
  type?: TInputTypes;
  icon: string;
}

const inputValue = defineModel('inputValue');

const props = defineProps<IInputProps>();

const showPassword = ref(false);

const currentType = computed(() => {
  if (props.type === 'password' && showPassword.value) {
    return 'text';
  }
  return props.type;
});

</script>
<template>
  <label class="base-input-with-icon">
    <span class="base-input-with-icon__icon" title="Найти">
      <Icon class="base-input-with-icon__icon-img" :name="icon" size="18" />
    </span>
    <input
      v-model="inputValue"
      v-maska="maskOptions"
      :placeholder="placeholder"
      :class="{ 'base-input-with-icon__input_error': error }"
      :type="currentType"
      class="base-input-with-icon__input"
    />

    <Icon
      v-if="type === 'password'"
      :name="showPassword ? HeroIcons.EYE_CLOSE: HeroIcons.EYE"
      size="20"
      class="base-input-with-icon__show"
      @click="showPassword = !showPassword"
    />
  </label>
</template>
<style lang="scss" scoped>
.base-input-with-icon {
  position: relative;
  display: flex;
  align-items: stretch;
  width: 100%;
  background-color: #e9ecef;

  &__show{
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    color: $txt;
    opacity: 0.7;
    cursor: pointer;
  }

  &__input {
    flex: 1 1 auto;
    width: 100%;
    padding: 8px 12px;
    background-color: #fff;
    font-size: 15px;
    outline: 1px solid #d6e3e3;
    color: $txt;
    // transition: all $default_ease;

    &:focus {
      outline: 1px solid green;
      border-radius: 5px;
    }

    &::placeholder {
      height: 100%;
      display: flex;
      align-items: center;
    }
  }
  &:focus-within &__icon-img {
    transform: scale(1.2);
  }

  &__icon {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px 12px;
    outline: 1px solid #d6e3e3;
    // transition: scale $fast_ease;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
    
    &-img {
      color: #2125298c;
      transition: all 0.5s ease;
    }

    &:active {
      .base-input-with-icon__icon-img {
        scale: 1.2;
      }
    }
  }
}

.base-input-with-icon__input:focus {
  .base-input-with-icon__icon {
    background-color: red;
  }
}
</style>
