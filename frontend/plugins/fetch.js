// export default defineNuxtPlugin(() => {
//   const { accessToken, refreshToken } = useAuth();

//   const config = useRuntimeConfig();
//   const apiFetch = $fetch.create({
//     baseURL: config.public.apiUrl,
//     async onRequest({ options }) {
//       // Добавляем access токен в заголовки
//       if (accessToken.value) {
//         options.headers = {
//           ...options.headers,
//           Authorization: `Bearer ${accessToken.value}`,
//         };
//       }
//     },
//     onResponse({ response }) {},
//     async onResponseError({ response }) {
//       if (response.status === 401 && accessToken.value) {
//         try {
//           await refreshToken();
//           return $fetch(response.url, {
//             method: response._data.config?.method,
//             body: response._data.config?.data,
//             headers: {
//               Authorization: `Bearer ${accessToken.value}`,
//             },
//           });
//         } catch {
//           await logout();
//         }
//       }
//     },
//   });
//   // Expose to useNuxtApp().$apiFetch
//   return {
//     provide: {
//       api: apiFetch,
//     },
//   };
// });

// Создание Nuxt.js плагина с помощью defineNuxtPlugin
export default defineNuxtPlugin(() => {
  // Получаем runtime конфиг приложения (переменные из nuxt.config.ts)
  const config = useRuntimeConfig();

  // Создаем кастомный экземпляр $fetch с настройками
  const apiFetch = $fetch.create({
    // Базовый URL для всех запросов берется из конфига
    baseURL: config.public.apiUrl,

    // Хук, срабатывающий перед отправкой запроса
    onRequest({ request, options, response, error }) {
      // Закомментированная альтернативная настройка URL для SSR/CSR
      // options.baseURL = import.meta.server ? config.ssrApiUrl : config.public.browserApiUrl

      // Логирование запросов в debug режиме
      if (config.public.debug) {
        console.log("making req", options.baseURL, request.toString());
      }
    },

    // Хук для обработки успешных ответов (пока пустой)
    onResponse({ response }) {},

    // Хук для обработки ошибок ответов (пока пустой)
    onResponseError({ response }) {},
  });

  // Экспортируем созданный apiFetch в контекст Nuxt приложения
  return {
    provide: {
      api: apiFetch, // Доступ через useNuxtApp().$api
    },
  };
});
