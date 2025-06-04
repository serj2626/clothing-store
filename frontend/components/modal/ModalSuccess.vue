<script setup lang="ts">
const modalsStore = useModalsStore();

interface IData {
  title: string;
  description?: string;
}

const data: IData = modalsStore.activeModals.get("success");

function closeToast() {
  setTimeout(() => {
    modalsStore.closeModal("success");
  }, 2500);
}

onMounted(() => {
  closeToast();
});
</script>
<template>
  <div class="modal-success modal-success_active">
    <p>✅ {{ data.title }}</p>
  </div>
</template>

<style scoped lang="scss">
.modal-success {
  position: fixed;
  top: 20px;
  right: 50px;
  background-color: #4caf50;
  color: white;
  padding: 14px 20px;
  border-radius: 8px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
  font-size: 16px;
  font-weight: 600;
  z-index: 9999;

  &_active {
    animation: fade-in 0.5s ease-in-out forwards;
  }
}

@keyframes fade-in {
  from {
    opacity: 0;
    transform: translate(100%, 50%);
  }
  to {
    opacity: 1;
    transform: translate(0, 50%);
  }
}
</style>
