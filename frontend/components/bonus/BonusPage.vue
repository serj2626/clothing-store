<script setup lang="ts">
import { bonusPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
</script>

<template>
  <div class="bonus-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="bonusPageBreadcrumbs" />
      
      <div class="bonus-page__header">
        <h1 class="bonus-page__title">Бонусная программа</h1>
        <p class="bonus-page__subtitle">Копите бонусы и получайте скидки на покупки</p>
      </div>
      
      <div class="bonus-card">
        <div class="bonus-card__info">
          <h2 class="bonus-card__title">Ваш бонусный баланс</h2>
          <div class="bonus-card__amount">1 250 <span>бонусов</span></div>
          <div class="bonus-card__progress">
            <div class="progress-bar">
              <div class="progress-bar__fill" style="width: 62%"></div>
            </div>
            <div class="progress-labels">
              <span>0</span>
              <span>2 000 бонусов</span>
            </div>
          </div>
          <p class="bonus-card__hint">Соберите 2000 бонусов и получите скидку 15% на следующий заказ</p>
        </div>
        <div class="bonus-card__image">
          <img src="/categories/one.png" alt="Бонусная карта" loading="lazy">
        </div>
      </div>
      
      <div class="bonus-rules">
        <h2 class="bonus-rules__title">Как это работает</h2>
        
        <div class="rules-grid">
          <div class="rule-card">
            <div class="rule-card__icon">1</div>
            <h3 class="rule-card__title">Получайте бонусы</h3>
            <p class="rule-card__text">1 бонус = 1 рубль. За каждую покупку начисляем 5% от суммы чека</p>
          </div>
          
          <div class="rule-card">
            <div class="rule-card__icon">2</div>
            <h3 class="rule-card__title">Копите быстрее</h3>
            <p class="rule-card__text">Участвуйте в акциях и получайте дополнительные бонусы</p>
          </div>
          
          <div class="rule-card">
            <div class="rule-card__icon">3</div>
            <h3 class="rule-card__title">Тратьте с умом</h3>
            <p class="rule-card__text">Оплачивайте бонусами до 30% стоимости следующей покупки</p>
          </div>
        </div>
      </div>
      
      <div class="bonus-levels">
        <h2 class="bonus-levels__title">Уровни программы</h2>
        
        <div class="levels-tabs">
          <button class="levels-tab active">Стандарт</button>
          <button class="levels-tab">Премиум</button>
          <button class="levels-tab">VIP</button>
        </div>
        
        <div class="levels-content">
          <div class="level-card">
            <div class="level-card__header">
              <h3 class="level-card__title">Стандарт</h3>
              <p class="level-card__requirement">0-10 000 бонусов</p>
            </div>
            <ul class="level-card__benefits">
              <li>5% бонусов от суммы покупки</li>
              <li>Доступ к обычным акциям</li>
              <li>Бесплатная доставка от 5000₽</li>
            </ul>
          </div>
        </div>
      </div>
      
      <div class="bonus-actions">
        <button class="btn btn--accent">Активировать бонусы</button>
        <button class="btn btn--outline">История начислений</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.bonus-page {
  padding: 40px 0 80px;
  
  &__header {
    text-align: center;
    margin-bottom: 48px;
  }
  
  &__title {
    font-family: $ff_title;
    font-size: 42px;
    font-weight: 700;
    color: $txt;
    margin-bottom: 12px;
    
    @media (min-width: $tablet) {
      font-size: 48px;
    }
  }
  
  &__subtitle {
    font-family: $ff_second;
    font-size: 18px;
    color: rgba($txt, 0.8);
    
    @media (min-width: $tablet) {
      font-size: 20px;
    }
  }
}

.bonus-card {
  background: linear-gradient(135deg, $accent 0%, $accent-dark 100%);
  border-radius: 20px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  color: $white;
  margin-bottom: 48px;
  box-shadow: 0 10px 20px rgba($accent-dark, 0.2);
  
  @media (min-width: $tablet) {
    flex-direction: row;
    align-items: center;
    padding: 40px;
  }
  
  &__info {
    flex: 1;
  }
  
  &__title {
    font-family: $ff_second;
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 16px;
    
    @media (min-width: $tablet) {
      font-size: 24px;
    }
  }
  
  &__amount {
    font-family: $ff_title;
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 24px;
    
    span {
      font-size: 20px;
      font-weight: 400;
    }
    
    @media (min-width: $tablet) {
      font-size: 56px;
    }
  }
  
  &__progress {
    margin-bottom: 16px;
  }
  
  &__hint {
    font-family: $ff_second;
    font-size: 14px;
    opacity: 0.9;
  }
  
  &__image {
    margin-top: 24px;
    text-align: center;
    
    @media (min-width: $tablet) {
      margin-top: 0;
      flex: 0 0 300px;
    }
    
    img {
      max-width: 100%;
      height: auto;
    }
  }
}

.progress-bar {
  height: 8px;
  background: rgba($white, 0.3);
  border-radius: 4px;
  margin-bottom: 8px;
  
  &__fill {
    height: 100%;
    background: $white;
    border-radius: 4px;
    transition: $default_transition;
  }
}

.progress-labels {
  display: flex;
  justify-content: space-between;
  font-family: $ff_second;
  font-size: 12px;
  color: rgba($white, 0.8);
}

.bonus-rules {
  margin-bottom: 60px;
  
  &__title {
    font-family: $ff_title;
    font-size: 32px;
    font-weight: 700;
    color: $txt;
    text-align: center;
    margin-bottom: 40px;
  }
}

.rules-grid {
  display: grid;
  gap: 24px;
  
  @media (min-width: $tablet) {
    grid-template-columns: repeat(3, 1fr);
  }
}

.rule-card {
  background: $white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 5px 15px rgba($black, 0.05);
  transition: $default_transition;
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba($black, 0.1);
  }
  
  &__icon {
    width: 40px;
    height: 40px;
    background: $accent;
    color: $white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: $ff_title;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 16px;
  }
  
  &__title {
    font-family: $ff_second;
    font-size: 18px;
    font-weight: 600;
    color: $txt;
    margin-bottom: 12px;
  }
  
  &__text {
    font-family: $ff_second;
    font-size: 14px;
    color: rgba($txt, 0.7);
    line-height: 1.5;
  }
}

.bonus-levels {
  margin-bottom: 40px;
  
  &__title {
    font-family: $ff_title;
    font-size: 32px;
    font-weight: 700;
    color: $txt;
    text-align: center;
    margin-bottom: 32px;
  }
}

.levels-tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 24px;
  gap: 8px;
}

.levels-tab {
  padding: 12px 24px;
  background: none;
  border: 1px solid rgba($txt, 0.1);
  border-radius: $btn_radius;
  font-family: $ff_second;
  font-size: 14px;
  color: $txt;
  cursor: pointer;
  transition: $default_transition;
  
  &.active {
    background: $accent;
    color: $white;
    border-color: $accent;
  }
  
  &:hover:not(.active) {
    border-color: rgba($txt, 0.3);
  }
}

.level-card {
  background: $white;
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 5px 15px rgba($black, 0.05);
  
  &__header {
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba($txt, 0.1);
  }
  
  &__title {
    font-family: $ff_title;
    font-size: 24px;
    font-weight: 700;
    color: $txt;
    margin-bottom: 8px;
  }
  
  &__requirement {
    font-family: $ff_second;
    font-size: 14px;
    color: rgba($txt, 0.7);
  }
  
  &__benefits {
    list-style: none;
    padding: 0;
    margin: 0;
    
    li {
      font-family: $ff_second;
      font-size: 16px;
      color: $txt;
      padding: 8px 0;
      position: relative;
      padding-left: 24px;
      
      &:before {
        content: "";
        position: absolute;
        left: 0;
        top: 14px;
        width: 8px;
        height: 8px;
        background: $accent;
        border-radius: 50%;
      }
    }
  }
}

.bonus-actions {
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
  
  @media (min-width: $tablet) {
    flex-direction: row;
    justify-content: center;
  }
}

.btn {
  padding: 16px 32px;
  border-radius: $btn_radius;
  font-family: $ff_second;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: $default_transition;
  
  &--accent {
    background: $accent;
    color: $white;
    border: none;
    
    &:hover {
      background: $accent-dark;
      box-shadow: $btn-accent-hover-shadow;
    }
    
    &:active {
      background: $btn-accent-active;
    }
  }
  
  &--outline {
    background: transparent;
    border: 1px solid $accent;
    color: $accent;
    
    &:hover {
      background: rgba($accent, 0.1);
    }
  }
}
</style>