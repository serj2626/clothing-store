<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Избранное", url: "/favorite" },
];
</script>
<template>
  <div class="favorite-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <div class="favorite-page__content">
        <h2 class="favorite-page__content-title">Избранное</h2>
        <div class="favorite-page__content-list">
          <article class="card">
            <div class="card__image">
              <button class="card__image-icon">
                <Icon :name="HeroIcons.HEART" size="24" />
              </button>
              <NuxtImg class="card__image-item" src="/favorites/one.png" />
            </div>

            <div class="card__info">
              <div class="card__info-title">Белая куртка</div>
              <div class="card__info-price">2900 грн</div>
              <div class="card__info-sizes">vsadadad</div>
              <div class="card__info-colors">asdsadsad</div>
            </div>
          </article>
          <article class="card">
            <div class="card__image">
              <button class="card__image-icon">
                <Icon :name="HeroIcons.HEART" size="24" />
              </button>
              <NuxtImg class="card__image-item" src="/favorites/two.png" />
            </div>

            <div class="card__info">
              <div class="card__info-title">Белая куртка</div>
              <div class="card__info-price">2900 грн</div>
              <div class="card__info-sizes">vsadadad</div>
              <div class="card__info-colors">asdsadsad</div>
            </div>
          </article>
          <article class="card">
            <div class="card__image">
              <button class="card__image-icon">
                <Icon :name="HeroIcons.HEART" size="24" />
              </button>
              <NuxtImg class="card__image-item" src="/favorites/three.png" />
            </div>

            <div class="card__info">
              <div class="card__info-title">Белая куртка</div>
              <div class="card__info-price">2900 грн</div>
              <div class="card__info-sizes">vsadadad</div>
              <div class="card__info-colors">asdsadsad</div>
            </div>
          </article>
          <article class="card">
            <div class="card__image">
              <button class="card__image-icon">
                <Icon :name="HeroIcons.HEART" size="24" />
              </button>
              <NuxtImg class="card__image-item" src="/favorites/one.png" />
            </div>

            <div class="card__info">
              <div class="card__info-title">Белая куртка</div>
              <div class="card__info-price">2900 грн</div>
              <div class="card__info-sizes">vsadadad</div>
              <div class="card__info-colors">asdsadsad</div>
            </div>
          </article>
          <article class="card">
            <div class="card__image">
              <button class="card__image-icon">
                <Icon :name="HeroIcons.HEART" size="24" />
              </button>
              <NuxtImg class="card__image-item" src="/favorites/two.png" />
            </div>

            <div class="card__info">
              <div class="card__info-title">Белая куртка</div>
              <div class="card__info-price">2900 грн</div>
              <div class="card__info-sizes">vsadadad</div>
              <div class="card__info-colors">asdsadsad</div>
            </div>
          </article>
          <article class="card">
            <div class="card__image">
              <button class="card__image-icon">
                <Icon :name="HeroIcons.HEART" size="24" />
              </button>
              <NuxtImg class="card__image-item" src="/favorites/three.png" />
            </div>

            <div class="card__info">
              <div class="card__info-title">Белая куртка</div>
              <div class="card__info-price">2900 грн</div>
              <div class="card__info-sizes">vsadadad</div>
              <div class="card__info-colors">asdsadsad</div>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.favorite-page {
  &__content {
    &-title {
      font-size: 20px;
      margin-block: 30px;
    }
    &-list {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 15px;
      margin-bottom: 100px;
    }
  }
}

.card {
  &__info {
    padding-top: 15px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    align-items: center;
    &-price {
      font-weight: 700;
    }
    &-sizes {
      opacity: 0.5;
    }
  }
}

.card__image {
  position: relative;
  width: 100%;
  height: 400px;
  display: block;

  &-icon {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 50px;
    height: 50px;
    border-bottom-left-radius: 25px;
    background-color: $accent;
    display: flex;
    justify-content: center;
    align-items: center;
    color: $white;
  }

  &-item {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
}
</style>
