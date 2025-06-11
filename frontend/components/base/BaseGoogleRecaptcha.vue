<script setup lang="ts">
const config = useRuntimeConfig();
const siteKey = config.public.recaptchaKey;

interface Props {
  error?: string;
  invisible?: boolean;
  theme?: "light" | "dark";
}

const props = withDefaults(defineProps<Props>(), {
  error: "",
  invisible: false,
  theme: "light",
});

const emit = defineEmits<{
  (e: "success", token: string): void;
  (e: "error"): void;
  (e: "expired"): void;
}>();

const recaptchaElement = ref<HTMLElement | null>(null);
const widgetId = ref<number | null>(null);

// Добавляем callback для невидимой reCAPTCHA
declare global {
  interface Window {
    invisibleCallback?: (token: string) => void;
  }
}

// Инициализация reCAPTCHA
const initRecaptcha = () => {
  if (window.grecaptcha && recaptchaElement.value) {
    if (props.invisible) {
      window.invisibleCallback = (token: string) => {
        emit("success", token);
      };
    }

    widgetId.value = window.grecaptcha.render(recaptchaElement.value, {
      sitekey: siteKey,
      size: props.invisible ? "invisible" : "normal",
      theme: props.theme,
      callback: !props.invisible
        ? (token: string) => emit("success", token)
        : undefined,
      "error-callback": () => emit("error"),
      "expired-callback": () => emit("expired"),
    });
  }
};

// Загрузка скрипта reCAPTCHA
const loadRecaptchaScript = () => {
  if (document.querySelector('script[src*="recaptcha/api.js"]')) {
    initRecaptcha();
    return;
  }

  const script = document.createElement("script");
  script.src = `https://www.google.com/recaptcha/api.js?render=explicit&hl=${
    document.documentElement.lang || "en"
  }`;
  script.async = true;
  script.defer = true;
  script.onload = initRecaptcha;
  document.head.appendChild(script);
};

// Сброс капчи
const reset = () => {
  if (widgetId.value !== null && window.grecaptcha) {
    window.grecaptcha.reset(widgetId.value);
  }
};

// Получение токена (для невидимой reCAPTCHA)
const execute = () => {
  if (widgetId.value !== null && window.grecaptcha) {
    window.grecaptcha.execute(widgetId.value);
  }
};

onMounted(() => {
  loadRecaptchaScript();
});

onUnmounted(() => {
  if (window.invisibleCallback) {
    delete window.invisibleCallback;
  }
});

// Экспортируем методы для использования через ref
defineExpose({
  reset,
  execute,
});
</script>
<template>
  <div :class="['base-captcha', { 'has-error': error }]">
    <div
      ref="recaptchaElement"
      class="g-recaptcha"
      :data-sitekey="siteKey"
      :data-size="invisible ? 'invisible' : 'normal'"
      :data-theme="theme"
      :data-callback="invisible ? 'invisibleCallback' : undefined"
    ></div>
    <div v-if="error" class="base-captcha__error">{{ error }}</div>
  </div>
</template>
<style scoped>
.base-captcha {
  margin: 1rem 0;
}

.base-captcha.has-error {
  color: red;
}

.base-captcha__error {
  margin-top: 0.5rem;
  color: red;
  font-size: 0.875rem;
}
</style>

<!-- 
<template>
  <form @submit.prevent="handleSubmit">
    <BaseCaptcha
      ref="captchaRef"
      class="base-schedule-form__captcha"
      :site-key="RECAPTCHA_SITE_KEY"
      :error="formData.captcha.error"
      :invisible="false"
      @success="(token) => captchaHandler(token, 'success')"
      @error="() => captchaHandler('', 'error')"
      @expired="() => captchaHandler('', 'expired')"
    />
    
    <button type="submit">Отправить</button>
  </form>
</template>

<script setup lang="ts">
const RECAPTCHA_SITE_KEY = 'ВАШ_SITE_KEY' // или из .env

const captchaRef = ref()

const formData = reactive({
  captcha: {
    token: '',
    error: ''
  }
})

const captchaHandler = (token: string, type: string) => {
  switch (type) {
    case 'success':
      formData.captcha.token = token
      formData.captcha.error = ''
      break
    case 'error':
      formData.captcha.token = ''
      formData.captcha.error = 'Ошибка проверки капчи'
      break
    case 'expired':
      formData.captcha.token = ''
      formData.captcha.error = 'Время действия капчи истекло'
      break
  }
}

const handleSubmit = async () => {
  if (!formData.captcha.token) {
    formData.captcha.error = 'Пожалуйста, пройдите проверку'
    return
  }
  
  try {
    // Отправка формы с токеном капчи
    // await submitForm({ ...formData, captchaToken: formData.captcha.token })
    
    // Сброс капчи после успешной отправки
    if (captchaRef.value) {
      captchaRef.value.reset()
    }
  } catch (error) {
    formData.captcha.error = 'Ошибка при проверке капчи'
  }
}
</script> -->



<!--     
3. Для невидимой reCAPTCHA
Если вам нужна невидимая reCAPTCHA:

vue
<template>
  <form @submit.prevent="handleSubmit">
    <BaseCaptcha
      ref="captchaRef"
      :site-key="RECAPTCHA_SITE_KEY"
      :invisible="true"
      @success="(token) => { formData.captcha.token = token }"
    />
    
    <button type="submit">Отправить</button>
  </form>
</template>

<script setup lang="ts">
const captchaRef = ref()

const handleSubmit = () => {
  captchaRef.value?.execute()
}
</script> -->


<!-- 
Как это работает
Компонент динамически загружает скрипт reCAPTCHA от Google

Инициализирует reCAPTCHA с указанными параметрами

Поддерживает как обычную, так и невидимую reCAPTCHA

Предоставляет методы reset() и execute() для управления через ref

Вызывает соответствующие события для обработки в родительском компоненте

Это решение не требует сторонних библиотек и полностью реализует функциональность reCAPTCHA v2 с использованием Composition API в Nuxt 3. -->

