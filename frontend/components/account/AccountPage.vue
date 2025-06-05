<script setup lang="ts">
const breadcrumbs = [
  { title: "Главная", url: "/" },
  { title: "Личный кабинет", url: "/account" },
];
</script>
<template>
  <div class="account-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <AccountContent />
    </div>
  </div>
</template>
<style scoped lang="scss"></style>
