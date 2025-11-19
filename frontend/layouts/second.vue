<template>
  <div class="second-layout">
    <HeaderComponent />
    <slot />
    <BaseButtonScrollToTop />
    <BaseAlertCookie />
    <ModalComponent />
  </div>
</template>
<style lang="scss">
.second-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  }
</style>