<script setup lang="ts"></script>
<template>
  <div class="basket-content">
    <h2 class="basket-content__title">Ваш заказ</h2>
    <div class="basket-content__orders-list">
      <OrdersProductCard />
      <OrdersProductCard />
      <OrdersProductCard />
      <OrdersProductCard />
    </div>
    <div class="basket-content__total">
      <span class="basket-content__total-title">К оплате:</span>
      <span class="basket-content__total-value">15250 руб</span>
    </div>
  </div>
</template>
<style scoped lang="scss">
.basket-content {
  margin-bottom: 70px;
  &__title {
    @include title_page;
  }
  &__orders-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  &__total {
    display: flex;
    justify-content: end;
    gap: 15px;
    margin-top: 30px;
    &-value {
      font-weight: 700;
    }
  }
}
</style>
