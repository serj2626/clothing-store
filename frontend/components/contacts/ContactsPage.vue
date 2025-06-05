<script setup lang="ts">
const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Контакты", url: "/contacts" },
];
</script>
<template>
  <div class="contacts-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <div class="contacts-page__content">
        <h4 class="contacts-page__content-title">Связаться с нами</h4>
        <div class="contacts-page__content-list">
          <div class="contacts-page__content-list-social">
            <p class="contacts-page__content-list-social-title">
              В социальных сетях
            </p>
          </div>
          <div class="contacts-page__content-list-phone">
            <p class="contacts-page__content-list-phone-title">По телефону</p>
            <span class="contacts-page__content-list-phone-value"
              >+38(067) 158 82 66</span
            >
            <span class="contacts-page__content-list-phone-value"
              >+38(067) 158 82 66</span
            >
          </div>
          <div class="contacts-page__content-list-mail">
            <p class="contacts-page__content-list-mail-title">По почте</p>
            <span class="contacts-page__content-list-mail-value"
              >example@gmail.com</span
            >
          </div>
          <div class="contacts-page__content-list-office">
            <p class="contacts-page__content-list-office-title">Наш офис</p>
            <span>Санкт-Петербург, ул. Ленсовета д81</span>
          </div>
        </div>
      </div>
      <BaseFormSubscribe />
    </div>
  </div>
</template>
<style scoped lang="scss">
.contacts-page {
  &__content {
    margin-top: 30px;
    margin-bottom: 100px;
    &-title {
      margin-bottom: 30px;
    }
    &-list {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 110px;

      &-phone {
        display: flex;
        flex-direction: column;
        gap: 20px;
        &-value {
          font-weight: 200;
        }
      }
      &-mail {
        display: flex;
        flex-direction: column;
        gap: 20px;
        &-value {
          font-weight: 200;
        }
      }
      &-office {
        display: flex;
        flex-direction: column;
        gap: 20px;
        &-value {
          font-weight: 200;
        }
      }
    }
  }
}
</style>
