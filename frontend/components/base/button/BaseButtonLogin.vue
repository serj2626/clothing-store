<script lang="ts" setup>
const showFormLogin = ref<boolean>(false);
</script>
<template>
  <div class="base-button-login" style="position: relative">
    <BaseButton
      class="base-button-login__btn"
      label="Войти"
      size="sm"
      color="gray"
      @click="showFormLogin = !showFormLogin"
    />
    <LazyBaseFormLogin v-if="showFormLogin" @close="showFormLogin = false" />
  </div>
</template>
<style lang="scss">
.base-button-login__btn {
  box-shadow: 0 0 10px white;
}
.header_active {
  .base-button-login__btn {
    color: $txt;
    background-color: rgba(0, 0, 0, 0.06);
    // transition: background-color $default_ease;
    box-shadow: 0 0 20px rgb(169, 164, 164);
    &:hover {
      background-color: rgba(0, 0, 0, 0.082);
    }
  }
}
</style>
