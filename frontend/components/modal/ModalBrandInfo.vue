<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IBrandProduct } from "~/types";

const modalsStore = useModalsStore();
const { activeModals } = storeToRefs(modalsStore);
const brandProps = computed<IBrandProduct>(() =>
  activeModals.value.get("brand")
);
</script>

<template>
  <div class="modal-brand-info">
    <div class="modal-brand-info__content">
      <div class="modal-brand-info__top">
        <p class="modal-brand-info__top-brand-title">{{ brandProps.name }}</p>
        <Icon
          class="modal-brand-info__top-brand-icon"
          :name="HeroIcons.COMPANY_SOLID"
          size="40"
        />
      </div>

      <div class="modal-brand-info__main">
        <p class="brand-description">
          {{ brandProps.description || "Описание отсутствует" }}
        </p>
      </div>

      <div class="modal-brand-info__footer">
        <div class="brand-country">
          <span class="country-label">Страна: </span>
          <span class="country-value">{{
            brandProps.country || "не указана"
          }}</span>
        </div>
      </div>

      <BaseButtonClose
        class="modal-brand-info__close"
        :size="24"
        top="15px"
        right="15px"
        @click="modalsStore.closeModal('brand')"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-brand-info {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: $white;
  border-radius: $btn_radius;
  box-shadow: 0 10px 25px rgba($black, 0.2);
  width: 90%;
  max-width: 500px;
  border: 1px solid rgba($accent, 0.3);
  overflow: hidden;
  animation: slideUp 0.4s $default_cubic;
  z-index: 1000;

  &__content {
    position: relative;
    padding: 60px 30px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  &__top {
    margin-top: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    &-brand-title {
      font-family: $ff_title;
      font-size: 24px;
      color: $accent-dark;
      margin: 0;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba($accent, 0.3);
    }

    &-brand-icon {
      color: $accent;
    }
  }

  &__main {
    .brand-description {
      font-family: $ff_second;
      font-size: 16px;
      line-height: 1.5;
      color: $txt;
      margin: 0;
    }
  }

  &__footer {
    .brand-country {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      font-family: $ff_second;

      .country-label {
        font-weight: 600;
        color: $accent-dark;
      }

      .country-value {
        color: $txt;
      }
    }
  }
  &__close {
    color: $accent-dark;
    background-color: rgb(0, 0, 0);
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 10px;
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translate(-50%, calc(-50% + 20px));
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%);
  }
}

// Адаптивность
@media (max-width: $tablet) {
  .modal-brand-info {
    &__content {
      padding: 30px 20px 20px;
    }

    &__top {
      .brand-title {
        font-size: 20px;
      }
    }

    &__main {
      .brand-description {
        font-size: 14px;
      }
    }
  }
}
</style>
