<template>
  <div class="comment-item">
    <div class="comment-header">
      <div class="user-info">
        <div class="user-avatar">
          <Icon name="ph:user-circle" />
        </div>
        <div class="user-name">{{ comment.user.name }}</div>
      </div>
      <div class="comment-date">{{ formatDate(comment.created_at) }}</div>
    </div>
    
    <div class="comment-rating">
      <div class="stars">
        <Icon 
          v-for="star in 5"
          :key="star"
          name="ph:star-fill"
          :class="{ 'active': star <= comment.rating }"
        />
      </div>
    </div>
    
    <div class="comment-text">{{ comment.text }}</div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  comment: {
    type: Object,
    required: true
  }
})

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>

<style scoped lang="scss">
.comment-item {
  padding: 20px 0;
  border-bottom: 1px solid rgba($txt, 0.1);
  
  &:last-child {
    border-bottom: none;
  }
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.user-avatar {
  .icon {
    font-size: 32px;
    color: rgba($txt, 0.5);
  }
}

.user-name {
  font-family: $ff_second;
  font-weight: 500;
  color: $txt;
}

.comment-date {
  font-family: $ff_second;
  font-size: 14px;
  color: rgba($txt, 0.5);
}

.comment-rating {
  margin-bottom: 10px;
  
  .stars {
    display: flex;
    gap: 3px;
    
    .icon {
      font-size: 18px;
      color: rgba($txt, 0.2);
      
      &.active {
        color: $accent-dark;
      }
    }
  }
}

.comment-text {
  font-family: $ff_second;
  line-height: 1.5;
  color: $txt;
}
</style>