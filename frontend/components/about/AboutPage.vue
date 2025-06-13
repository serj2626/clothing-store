<script lang="ts" setup>
import { api } from "~/api";
import { aboutPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
const { $api } = useNuxtApp();

interface ILegalInfo {
  title: string;
  content: string;
}

const { data: aboutInfo } = await useAsyncData<ILegalInfo>(
  "about-page-info",
  () => $api(api.legal.aboutcompany)
);
</script>
<template>
  <div class="about-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="aboutPageBreadcrumbs" />
      <BaseWysiwyg v-if="aboutInfo?.content" :html="aboutInfo?.content" />
    </div>
  </div>
</template>
