// Создание Nuxt.js плагина с помощью defineNuxtPlugin
export default defineNuxtPlugin(() => {
  // Получаем runtime конфиг приложения (переменные из nuxt.config.ts)
  const config = useRuntimeConfig();
  const auth = useAuthStore();

  // Создаем кастомный экземпляр $fetch с настройками
  const apiFetch = $fetch.create({
    // Базовый URL для всех запросов берется из конфига
    baseURL: config.public.apiUrl,

    // Хук, срабатывающий перед отправкой запроса
    onRequest({ request, options, response, error }) {
      // Закомментированная альтернативная настройка URL для SSR/CSR
      // options.baseURL = import.meta.server ? config.ssrApiUrl : config.public.browserApiUrl

      // Логирование запросов в debug режиме
      if (config.public.isDebug) {
        console.log("making req", options.baseURL, request.toString());
      }

      // Получаем access-токен из хранилища (Pinia, localStorage и т.д.)
      const token = auth.accessToken; // или: useCookie('access_token').value

      // Добавляем Bearer Token в заголовки, если он есть
      if (token) {
        options.headers = {
          ...options.headers,
          Authorization: `Bearer ${token}`,
        };
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
