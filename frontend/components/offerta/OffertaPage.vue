<script lang="ts" setup>
import { api } from "~/api";
import { offertaPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";

const { $api } = useNuxtApp();

interface ILegalInfo {
  title: string;
  content: string;
}

const { data: offertaInfo } = await useAsyncData<ILegalInfo>(
  "offerta-page-info",
  () => $api(api.legal.oferta)
);
</script>
<template>
  <div class="offerta-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="offertaPageBreadcrumbs" />
      <BaseWysiwyg v-if="offertaInfo?.content" :html="offertaInfo?.content" />
    </div>
  </div>
</template>
