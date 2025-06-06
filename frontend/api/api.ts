export const api = {
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  // specialists: {
  //   list: "/specialists/", //Возвращает всех специалистов
  //   dropdown: "/specialists/dropdown/", //Список всех специалистов для дропдаунов
  //   item: (slug: string): string => `/specialists/${slug}`, // Получить конкретный специалиста по слагу
  // },

  legal: {
    policy: "/legal/policy/", //Получает политику
    oferta: "/legal/offerta/", //Получает оферту
    aboutcompany: "/legal/about-company/", //Получает информацию о компании
    cookiepolicy: "/legal/cookie-policy/", //Получает политику cookie
  },
  contacts: {
    contacts: "/contacts/", //Получает контактную информацию
    feedback: "/contacts/feedback/", //Запрос на создание обратной связи
    footer: "/contacts/footer/", //Запрос на получение данных для футера
    subscription: "/contacts/subscription/", //Запрос на создание подписки
  },
  orders: {
    checkout: "/orders/checkout/", //Запрос на создание заказа
  },
  brands: {
    list: "/products/brands/", //Возвращает список всех брендов
  },
  category: {
    list: "/products/categories/", //Возвращает список всех категорий
    detail: (slug: string) => `/products/categories/${slug}`, //Возвращает конкретную категорию
  },
  products: {
    list: "/products/", //Возвращает список всех продуктов
    detail: (id: string) => `/products/${id}`, //Возвращает конкретный продукт
    like: (id: string) => `/products/${id}/like`, //Возвращает конкретный продукт
  },
  users: {
    login: "/users/login/", // Авторизация пользователя
    register: "/users/register/", // Регистрация пользователя
    refresh: "/users/refresh/", // Обновление токена
    detail: "/users/detail/info", //Возвращает конкретного пользователя
  },
  seo: {
    url: (url: string = "") => `/seo/${url}`, //Возвращает сео для конкретной страницы
  },
};
