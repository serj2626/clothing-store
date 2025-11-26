<script setup lang="ts">
const { isOpen = false } = defineProps<{ isOpen?: boolean }>();

// Плавная анимация открытия/закрытия
function onEnter(el: HTMLElement) {
  el.style.height = "0";
  el.style.opacity = "0";
  el.style.overflow = "hidden";

  const fullHeight = el.scrollHeight > 350 ? 350 : el.scrollHeight;

  requestAnimationFrame(() => {
    el.style.transition =
      "height 0.6s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.5s ease";
    el.style.height = fullHeight + "px";
    el.style.opacity = "1";
  });
}

function onAfterEnter(el: HTMLElement) {
  el.style.height = el.scrollHeight > 350 ? "350px" : "auto";
  el.style.overflow = el.scrollHeight > 350 ? "auto" : "visible";
}

function onLeave(el: HTMLElement) {
  const fullHeight = el.scrollHeight > 350 ? 350 : el.scrollHeight;
  el.style.height = fullHeight + "px";
  el.style.opacity = "1";
  el.style.overflow = "hidden";

  requestAnimationFrame(() => {
    el.style.transition =
      "height 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s ease";
    el.style.height = "0";
    el.style.opacity = "0";
  });
}
</script>

<template>
  <div
    class="base-accordion-component"
    :class="{ 'base-accordion-component_open': isOpen }"
  >
    <div class="base-accordion-component__summary">
      <slot name="summary" />
    </div>

    <Transition
      name="accordion"
      @enter="onEnter"
      @after-enter="onAfterEnter"
      @leave="onLeave"
    >
      <div v-show="isOpen" class="base-accordion-component__content">
        <slot name="content" />
      </div>
    </Transition>
  </div>
</template>

<style scoped lang="scss">
.base-accordion-component {
  display: flex;
  flex-direction: column;
  width: 100%;
  cursor: pointer;

  &__content {
    overflow: hidden;
    // max-height: 150px;
    transition: height 0.6s ease, opacity 0.5s ease;
    scrollbar-width: thin;
    scrollbar-color: $accent transparent;


    @include mediaTablet {
      max-height: 200px;
    }

    @include mediaLaptop {
      max-height: 250px;
    }

    &::-webkit-scrollbar {
      width: 6px;
    }

    &::-webkit-scrollbar-thumb {
      background: $text-secondary;
      border-radius: 4px;
    }
  }
}

/* Эффект плавного появления */
.accordion-enter-active,
.accordion-leave-active {
  transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.accordion-enter-from,
.accordion-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
