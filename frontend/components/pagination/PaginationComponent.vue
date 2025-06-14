<script setup lang="ts">
// Демо-данные для макета
const props = defineProps({
  currentPage: {
    type: Number,
    default: 3
  },
  totalPages: {
    type: Number,
    default: 10
  },
  maxVisible: {
    type: Number,
    default: 5
  }
});

const emit = defineEmits(['page-changed']);

// Вычисляемые свойства для отображения
const showFirstDots = computed(() => props.currentPage > 3);
const showLastDots = computed(() => props.currentPage < props.totalPages - 2);

const visiblePages = computed(() => {
  const pages = [];
  const half = Math.floor(props.maxVisible / 2);
  let start = Math.max(props.currentPage - half, 1);
  let end = Math.min(start + props.maxVisible - 1, props.totalPages);
  
  if (end - start + 1 < props.maxVisible) {
    start = Math.max(end - props.maxVisible + 1, 1);
  }
  
  for (let i = start; i <= end; i++) {
    pages.push(i);
  }
  
  return pages;
});

// Метод для изменения страницы
const changePage = (page) => {
  if (page < 1 || page > props.totalPages || page === props.currentPage) return;
  emit('page-changed', page);
};
</script>
<template>
  <div class="pagination">
    <button 
      class="pagination-arrow prev" 
      :disabled="currentPage === 1"
      @click="changePage(currentPage - 1)"
    >
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M15 18L9 12L15 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
    
    <div class="pagination-pages">
      <button 
        v-if="showFirstDots" 
        class="pagination-dots"
        @click="changePage(1)"
      >...</button>
      
      <button 
        v-for="page in visiblePages" 
        :key="page" 
        class="pagination-page"
        :class="{ active: page === currentPage }"
        @click="changePage(page)"
      >
        {{ page }}
      </button>
      
      <button 
        v-if="showLastDots" 
        class="pagination-dots"
        @click="changePage(totalPages)"
      >...</button>
    </div>
    
    <button 
      class="pagination-arrow next" 
      :disabled="currentPage === totalPages"
      @click="changePage(currentPage + 1)"
    >
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M9 6L15 12L9 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  </div>
</template>
<style scoped lang="scss">
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 2rem;
  font-family: $ff_second;
}

.pagination-arrow {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  border: 1px solid #e0e0e0;
  background-color: $white;
  color: $txt;
  cursor: pointer;
  transition: $default_transition;
  
  &:hover:not(:disabled) {
    border-color: $accent;
    color: $accent-dark;
    background-color: rgba($accent, 0.1);
  }
  
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  
  svg {
    stroke: currentColor;
  }
}

.pagination-pages {
  display: flex;
  gap: 0.25rem;
}

.pagination-page {
  min-width: 36px;
  height: 36px;
  padding: 0 0.5rem;
  border-radius: 8px;
  border: 1px solid transparent;
  background-color: transparent;
  color: $txt;
  font-family: $ff_second;
  font-size: 0.95rem;
  cursor: pointer;
  transition: $default_transition;
  
  &:hover:not(.active) {
    background-color: rgba($accent, 0.1);
    color: $accent-dark;
  }
  
  &.active {
    background-color: $accent;
    color: $white;
    border-color: $accent;
    font-weight: 500;
  }
}

.pagination-dots {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-family: $ff_second;
  cursor: pointer;
  
  &:hover {
    color: $accent-dark;
  }
}

@media (max-width: $tablet) {
  .pagination {
    gap: 0.25rem;
  }
  
  .pagination-page {
    min-width: 32px;
    height: 32px;
  }
  
  .pagination-arrow {
    width: 32px;
    height: 32px;
  }
}
</style>