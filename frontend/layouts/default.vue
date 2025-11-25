<template>
  <div class="layout-default">
    <HeaderComponent />
    <main>
      <slot />
    </main>
    <FooterComponent />
    <BaseButtonScrollToTop />
    <BaseAlertCookie />
    <ModalComponent />
  </div>
</template>
<style lang="scss">
.layout-default {
  min-height: 100vh;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
main {
  flex-grow: 1;
}
</style>
