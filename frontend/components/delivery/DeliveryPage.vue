<script setup lang="ts">
import { deliveryPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
</script>
<template>
  <div class="delivery-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="deliveryPageBreadcrumbs" />
      <DeliveryContent />
    </div>
  </div>
</template>
