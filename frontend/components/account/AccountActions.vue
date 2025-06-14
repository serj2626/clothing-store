<script setup lang="ts">
import AccountHistoryOrders from "./AccountHistoryOrders.vue";
import AccountLogout from "./AccountLogout.vue";
import AccountFormData from "./form/AccountFormData.vue";
import BaseFormFeedback from "../base/form/BaseFormFeedback.vue";
const currentComponent = ref<"one" | "two" | "three" | "four">("one");

const tabs = {
  one: AccountHistoryOrders,
  two: AccountFormData,
  three: BaseFormFeedback,
  four: AccountLogout,
};
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
      Обратная связь
    </button>
    <button
      class="account-actions__btn"
      :class="{ 'account-actions__btn_active': currentComponent === 'four' }"
      @click="currentComponent = 'four'"
    >
      Выйти
    </button>
  </div>
  <Transition name="fade" mode="out-in">
    <keep-alive>
      <component :is="tabs[currentComponent]" :key="currentComponent" />
    </keep-alive>
  </Transition>
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  scale: 0;
}
</style>
