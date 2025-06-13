<script setup lang="ts">
const emit = defineEmits(['intersect']);

const observerRef = ref(null);

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        emit('intersect');
      }
    },
    { threshold: 0.1 }
  );

  if (observerRef.value) {
    observer.observe(observerRef.value);
  }

  onBeforeUnmount(() => {
    observer.disconnect();
  });
});
</script>

<template>
  <div ref="observerRef" style="height: 1px; width: 100%"></div>
</template>