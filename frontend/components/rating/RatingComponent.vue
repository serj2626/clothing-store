<script setup lang="ts">
const {
  maxRating = 5,
  readOnly = false,
  size = "lg",
} = defineProps<{
  maxRating?: number;
  readOnly?: boolean;
  size?: "sm" | "md" | "lg";
}>();

const rating = defineModel<number>("ratingValue");

const hoverRating = ref(0);

const setRating = (value: number) => {
  if (readOnly) return;
  rating.value = value;
  // emit("update:modelValue", value);
};

const setHoverRating = (value: number) => {
  if (readOnly) return;
  hoverRating.value = value;
  
};

const resetHoverRating = () => {
  if (readOnly) return;
  hoverRating.value = 0;
};
</script>

<template>
  <div
    class="rating-component"
    :class="[
      `rating-component__size-${size}`,
      { 'rating-component__is-readonly': readOnly },
    ]"
  >
    <span
      v-for="(star, index) in maxRating"
      :key="index"
      class="rating-component__star"
      :class="{
        'rating-component__star-is-active': star <= (hoverRating || rating),
        'rating-component__star-is-hover': star <= hoverRating && !readOnly,
      }"
      @click="setRating(star)"
      @mouseover="setHoverRating(star)"
      @mouseleave="resetHoverRating"
    >
      <Icon name="ph:star-fill" class="rating-component__star-icon" />
    </span>
  </div>
</template>

<style lang="scss" scoped>
.rating-component {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  margin-block: 20px 50px;

  &__size-sm {
    .rating-component__star {
      width: 20px;
      height: 20px;

      .rating-component__star-icon {
        font-size: 20px;
      }
    }
  }

  &__size-md {
    .rating-component__star {
      width: 24px;
      height: 24px;

      .rating-component__star-icon {
        font-size: 24px;
      }
    }
  }

  &__size-lg {
    .rating-component__star {
      width: 28px;
      height: 28px;

      .rating-component__star-icon {
        font-size: 28px;
      }
    }
  }

  &__star {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: rgba($txt, 0.2);
    transition: $default_transition;
    position: relative;

    &-icon {
      transition: $default_transition;
    }

    &-is-active {
      color: $accent-dark;
    }

    &-is-hover {
      transform: scale(1.1);
    }

    &:hover:not(.rating-component__star-is-active) {
      color: rgba($accent, 0.5);
    }
  }

  &__is-readonly {
    .rating-component__star {
      cursor: default;

      &:hover {
        transform: none;
      }
    }
  }
}
</style>
