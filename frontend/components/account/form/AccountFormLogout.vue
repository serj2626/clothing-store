<script setup lang="ts">
const modalsStore = useModalsStore();
function goBack() {
  useRouter().back();
}
</script>

<template>
  <form class="account-logout">
    <p class="account-logout__text">Вы уверены, что хотите выйти?</p>
    <div class="account-logout__actions">
      <button
        type="button"
        class="account-logout__actions-btn account-logout__actions-btn--yes"
        @click="modalsStore.openModal('logout')"
      >
        Да
      </button>
      <button
        type="button"
        class="account-logout__actions-btn account-logout__actions-btn--no"
        @click="goBack"
      >
        Нет
      </button>
    </div>
  </form>
</template>

<style scoped lang="scss">
.account-logout {
  padding: 30px;
  max-width: 400px;
  margin: 40px auto;
  text-align: center;

  &__text {
    font-size: 18px;
    font-weight: 500;
    color: var(--color-text);
    margin-bottom: 30px;
  }

  &__actions {
    display: flex;
    justify-content: center;
    gap: 20px;

    &-btn {
      padding: 10px 24px;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease-in-out;

      &--yes {
        background-color: $error;
        color: #fff;

        &:hover {
          background-color: #d32f2f;
        }
      }

      &--no {
        background-color: #e0e0e0;
        color: $txt;

        &:hover {
          background-color: #bdbdbd;
        }
      }
    }
  }
}
</style>
