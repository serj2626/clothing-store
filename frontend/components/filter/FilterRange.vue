<script setup lang="ts"></script>
<template>
  <FilterContent title="Цена">
    <div class="filter-range">
      <div class="filter-range__block">
        <p class="filter-range__block-title">От</p>
        <BaseInput placeholder="Мин цена" radius="10px" />
      </div>
      <div class="filter-range__block">
        <p class="filter-range__block-title">До</p>
        <BaseInput placeholder="Макс цена" radius="10px" />
      </div>
    </div>
  </FilterContent>
</template>
<style scoped lang="scss">
.filter-range {
  width: max-content;

  &__block {
    padding: 10px;
    display: flex;
    align-items: center;
    gap: 15px;
    justify-content: space-between;

    &-title {
      font-size: 14px;
      font-weight: 600;
    }
  }
}
</style>
