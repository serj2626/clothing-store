<script lang="ts" setup>
interface Props {
  title?: string;
  description?: string;
  actionText?: string;
  iconComponent?: Component | null;
}

withDefaults(defineProps<Props>(), {
  title: "Здесь пока пусто",
  description: "Добавьте товары, чтобы они появились здесь",
  actionText: "",
  iconComponent: null,
});

defineEmits(["action"]);
</script>
<template>
  <div class="base-alert-empty-state">
    <slot name="icon">
      <component :is="iconComponent" class="base-alert-empty-state__icon" />
    </slot>
    <h3 class="base-alert-empty-state__title">
      <slot name="title">{{ title }}</slot>
    </h3>
    <p class="base-alert-empty-state__description">
      <slot name="description">{{ description }}</slot>
    </p>
    <slot name="action">
      <BaseButton
        v-if="actionText"
        class="base-alert-empty-state__action"
        :label="actionText"
        @click="$emit('action')"
      />
    </slot>
  </div>
</template>

<style lang="scss" scoped>
.base-alert-empty-state {
  text-align: center;
  padding: 40px 20px;
  background-color: $white;
  border-radius: $btn_radius;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  max-width: 500px;
  margin: 0 auto;

  &__icon {
    width: 80px;
    height: 80px;
    margin-bottom: 20px;
    color: $accent;
  }

  &__title {
    font-family: $ff_title;
    font-size: 22px;
    color: $txt;
    margin-bottom: 10px;
  }

  &__description {
    font-family: $ff_second;
    font-size: 16px;
    color: lighten($txt, 30%);
    margin-bottom: 25px;
  }

  &__action {
    margin: 0 auto;
  }
}
</style>
