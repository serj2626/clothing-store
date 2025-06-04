<template></template>
<script setup lang="ts">
import { api } from "~/api";

const { $api } = useNuxtApp();
const route = useRoute();
const mediaUrl = useRuntimeConfig().public.mediaUrl + "/media/";

export interface ISeoMeta {
  og_image: string;
  seo_title: string;
  seo_description: string;
  og_title: string;
  og_description: string;
  canonical: string;
  is_no_index: boolean;
  is_no_follow: boolean;
}


const { data } = await useAsyncData<ISeoMeta>(
  "seo",
  () => $api(api.seo.url(route.path.slice(1))),
  {
    watch: [() => route.path],
  }
);

const title = computed(() => {
  return data.value?.seo_title ? data.value?.seo_title + " - PAVEL POLA" : "PAVEL POLA"
})

const robotsContent = computed(() => {
  const robotsContent: string[] = [];
  if (data.value?.is_no_follow) robotsContent.push("nofollow");
  if (data.value?.is_no_index) robotsContent.push("noindex");

  return robotsContent.join(", ");
});
useSeoMeta({
  title: () => data.value?.seo_title || title.value,
  description: () => data.value?.seo_description || "",
  ogTitle: () => data.value?.og_title || title.value,
  ogDescription: () => data.value?.og_description || "",
  ogImage: () => (data.value?.og_image ? mediaUrl + data.value?.og_image : ""),
});
useHead({
  link: [
    {
      rel: "canonical",
      href: data.value?.canonical,
    },
  ],
  meta: [
    {
      name: "robots",
      content: robotsContent,
    },
  ],
});
</script>
