<script lang="ts" setup>
import { api } from "~/api";
import { policyPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";
const { $api } = useNuxtApp();

interface ILegalInfo {
  title: string;
  content: string;
}

const { data: policyInfo } = await useAsyncData<ILegalInfo>(
  "policy-page-info",
  () => $api(api.legal.policy)
);
</script>
<template>
  <div class="policy-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="policyPageBreadcrumbs" />
      <BaseWysiwyg v-if="policyInfo?.content" :html="policyInfo?.content" />
    </div>
  </div>
</template>
