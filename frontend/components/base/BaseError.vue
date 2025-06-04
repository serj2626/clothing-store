<script setup>
defineProps({
  error: {
    type: Object,
    default: null,
    required: true,
  },
})
</script>
<template>
  <div class="error-page container">
    <div class="error-page__bg"></div>
    <div class="error-page__bg-second"></div>

    <div class="error-page__info">
      <h2 class="error-page__title">
        {{ error?.statusCode < 500 ? 'Страница не найдена' : 'Ошибка сервера' }}
      </h2>
      <p class="error-page__status">{{ error?.statusCode }}</p>
      <NuxtLink class="error-page__link" to="/">На главную</NuxtLink>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.error-page {
  position: relative;
  min-height: 90vh;

  &__info {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  &__title {
    // @include txt_europe_ext(24px, 400, 100%, $txt_);
    text-transform: uppercase;
    margin-bottom: 54px;
    min-width: 423px;

    @include mediaTablet {
      // @include txt_europe_ext(28px, 400, 130%, $txt_title);
      margin-bottom: 35px;
    }

    @include mediaLaptop {
      // @include txt_europe_ext(40px, 400, 120%, $txt_title);
      margin-bottom: 31px;
    }
  }
  &__status {
    // @include txt_europe_ext(78px, 400, 110%, $txt_title);
    margin-bottom: 40px;

    @include mediaTablet {
      font-size: 128px;
      margin-bottom: 51px;
    }
    @include mediaLaptop {
      margin-bottom: 46px;
    }
    @include mediaDesktop {
      margin-bottom: 50px;
    }
  }
  &__link {
    // @include txt_mulish(20px, 400, 140%, $txt_review);
    padding-bottom: 5px;
    padding-inline: 10px;
    border-bottom: 1px solid currentColor;
  }

  &__bg {
    // background-image: url('/public/img/error-bg.png');
    background-size: cover;
    background-position: center;

    width: 281px;
    height: 261px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    @include mediaTablet {
      width: 732px;
      height: 680px;
    }
    @include mediaLaptop {
      top: 65%;
      left: 30%;
    }
    @include mediaDesktop {
      left: 25%;
    }
  }

  &__bg-second {
    display: none;

    @include mediaLaptop {
      display: block;
      position: absolute;
      top: 40%;
      right: 80px;
      transform: translateY(-50%);
      width: 434px;
      height: 403px;
      background-image: url('/public/img/error-bg.png');
      background-size: cover;
      background-position: center;
    }

    @include mediaDesktop {
      top: 40%;
      right: 170px;
    }
  }
}
</style>
