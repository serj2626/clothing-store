<template>
  <div class="app">
    <HeaderComponent />
    <slot />
    <FooterComponent />
    <BaseButtonScrollToTop />
    <BaseAlertCookie />
    <ModalComponent />
  </div>
</template>
<style lang="scss">
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
