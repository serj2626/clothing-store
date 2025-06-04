<template>
  <transition name="fade-modal">
    <div
      v-if="isAnyModalOpen"
      class="modal-wrapper"
      role="dialog"
      @click.self="modalsStore.closeAllModals()"
    >
      <!-- <LazyBaseFormRegister
        v-if="activeModals.has('register')"
        key="register"
      /> -->
      <LazyModalFeedback v-if="activeModals.has('feedback')" key="chat" />
      <LazyModalSuccess v-if="activeModals.has('success')" key="success" />
    </div>
  </transition>
</template>

<script setup>
const modalsStore = useModalsStore();
const { activeModals, isAnyModalOpen } = storeToRefs(modalsStore);
</script>

<style lang="scss" scoped>
.modal-wrapper {
  position: fixed;
  bottom: 0;
  right: 0;
  left: 0;
  top: 0;
  z-index: 110;
  background: rgba(0, 0, 0, 0.47);
}

.fade-modal-enter-active,
.fade-modal-leave-active {
  opacity: 1;
  transition: opacity $default_cubic;
}
.fade-modal-enter-from,
.fade-modal-leave-to {
  opacity: 0;
  transition: opacity $default_cubic;
}

.review-detail-modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
