<script setup lang="ts">
import { api } from "~/api";

const { $api } = useNuxtApp();
const route = useRoute();

const currentPath = computed(() =>
  route.path === "/" ? "home" : route.path.slice(1)
);
const mediaUrl = useRuntimeConfig().public.mediaUrl + "/media/";

export interface ISeoMeta {
  id: number;

  title: string;
  description: string;
  keywords: string;

  og_image: string;
  og_title: string;
  og_description: string;

  canonical_url: string;
  noindex: boolean;
  nofollow: boolean;

  json_ld: string;
  priority: number;
  changefreq: string;
  lastmod: string;
}

const { data } = await useAsyncData<ISeoMeta>(
  "seo",
  () => $api(api.seo.url(currentPath.value)),
  {
    watch: [() => route.path],
  }
);

const title = computed(() => {
  return data.value?.title
    ? data.value?.title + " - Clothes Store"
    : "Clothes Store";
});

const robotsContent = computed(() => {
  const robotsContent: string[] = [];
  if (data.value?.nofollow) robotsContent.push("nofollow");
  if (data.value?.noindex) robotsContent.push("noindex");

  return robotsContent.join(", ");
});


useSeoMeta({
  title: () => data.value?.title || title.value,
  keywords: () => data.value?.keywords || "",
  description: () => data.value?.description || "",
  ogTitle: () => data.value?.og_title || title.value,
  ogDescription: () => data.value?.og_description || "",
  ogImage: () => (data.value?.og_image ? mediaUrl + data.value?.og_image : ""),
});
useHead({
  link: [
    {
      rel: "canonical",
      href: data.value?.canonical_url,
    },
  ],
  meta: [
    {
      name: "robots",
      content: robotsContent,
    },
  ],
});

useHead({
  script: data.value?.json_ld
    ? [
        {
          type: "application/ld+json",
          innerHTML: data.value.json_ld,
        },
      ]
    : [],
});
</script>
