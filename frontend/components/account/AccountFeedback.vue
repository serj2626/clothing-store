<script setup lang="ts">

</script>

<template>
  <form class="account-logout">
    <p class="account-logout__text">Форма обратной связи</p>
  </form>
</template>

<style scoped lang="scss">
.account-logout {
  padding: 30px;
  background-color: $white;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  margin: 40px auto;
  text-align: center;

  &__text {
    font-size: 18px;
    font-weight: 500;
    color: $txt;
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
