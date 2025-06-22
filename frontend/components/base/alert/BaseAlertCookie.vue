<script lang="ts" setup>
const cookieConsent = useCookie<boolean>('store-cookie', {
  default: () => false,
  maxAge: 60 * 120
})

const showAlert = ref(!cookieConsent.value)

function hideAlert() {
  cookieConsent.value = true
  showAlert.value = false
}
</script>
<template>
  <div v-if="showAlert" class="alert-cookie container">
    <p class="alert-cookie__text">
      Наш магазин использует файлы cookie для улучшения взаимодействия с сайтом.
      Продолжая просмотр страниц сайта, вы соглашаетесь с использованием файлов
      cookie.
      <NuxtLink to="/cookie" class="alert-cookie__text-link">Подробнее</NuxtLink>
    </p>
    <BaseButton
      class="alert-cookie__btn"
      size="md"
      color="#cca88a"
      label="Понятно"
      @click="hideAlert"
    />
  </div>
</template>
<style scoped lang="scss">
.alert-cookie {
  position: fixed;
  bottom: 20px;
  left: 50%;
  z-index: 120;
  transform: translateX(-50%);
  height: auto;

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;

  padding: 15px;
  border-radius: 10px;
  background-color: $white;
  box-shadow: 0 16px 48px 0 rgba(0, 0, 0, 0.46);

  @include mediaTablet{
    flex-direction: row;
  }

  &__text {
    color: $txt;
    font-size: 14px;

    @include mediaTablet {
      font-size: 16px;
    }
  }

  &__text-link {
    color: blue;
  }

  &:deep(.base-button){
    padding-inline: 60px;
  }

  &__btn {
    width: 100%;
    font-size: 14px;
    @include mediaMobile {
      width: auto;
    }
    @include mediaTablet {
      font-size: 16px;
    }
  }
}
</style>
