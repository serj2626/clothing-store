<script setup lang="ts">
import { api } from "~/api";

const { $api } = useNuxtApp();
const route = useRoute();

const mediaUrl = useRuntimeConfig().public.mediaUrl + "/media/";

const currentPath = computed(() =>
  route.path === "/" ? "home" : route.path.slice(1)
);

export interface ISeoMeta {
  id: number;

  seo_title: string;
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
  { watch: [() => route.path] }
);

const title = "Clothes Store";

const canonicalLink = computed(() =>
  data.value?.canonical_url
    ? [{ rel: "canonical", href: data.value.canonical_url }]
    : []
);

const json_ld = computed(() => data.value?.json_ld || null);

// useHead({
//   link: canonicalLink,
//   script: [
//     {
//       type: "application/ld+json",
//       innerHTML: json_ld,
//     },
//   ],
// });

useSeoMeta({
  title: () => data.value?.seo_title || title,
  keywords: () => data.value?.keywords || "",
  description: () => data.value?.description || "",
  ogTitle: () => data.value?.og_title || title,
  ogDescription: () => data.value?.og_description || "",
  ogImage: () => (data.value?.og_image ? mediaUrl + data.value?.og_image : ""),
  robots: `${data.value?.noindex ? "noindex" : "index"},${
    data.value?.nofollow ? "nofollow" : "follow"
  }`,
});
</script>
