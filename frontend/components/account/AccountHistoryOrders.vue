<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
interface Order {
  id: number;
  date: string;
  status: string;
  amount: string;
}

const orders: Order[] = [
  { id: 718, date: "28.09.21", status: "Выполнен", amount: "55 320 руб." },
  {
    id: 719,
    date: "29.09.21",
    status: "В процессе",
    amount: "12 890 руб.",
  },
  { id: 720, date: "30.09.21", status: "Отменён", amount: "7 590 руб." },
  { id: 721, date: "01.10.21", status: "Выполнен", amount: "33 300 руб." },
];
</script>
<template>
  <div class="account-history-orders">
    <div class="account-history-orders__content">
      <div
        v-for="order in orders"
        :key="order.id"
        class="account-history-orders__content-item"
      >
        <p class="account-history-orders__content-item-number">
          № {{ order.id }} от {{ order.date }}
        </p>
        <p class="account-history-orders__content-item-status">
          <span class="account-history-orders__content-item-status-title"
            >Статус</span
          >
          <span class="account-history-orders__content-item-status-value">{{
            order.status
          }}</span>
        </p>
        <p class="account-history-orders__content-item-sum">
          <span class="account-history-orders__content-item-sum-title"
            >Сумма</span
          >
          <span class="account-history-orders__content-item-sum-value">{{
            order.amount
          }}</span>
        </p>
        <button style="flex-shrink: 0">
          <Icon style="color: #e0bea2" :name="HeroIcons.DOWN" size="18" />
        </button>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.account-history-orders {
  &__content {
    display: flex;
    flex-direction: column;
    gap: 20px;

    &-item {
      position: relative;
      display: flex;
      align-items: center;

      &::after {
        content: "";
        position: absolute;
        bottom: -15px;
        left: 0;
        width: 100%;
        height: 1px;
        background-color: $txt;
        opacity: 0.3;
      }

      &-number {
        flex-basis: 33.33%;
      }

      &-status {
        display: flex;
        flex-direction: column;
        flex-basis: 33.33%;
        justify-content: start;
        gap: 5px;
        &-value {
          font-weight: 700;
        }
      }
      &-sum {
        display: flex;
        flex-direction: column;
        gap: 5px;
        flex-basis: 33.33%;
        &-value {
          font-weight: 700;
        }
      }
    }
  }
}
</style>
