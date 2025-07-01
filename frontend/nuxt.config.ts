export default defineNuxtConfig({
  compatibilityDate: "2025-05-15",
  devtools: { enabled: true },
  css: ["@/assets/scss/global.scss"],
  modules: [
    "@pinia/nuxt",
    "@nuxt/eslint",
    "@nuxt/icon",
    "@nuxt/image",
    "nuxt-swiper",
    "@nuxtjs/robots",
    "vue-yandex-maps/nuxt",
    "@nuxt-alt/auth",
    "@nuxt-alt/http",
    "unplugin-icons/nuxt",
  ],
  auth: {
    strategies: {
      local: {
        token: false, // 💥 отключаем полностью!
        refreshToken: false,
        user: {
          property: null,
        },
        endpoints: {
          login: { url: "/login/", method: "post" },
          refresh: { url: "/token/refresh/", method: "post" },
          logout: { url: "/logout/", method: "post" },
          user: { url: "/me/", method: "get" },
        },
      },
    },
    watchLoggedIn: true,
    redirect: {
      login: "/login",
      logout: "/",
      home: "/",
    },
  },
  http: {
    baseURL: process.env.NUXT_PUBLIC_API_URL,
    credentials: true, // 💡 обязательно, чтобы куки шли с каждым запросом
  },

  icon: {
    customCollections: [
      { prefix: "social", dir: "./assets/icons/social" },
      { prefix: "actions", dir: "./assets/icons/actions" },
      { prefix: "conditions", dir: "./assets/icons/conditions" },
    ],
  },
  pinia: {
    storesDirs: ["./stores/**"],
  },
  yandexMaps: {
    apikey: process.env.YANDEX_MAP_API_KEY,
    initializeOn: "onComponentMount",
    strictMode: true,
    lang: "ru_RU",
  },
  app: {
    head: {
      script: [
        {
          src: "https://www.google.com/recaptcha/api.js",
          async: true,
          defer: true,
        },
      ],
      title: "Store",
      htmlAttrs: {
        lang: "ru",
      },
      link: [
        {
          rel: "icon",
          type: "image/png",
          href: "/fav/logo.png",
          sizes: "96x96",
        },
        { rel: "icon", type: "image/svg+xml", href: "/public/fav/favicon.svg" },
        { rel: "shortcut icon", href: "/public/fav/favicon.ico" },
        // { rel: 'apple-touch-icon', sizes: '180x180', href: '/public/fav/apple-touch-icon.png' },
        // { rel: 'manifest', href: '/public/fav/site.webmanifest' },
      ],
      meta: [
        { name: "msapplication-TileColor", content: "#da532c" },
        { name: "theme-color", content: "#ffffff" },
        { charset: "UTF-8" },
        { "http-equiv": "X-UA-Compatible", content: "IE=edge" },
        { name: "format-detection", content: "telephone=no" },
        {
          name: "viewport",
          content: "width=device-width, initial-scale=1.0, maximum-scale=5",
        },
        { name: "apple-mobile-web-app-title", content: "pavelpola" },
      ],
    },
    pageTransition: { name: "page", mode: "out-in" },
  },
  runtimeConfig: {
    public: {
      isDebug: process.env.DEBUG,
      replainId: process.env.REPLAIN_ID,
      apiUrl: process.env.API_URL,
      recaptchaKey: process.env.RECAPTCHA_PUBLIC_KEY,
      stripeKey: process.env.STRIPE_PUBLIC_KEY,
      mediaUrl: process.env.MEDIA_URL,
    },
  },
  vite: {
    vue: {
      script: {
        defineModel: true,
        propsDestructure: true,
      },
    },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `
              @use '@/assets/scss/_vars.scss' as *;
              @use '@/assets/scss/_fonts.scss' as *;
              @use '@/assets/scss/_mixins.scss' as *;
              @use '@/assets/scss/_animations.scss' as *;
            `,
        },
      },
    },
  },
});
