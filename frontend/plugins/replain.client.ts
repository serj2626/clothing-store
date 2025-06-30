// plugins/replain.client.ts
export default defineNuxtPlugin((nuxtApp) => {
  if (import.meta.client) {
    const config = useRuntimeConfig();

    window.replainSettings = {
      id: config.public.replainId,
    };
    const script = document.createElement("script");
    script.src = "https://widget.replain.cc/dist/client.js";
    script.async = true;

    document.head.appendChild(script);
  }
});
