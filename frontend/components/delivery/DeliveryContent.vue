<script setup lang="ts">
const stages = ref([
  {
    icon: "conditions:stage1",
    text: 'Выбрать в корзине способ оплаты "LIQPAY";',
  },
  {
    icon: "conditions:stage2",
    text: "Подтвердить заказ;",
  },
  {
    icon: "conditions:stage3",
    text: "После этого Вас перенаправит на сайт LIQPAY, где вы выбираете удобный для вас способ оплаты: через Приват24, или с помощью карты Mastercard/VISA со всего мира.",
  },
]);
</script>
<template>
  <div class="delivery-content">
    <p class="delivery-content__title">Оплата и доставка</p>
    <div class="delivery-content__conditions">
      <div class="delivery-content__conditions-item">
        <p class="delivery-content__conditions-item-title">
          Вы можете оплатить покупку одним из ниже перечисленных способов:
        </p>
        <ul class="delivery-content__conditions-list-item-list">
          <li class="delivery-content__conditions-list-item-list-value">
            • наложенным платежом в отделении Новой Почты
          </li>
          <li class="delivery-content__conditions-list-item-list-value">
            • денежным переводом Visa/MasterCard
          </li>
          <li class="delivery-content__conditions-list-item-list-value">
            • полная предоплата через Приват 24
          </li>
        </ul>
      </div>
      <div class="delivery-content__conditions-item">
        <p class="delivery-content__conditions-item-title">
          Мы готовы предложить несколько вариантов доставки:
        </p>
        <ul class="delivery-content__conditions-list-item-list">
          <li class="delivery-content__conditions-list-item-list-value">
            • отправка по всей Украине в отделение Новой Почты(1-2 дня)
          </li>
          <li class="delivery-content__conditions-list-item-list-value">
            • международные сервисы доставки для жителей зарубежья: Укрпочта(
            1-3 недели ,DHL(3-7 дней)
          </li>
          <li class="delivery-content__conditions-list-item-list-value">
            • Срок доставки: 1–2 дня с момента заказа
          </li>
        </ul>
      </div>
    </div>

    <div class="delivery-content__stages-order">
      <p class="delivery-content__stages-order-title">
        Процесс оформления заказа с помощью LIQPAY:
      </p>
      <div class="delivery-content__stages-order-list">
        <div
          v-for="(stage, idx) in stages"
          :key="idx"
          class="delivery-content__stages-order-list-item"
        >
          <Icon
            :name="stage.icon"
            size="100"
            class="delivery-content__stages-order-list-item-icon"
          />
          <p class="delivery-content__stages-order-list-item-text">
            {{ stage.text }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.delivery-content {
  &__title {
    @include title_page;
  }
  &__conditions {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 40px;

    &-item {
      display: flex;
      flex-direction: column;
      gap: 10px;

      &-list {
        list-style: circle;
        display: flex;
        flex-direction: column;
        gap: 5px;
      }
    }
  }
  &__stages-order {
    &-title {
      margin-block: 25px;
    }
    &-list {
      display: flex;
      align-items: center;
      gap: 80px;

      &-item {
        display: flex;
        align-items: center;
        gap: 15px;
      }
    }
  }
}
</style>
