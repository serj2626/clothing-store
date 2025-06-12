<script setup lang="ts">
import { contactsPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
const { data: contactsInfo } = useNuxtData("contacts-info");
</script>
<template>
  <div class="contacts-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="contactsPageBreadcrumbs" />
      <ContactsMap
        :map-width="contactsInfo.latitude[0].value"
        :map-longitude="contactsInfo.longitude[0].value"
        style="margin-block: 50px"
      />
      <div class="contacts-page__content">
        <h4 class="contacts-page__content-title">Связаться с нами</h4>
        <div class="contacts-page__content-list">
          <div class="contacts-page__content-list-social">
            <p class="contacts-page__content-list-social-title">
              В социальных сетях
            </p>
            <span class="contacts-page__content-list-social-value">
              <a :href="contactsInfo.insta[0].value"
                ><Icon name="social:insta" size="20"
              /></a>
              <a :href="contactsInfo.tg[0].value"
                ><Icon name="social:tg" size="20"
              /></a>
            </span>
          </div>
          <div class="contacts-page__content-list-phone">
            <p class="contacts-page__content-list-phone-title">По телефону</p>
            <span
              v-for="(phone, index) in contactsInfo.phone"
              :key="index"
              class="contacts-page__content-list-phone-value"
            >
              {{ phone.value }}
            </span>
          </div>
          <div class="contacts-page__content-list-mail">
            <p class="contacts-page__content-list-mail-title">По почте</p>
            <span
              v-for="(mail, index) in contactsInfo.mail"
              :key="index"
              class="contacts-page__content-list-mail-value"
              >{{ mail.value }}
            </span>
          </div>
          <div class="contacts-page__content-list-office">
            <p class="contacts-page__content-list-office-title">Наш офис</p>
            <span>{{ contactsInfo.address[0].value }}</span>
          </div>
        </div>
      </div>
      <BaseFormSubscribe style="margin-inline: auto" />
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

      &-social {
        display: flex;
        flex-direction: column;
        gap: 20px;
        &-value {
          display: flex;
          align-items: center;
          gap: 10px;

          span {
            cursor: pointer;
          }
        }
      }

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
