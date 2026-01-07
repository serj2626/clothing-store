<script lang="ts" setup></script>

<template>
  <div role="navigation" class="pagination__component">
    <PaginationBtn />
    <PaginationBtn label="2" />
    <PaginationBtn label="3" />
    <PaginationBtn label="4" />
    <PaginationBtn label="5" :disabled="true" />
  </div>
</template>
<style scoped lang="scss">
.pagination__component {
  display: flex;
  gap: 10px;
  justify-content: center;
}
</style>
