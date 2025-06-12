import { nextTick, onBeforeUnmount, watch } from "vue";

import { useRoute } from "vue-router";

export function useJsonLd(getJsonLd: () => string | undefined | null) {
  const route = useRoute();

  const isClient = typeof window !== "undefined" && typeof document !== "undefined";

  const updateJsonLd = async () => {
    if (!isClient) return;

    await nextTick();

    // Удалить старый тег
    const old = document.querySelector('script[type="application/ld+json"]');
    if (old) old.remove();

    // Добавить новый, если есть содержимое
    const jsonLd = getJsonLd();
    if (jsonLd) {
      const script = document.createElement("script");
      script.type = "application/ld+json";
      script.innerHTML = jsonLd;
      document.head.appendChild(script);
    }
  };

  // Следить за маршрутом и обновлять JSON-LD (только на клиенте)
  if (isClient) {
    watch(() => route.fullPath, updateJsonLd, { immediate: true });

    // Удалить при размонтировании компонента
    onBeforeUnmount(() => {
      const old = document.querySelector('script[type="application/ld+json"]');
      if (old) old.remove();
    });
  }
}
