<script setup lang="ts">
const modalsStore = useModalsStore();
</script>
<template>
  <div class="modal-success">
    <div class="modal-content">
      <div class="modal-icon">
        <svg
          width="64"
          height="64"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM10 17L5 12L6.41 10.59L10 14.17L17.59 6.58L19 8L10 17Z"
            fill="#d38f56"
          />
        </svg>
      </div>
      <h3 class="modal-title">Спасибо за ваш заказ!</h3>
      <p class="modal-message">
        Мы получили вашу заявку и свяжемся с вами в ближайшее время для
        подтверждения.
      </p>
      <BaseButton
        label="Отлично"
        size="md"
        radius="5px"
        @click="modalsStore.closeModal('success')"
      />
      <BaseButtonClose
        top="15px"
        right="20px"
        @click="modalsStore.closeModal('success')"
      />
    </div>
  </div>
</template>
<style scoped lang="scss">
.modal-success {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: $white;
  border-radius: $btn_radius;
  box-shadow: 0 10px 25px rgba($black, 0.2);
  width: 90%;
  max-width: 500px;

  text-align: center;
  animation: slideUp 0.4s $default_cubic;
}

.modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  padding: 2rem;
}

.modal-icon {
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba($accent, 0.1);
  border-radius: 50%;
  padding: 1rem;
}

.modal-title {
  font-family: $ff_title;
  font-size: 1.5rem;
  color: $txt;
  margin: 0;
}

.modal-message {
  font-family: $ff_second;
  color: $txt;
  margin: 0;
  line-height: 1.5;
}

.modal-button {
  font-family: $ff_main;
  background-color: $accent;
  color: $white;
  border: none;
  border-radius: $btn_radius;
  padding: 0.75rem 2rem;
  font-size: 1rem;
  cursor: pointer;
  transition: $default_transition;
  margin-top: 1rem;

  &:hover {
    background-color: $accent-dark;
    box-shadow: $btn-accent-hover-shadow;
  }

  &:active {
    background-color: $btn-accent-active;
    transform: translateY(2px);
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    scale: 0.5;
    transform: translate(-50%, calc(-50% + 20px));
  }
  to {
    opacity: 1;
    scale: 1;
    transform: translate(-50%, -50%);
  }
}

@media (max-width: $tablet) {
  .modal-success {
    padding: 1.5rem;
  }

  .modal-title {
    font-size: 1.3rem;
  }

  .modal-message {
    font-size: 0.9rem;
  }
}
</style>
