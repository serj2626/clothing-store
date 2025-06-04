<script lang="ts" setup>
import { HeroIcons } from '~/assets/icons/types/hero-icons';
</script>
<template>
  <div class="base-search-component">
    <Icon
      class="base-search-component__wraper-close"
      :name="HeroIcons.CLOSE"
      size="26"
      @click="$emit('close')"
    />
    <div class="base-search-component__wraper">
      <p class="base-search-component__wraper-title">Поиск</p>
      <BaseInputWithIcon
        class="base-search-component__wraper-search"
        type="search"
        placeholder="Поиск в AlfaSMS"
        :icon="HeroIcons.SEARCH"
      />
    </div>
  </div>
</template>
<style scoped lang="scss">
.base-search-component {
  position: absolute;
  z-index: 120;
  top: 50px;
  width: 755px;
  left: -85px;
  transform: translateX(-68%);
  box-shadow: 0 0 10px 10px rgba(0, 0, 0, 0.158);
  background-color: $txt_white;
  border-radius: 10px;

  @include modal_arrow(600px, -3px);

  &__wraper {
    display: flex;
    flex-direction: column;
    position: relative;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px;

    &-close {
      @include btn_close_form;
      z-index: 200;
      color: $bg_footer;
    }
    &-title {
      color: $txt;
      font-size: 18px;
      margin-bottom: 10px;
      font-weight: 700;
    }
    &-search {
      width: 100%;
    }
    &:deep(.base-input-icon__icon){
      order: 1;

    }
  }
}
</style>
