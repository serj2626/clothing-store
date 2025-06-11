<script lang="ts" setup>
import { api } from "./api";
import type { IContactsResponse } from "./types";
const { $api } = useNuxtApp();

await useAsyncData<Record<string, IContactsResponse[]>>(
  "contacts-info",
  () => $api(api.contacts.list),
  {
    transform: (data: IContactsResponse[]) => {
      const res: Record<string, IContactsResponse[]> = {};
      for (const key of data) {
        if (key.type in res) {
          res[key.type].push(key);
        } else {
          res[key.type] = [key];
        }
      }
      return res;
    },
    server: true,
    lazy: false,
    staleTime: 360,
  }
);
</script>
<template>
  <NuxtLayout>
    <NuxtLoadingIndicator />
    <NuxtPage />
  </NuxtLayout>
  <BaseSeoMeta />
</template>
<style>
.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>
