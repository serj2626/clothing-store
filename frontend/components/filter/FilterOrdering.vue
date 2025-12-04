<script setup lang="ts">
const orderingList = [
  { id: 1, title: "По умолчанию" },
  { id: 2, title: "По цене" },
  { id: 3, title: "По популярности" },
  { id: 4, title: "По рейтингу" },
];
</script>

<template>
  <FilterContent title="Сортировать">
    <ul class="filter-ordering">
      <li
        v-for="item in orderingList"
        :key="item.id"
        class="filter-ordering__item"
      >
        {{ item.title }}
      </li>
    </ul>
  </FilterContent>
</template>
<style scoped lang="scss">
.filter-ordering {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: max-content;

  &__item {
    cursor: pointer;
    padding: 5px 40px;
    font-size: 15px;
    transition: all 0.3s ease-in-out;

    &:hover {
      background-color: $accent;
    }
  }
}
</style>
