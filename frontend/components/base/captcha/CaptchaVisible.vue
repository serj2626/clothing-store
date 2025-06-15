<script setup>
const { $config } = useNuxtApp()

const props = defineProps({
  theme: {
    type: String, // 'light' | 'dark'
    default: 'light'
  },
  size: {
    type: String, // 'normal' | 'compact'
    default: 'normal'
  },
  badge: {
    type: String, // 'bottomright' | 'bottomleft' | 'inline'
    default: 'bottomright'
  },
  test: {
    type: Boolean,
    default: false
  },
  invisible: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: ''
  }
})

const isLoading = ref(true)
const captchaEl = ref(null)
const widgetId = ref(null)
const passed = ref(false)
const sitekey = $config.public.recaptchaKey
const emit = defineEmits(['success', 'error', 'expired', 'inited'])
let script = null

async function checkToken(token) {
  if (token) {
    passed.value = true
    emit('success', token)
  }
}

function captchaInit() {
  if (!window.grecaptcha) {
    return emit('error', 'reCAPTCHA library not loaded')
  }

  widgetId.value = window.grecaptcha.render(captchaEl.value, {
    sitekey: sitekey,
    theme: props.theme,
    size: props.invisible ? 'invisible' : props.size,
    badge: props.badge,
    callback: (token) => checkToken(token),
    'expired-callback': () => {
      passed.value = false
      emit('expired')
    },
    'error-callback': () => {
      passed.value = false
      emit('error', 'reCAPTCHA error occurred')
    }
  })

  if (props.invisible) {
    window.grecaptcha.execute(widgetId.value)
  }

  isLoading.value = false
  initHandler()
}

function loadRecaptcha() {
  if (!sitekey) {
    return emit('error', 'Отсутствует ключ reCAPTCHA')
  }

  if (window.grecaptcha) {
    captchaInit()
    return
  }

  script = document.createElement('script')
  script.src = `https://www.google.com/recaptcha/api.js?render=explicit&hl=${props.hl}`
  script.defer = true
  script.async = true
  script.onload = captchaInit
  script.onerror = () => emit('error', 'Failed to load reCAPTCHA script')
  document.head.appendChild(script)
}

onMounted(() => {
  loadRecaptcha()
})

onBeforeUnmount(() => {
  if (window.grecaptcha && widgetId.value) {
    window.grecaptcha.reset(widgetId.value)
  }
  if (script) {
    document.head.removeChild(script)
  }
})

function captchaReset(id = widgetId.value) {
  if (!window.grecaptcha || !id) return
  window.grecaptcha.reset(id)
  passed.value = false
}

function getCaptchaResponse(id = widgetId.value) {
  if (!window.grecaptcha || !id) return null
  return window.grecaptcha.getResponse(id)
}

function executeCaptcha(id = widgetId.value) {
  if (!window.grecaptcha || !id) return null
  window.grecaptcha.execute(id)
}

function initHandler() {
  emit('inited', {
    widgetId: widgetId.value,
    execute: executeCaptcha,
    getResponse: getCaptchaResponse,
    reset: captchaReset
  })
}
</script>

<template>
  <div class="captcha-component" :loading="isLoading">
    <div
      ref="captchaEl"
      class="captcha-component__wrapper"
      :style="!invisible && size === 'normal' ? 'min-height: 78px' : 'min-height: 60px'"
    />
    <label
      v-if="invisible"
      class="captcha-component__checkbox-label"
      @click="executeCaptcha"
    >
      <input
        v-model="passed"
        type="checkbox"
        class="captcha-component__checkbox"
        :value="passed"
      >
      <span>Я не робот</span>
    </label>
    <p
      v-if="!invisible"
      class="captcha-component__error"
      :class="{
        'captcha-component__error_hidden': !error
      }"
    >
      {{ error }}
    </p>
    <p v-if="!invisible" class="captcha-component__message">
      {{ isLoading ? 'Загружаем проверку reCAPTCHA' : '' }}
    </p>
  </div>
</template>

<style lang="scss" scoped>
.captcha-component {
  position: relative;
  width: 100%;
  color: #333;

  &__checkbox {
    &-label {
      display: flex;
      gap: 10px;
      align-items: center;
      cursor: pointer;
      user-select: none;
    }
  }

  &__wrapper {
    display: flex;
    justify-content: center;
  }

  &__error {
    position: absolute;
    color: $error;
    opacity: 1;
    top: 100%;
    left: 0;
    font-size: 12px;
    transition: opacity 0.3s ease;
    
    &_hidden {
      opacity: 0;
      pointer-events: none;
    }

    &::before {
      content: '*';
    }
  }

  &__message {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
  }
}
</style>




<!-- Ключевые особенности реализации:
Поддержка разных типов reCAPTCHA:

Обычная (с галочкой)

Невидимая (invisible)

Параметры настройки:

Тема (light/dark)

Размер (normal/compact)

Положение бейджа (bottomright/bottomleft/inline)

Методы API:

reset() - сброс капчи

getResponse() - получение токена

execute() - принудительный запуск (для невидимой)

События:

success - при успешной проверке

error - при ошибке

expired - когда токен истек

inited - когда виджет инициализирован

Интеграция с Nuxt 3:

Использование useNuxtApp() для доступа к конфигу

Автоматическая загрузка скрипта reCAPTCHA

Очистка ресурсов при размонтировании

Адаптивный дизайн:

Поддержка разных размеров

Стилизация ошибок и состояний -->