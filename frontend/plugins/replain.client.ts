// plugins/replain.client.ts
export default defineNuxtPlugin((nuxtApp) => {
  if (import.meta.client) {
    const config = useRuntimeConfig();

    // Получаем ID из runtime config
    window.replainSettings = {
      id: config.public.replainId,
      // Это важно: не отображать встроенную кнопку
    };
    const script = document.createElement("script");
    script.src = "https://widget.replain.cc/dist/client.js";
    script.async = true;

    document.head.appendChild(script);
  }
});
