export const api = {
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  legal: {
    policy: "/legal/policy/", //Получает политику
    oferta: "/legal/offerta/", //Получает оферту
    aboutcompany: "/legal/about-company/", //Получает информацию о компании
    cookiepolicy: "/legal/cookie-policy/", //Получает политику cookie
    exchange: "/legal/exchange-and-return/", // Страница обмена и возврата
  },
  contacts: {
    list: "/contacts/", //Получает контактную информацию
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
    list: (slug: string) => `/products/${slug}/list`, // Возвращает список всех продуктов
    last: "/products/last-collection/", // Возвращает список последних продуктов
    detail: (id: string) => `/products/${id}`, // Возвращает конкретный продукт
    commentsList: (id: string) => `/products/${id}/reviews/list`, // Возвращает список комментарив продукта
    createReview: (id: string) => `/products/${id}/create-review`, // Добавить отзыв к продукту
    like: (id: string) => `/products/${id}/like/`, // Добавить лайк продукту
  },
  users: {
    login: "/users/login/", // Авторизация пользователя
    logout: "/users/logout/", // Выход пользователя
    register: "/users/register/", // Регистрация пользователя
    refresh: "/users/refresh/", // Обновление токена
    detail: "/users/me/", // Возвращает конкретного пользователя
  },
  seo: {
    url: (url: string = "") => `/seo/${url}`, //Возвращает сео для конкретной страницы
  },
};
