<script setup lang="ts">
import { basketPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
</script>
<template>
  <div class="basket-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="basketPageBreadcrumbs" />
      <BasketContent />
    </div>
  </div>
</template>
