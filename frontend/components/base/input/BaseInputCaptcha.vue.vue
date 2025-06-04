<script setup>
const { $config } = useNuxtApp()

const props = defineProps({
  hl: {
    type: String, // 'ru' | 'en' | 'be' | 'kk' | 'tt' | 'uk' | 'uz' | 'tr';
    default: 'ru'
  },
  test: {
    type: Boolean,
    default: false
  },
  webview: {
    type: Boolean,
    default: false
  },
  invisible: {
    type: Boolean,
    default: false
  },
  shieldPosition: {
    type: String, // `top-left` | `center-left` | `bottom-left` | `top-right` | `center-right` | `bottom-right`;
    default: 'top-left'
  },
  hideShield: {
    type: Boolean,
    default: true
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
const sitekey = $config.public.yandexCaptchaPublicKey
const emit = defineEmits(['success', 'error', 'expired', 'inited'])
let script = null
let mo = null

async function checkToken (val) {
  emit('success', val)
}

async function captchaInit () {
  widgetId.value = await window.smartCaptcha.render(
    captchaEl.value,
    {
      ...props,
      sitekey
    }
  )
  mo = new MutationObserver(async ([e]) => {
    if (e.target && e.target.value) {
      await checkToken(e.target.value)
    }
  })
  mo.observe(captchaEl.value.querySelector('input'), { attributes: true })
  isLoading.value = false
  initHandler()
}

onMounted(() => {
  if (!sitekey) {
    return emit('error', 'no key for captcha provided')
  }
  if (!window.smartCaptcha) {
    script = document.createElement('script')
    script.src = 'https://smartcaptcha.yandexcloud.net/captcha.js'
    script.defer = true
    script.onload = captchaInit
    document.head.appendChild(script)
  } else {
    captchaInit()
  }
})

onBeforeUnmount(() => {
  if (mo) {
    mo.disconnect()
  }
})

function captchaReset (id = widgetId.value) {
  if (!window.smartCaptcha) {
    return
  }
  window.smartCaptcha.reset(id)
  passed.value = false
}

function getCaptchaResponse (id = widgetId.value) {
  if (!window.smartCaptcha) {
    return null
  }
  return window.smartCaptcha.getResponse(id)
}

function checkUser (id = widgetId.value) {
  if (!window.smartCaptcha) {
    return null
  }
  window.smartCaptcha.subscribe(id, 'token-expired', () => {
    passed.value = false
    emit('expired')
  })
  return window.smartCaptcha.execute(id)
}

function initHandler () {
  emit('inited', {
    widgetId: widgetId.value,
    execute: checkUser,
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
      :style="!invisible && 'height: 102px'"
    />
    <label
      v-if="invisible"
      class="captcha-component__checkbox-label"
      @change="() => checkUser()"
    >
      <input
        v-model="passed"
        type="checkbox"
        class="captcha-component__checkbox"
        :value="passed"
      >
      <span>Подтвердите, что вы не робот</span>
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
      {{ isLoading ? 'Загружаем антиспам проверку' : '' }}
    </p>
  </div>
</template>
<style lang="scss" scoped>
.captcha-component {
  position: relative;
  width: 100%;
  color: rgb(250, 192, 0);
  color: #333;

  &__checkbox {
    &-label {
      display: flex;
      gap: 10px;
      cursor: pointer;
    }
  }

  &__error {
    position: absolute;
    color: $error;
    opacity: 1;
    top: 100%;
    left: 14px;
    font-size: 12px;
    transition: opacity .3s ease;
    
    &_hidden {
      opacity: 0;
      pointer-events: none;
    }

    &::before {
      content: '*';
    }
  }
}
</style>
