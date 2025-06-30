# 🛍️ Документация проекта: Интернет-магазин одежды (Django + Nuxt 3)

![Магазин одежды](/frontend/public/store_screen.png)

## 📌 О проекте

Интернет-магазин одежды с:

- ✅ **Backend на Django** (API, админка, БД)
- ✅ **Frontend на Nuxt 3** (SSR, SEO-оптимизация)
- ✅ **Полная интеграция SEO** (мета-теги, JSON-LD, sitemap)
- ✅ **Корзина, фильтры, адаптивный дизайн**

---

## ⚙️ Технологии

### Backend (Django)

- Python **3.10+**
- Django **4.2+**
- Django REST Framework (**DRF**) – API
- PostgreSQL – база данных
- Django SEO – управление мета-тегами, sitemap
- Django Filters – фильтрация товаров
- Celery + Redis – асинхронные задачи (отправка писем)

### Frontend (Nuxt 3)

- Vue 3 + Composition API
- Pinia – управление состоянием (корзина, избранное)
- @nuxtjs/sitemap – генерация `sitemap.xml`
- UseSeoMeta, UseHead – динамические мета-теги
- SASS – стилизация
- Yandex.Maps – карты
- Swiper – слайдеры
- Google reCAPTCHA – защита от спама
- REplain bot - онлайн консультант
- ThemeSwitcher – темная тема
- @nuxt-alt/auth – аутентификация и авторизация

### DevOps

- Docker
- Docker Compose
- Nginx

---

## 📂 Структура проекта

### Django (backend)

```
backend/
├── config/               # Настройки Django
├── apps/
│   ├── products/         # Товары, категории
│   ├── cart/             # Корзина
│   ├── orders/           # Заказы
│   ├── seo/              # SEO (мета-теги, sitemap)
│   └── users/            # Пользователи, аутентификация
├── static/               # Статика (изображения)
└── manage.py
```

### Nuxt 3 (frontend)

```
frontend/
├── components/
│   ├── seo/              # SEO-компоненты
│   ├── product/          # Карточки товаров
│   └── cart/             # Корзина
├── composables/          # Логика Pinia, API-запросы
├── pages/                # Роуты (главная, товары, корзина)
├── public/               # Статика (лого, favicon)
└── nuxt.config.ts        # Настройки Nuxt
```

---

## 🔧 Установка и запуск

### 1. Backend (Django)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # (Linux/Mac) | venv\Scripts\activate (Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- API: [http://localhost:8000/api/v1](http://localhost:8000/api/)
- Админка: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### 2. Frontend (Nuxt 3)

```bash
cd frontend
npm install
npm run dev
```

- Frontend: [http://localhost:3000](http://localhost:3000)

---

## 🔍 SEO-реализация

### 1. Мета-теги (Django → Nuxt 3)

SEO модель в Django хранит:

- `title`, `description`, `keywords`
- `og:title`, `og:image`, `og:description`
- `canonical_url`, `noindex`, `nofollow`
- `json_ld` (структурированные данные)

### 2. Динамические теги в Nuxt 3

```ts
useSeoMeta({
  title: data.value?.title,
  description: data.value?.description,
  ogImage: data.value?.og_image,
});

useHead({
  script: [{ type: "application/ld+json", innerHTML: data.value?.json_ld }],
});
```

### 3. Sitemap (Django API + Nuxt Sitemap)

Django API (`/api/sitemap/`) отдает:

```json
[
  {
    "slug": "home",
    "priority": 1.0,
    "changefreq": "daily",
    "lastmod": "2024-06-01"
  },
  {
    "slug": "products",
    "priority": 0.8,
    "changefreq": "weekly",
    "lastmod": "2024-05-28"
  }
]
```

Nuxt `@nuxtjs/sitemap` генерирует `sitemap.xml` автоматически.

---

## 🛒 Корзина и заказы

### Pinia (хранилище)

```ts
const cartStore = useCartStore();
cartStore.addToCart(product);
```

### Django API

- `POST /api/cart/add/` – добавить товар
- `GET /api/cart/` – получить корзину
- `POST /api/orders/create/` – оформить заказ

---

## 🚀 Дальнейшее развитие

- Интеграция с платежками (Stripe, LiqPay)
- Реализация поиска (ElasticSearch)
- SSR-кэширование для SEO
- PWA-режим (оффлайн доступ)

---

## 🔗 Ссылки

- [Django Documentation](https://docs.djangoproject.com/)
- [Nuxt 3 Docs](https://nuxt.com/docs)
- [Пример API (Django REST Framework)](https://www.django-rest-framework.org/)
