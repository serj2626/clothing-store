<script setup lang="ts">
import { api } from "~/api";
import { returnPageBreadcrumbs } from "~/assets/data/breadcrumbs.data";

const { $api } = useNuxtApp();

export interface IExchangeReturnResponse {
  id: number;
  title: string;
  created_at: string;
  updated_at: string;
  description: string;
  text: string;
  terms_processes_items: {
    icon: string;
    text: string;
  }[];
}

const { data: exchangeAndReturnInfo } =
  await useAsyncData<IExchangeReturnResponse>("exchange-and-return-page", () =>
    $api(api.legal.exchange)
  );
</script>
<template>
  <div class="return-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="returnPageBreadcrumbs" />
      <ReturnContent
        v-if="exchangeAndReturnInfo"
        v-bind="exchangeAndReturnInfo"
      />
    </div>
  </div>
</template>
