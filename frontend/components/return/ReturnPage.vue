<script setup lang="ts">
import { returnPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
</script>
<template>
  <div class="return-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="returnPageBreadcrumbs" />
      <ReturnContent />
    </div>
  </div>
</template>
