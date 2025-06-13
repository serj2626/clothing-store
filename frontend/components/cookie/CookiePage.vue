<script setup lang="ts">
import { api } from "~/api";
import { cookiePageBreadcrumbs } from "~/assets/data/breadcrumbs.data";

const { $api } = useNuxtApp();

interface ILegalInfo {
  title: string;
  content: string;
}

const { data: cookieInfo } = await useAsyncData<ILegalInfo>(
  "cookie-page-info",
  () => $api(api.legal.cookiepolicy)
);
</script>
<template>
  <div class="cookie-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="cookiePageBreadcrumbs" />
      <BaseWysiwyg v-if="cookieInfo?.content" :html="cookieInfo?.content" />
    </div>
  </div>
</template>
<style scoped lang="scss"></style>
