<script setup lang="ts">
import { accountPageBreadcrumbs } from '~/assets/data/breadcrumbs.data';
</script>
<template>
  <div class="account-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="accountPageBreadcrumbs" />
      <AccountContent />
    </div>
  </div>
</template>
<style scoped lang="scss"></style>
