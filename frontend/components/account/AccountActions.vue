<script setup lang="ts">
const currentComponent = ref<"one" | "two" | "three">("one");

// const tabs = {
//   one: TabOne,
//   two: TabTwo,
//   three: TabThree,
// };
</script>
<template>
  <div class="account-actions">
    <button
      class="account-actions__btn"
      :class="{ 'account-actions__btn_active': currentComponent === 'one' }"
      @click="currentComponent = 'one'"
    >
      История заказов
    </button>
    <button
      class="account-actions__btn"
      :class="{ 'account-actions__btn_active': currentComponent === 'two' }"
      @click="currentComponent = 'two'"
    >
      Личные данные
    </button>
    <button
      class="account-actions__btn"
      :class="{ 'account-actions__btn_active': currentComponent === 'three' }"
      @click="currentComponent = 'three'"
    >
      Выйти
    </button>
  </div>
</template>
<style scoped lang="scss">
.account-actions {
  position: relative;
  margin-block: 30px 20px;
  display: flex;
  width: 100%;
  align-items: center;
  border-bottom: 1px solid #6058583d;
  border-top: 1px solid #6058583d;
  justify-content: center;

  &__btn {
    color: $white;
    padding: 15px 50px;
    transition: all 0.5s ease-in;
    background-color: #fff;
    color: $txt;

    &_active {
      background-color: $accent;
      color: $white;
    }

    &:active {
      background-color: $btn-accent-active;
    }
    &:hover {
      box-shadow: $btn-accent-hover-shadow;
    }
  }
}
</style>
