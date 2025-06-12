<script setup lang="ts">
interface Condition {
  icon: string;
  text: string;
}

const conditions = ref<Condition[]>([
  {
    icon: "conditions:one",
    text: "если заказ не был использован и сохранил товарный вид(в том числе не нарушены бирки, ярлыки, упаковочные материалы)",
  },
  {
    icon: "conditions:two",
    text: "возврат и обмен осуществляется в течение двух дней с момента получения заказа",
  },
  {
    icon: "conditions:three",
    text: "возврат и обмен товара возможен только при отправке по Украине",
  },
  {
    icon: "conditions:four",
    text: "бланк возврата присутствует в каждой посылке",
  },
  {
    icon: "conditions:five",
    text: "все расходы по обмену и возврату товара несет покупатель",
  },
  {
    icon: "conditions:six",
    text: "после получения возврата мы делаем перевод денежных средств на карту клиента",
  },
]);
</script>
<template>
  <div class="return-content">
    <p class="return-content__title">Обмен и возврат</p>
    <p class="return-content__text">
      Если вам не подошел заказ, мы с удовольствием вам его обменяем или примем
      возврат
    </p>
    <p class="return-content__conditions">
      Обмен и возврат возможен в случае :
    </p>
    <div class="return-content__conditions-list">
      <div
        v-for="(condition, index) in conditions"
        :key="index"
        class="return-content__conditions-list-item"
      >
        <div class="return-content__conditions-list-item-icon">
          <Icon :name="condition.icon" size="30" />
        </div>
        <p class="return-content__conditions-list-item-text">
          {{ condition.text }}
        </p>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.return-content {
  &__title {
    @include title_page;
  }
  &__text {
    margin-bottom: 10px;
  }
  &__conditions {
    margin-bottom: 20px;

    &-list {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 30px;
      &-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;

        &-icon {
        }

        &-text {
          flex: 1;
          text-align: center;
        }
      }
    }
  }
}
</style>
