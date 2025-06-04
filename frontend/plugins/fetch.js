export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig();
  const apiFetch = $fetch.create({
    baseURL: config.public.apiUrl,
    onRequest({ request, options, response, error }) {
      // options.baseURL = import.meta.server ? config.ssrApiUrl : config.public.browserApiUrl
      if (config.public.debug) {
        console.log("making req", options.baseURL, request.toString());
      }
    },
    onResponse({ response }) {},
    onResponseError({ response }) {},
  });
  // Expose to useNuxtApp().$apiFetch
  return {
    provide: {
      api: apiFetch,
    },
  };
});
