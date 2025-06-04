<!-- npm install @vueuse/core -->

<!-- <script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useScriptTag } from '@vueuse/core'

const props = defineProps<{
  siteKey: string
  theme?: 'light' | 'dark'
  size?: 'normal' | 'compact'
  tabindex?: number
  error?: string
  invisible?: boolean
}>()

const emit = defineEmits(['success', 'error', 'expired', 'inited'])

const captchaRef = ref<HTMLElement | null>(null)
const widgetId = ref<number | null>(null)

const renderCaptcha = () => {
  if (!window.grecaptcha || !captchaRef.value) {
    emit('error', 'Капча не загрузилась')
    return
  }

  widgetId.value = window.grecaptcha.render(captchaRef.value, {
    sitekey: props.siteKey,
    theme: props.theme || 'light',
    size: props.invisible ? 'invisible' : (props.size || 'normal'),
    tabindex: props.tabindex || 0,
    callback: (response: string) => {
      emit('success', response)
    },
    'expired-callback': () => {
      emit('expired')
    },
    'error-callback': () => {
      emit('error', 'Ошибка капчи')
    },
  })

  emit('inited', true)
}

onMounted(async () => {
  // Загружаем скрипт
  await useScriptTag('https://www.google.com/recaptcha/api.js?render=explicit', () => {
    // Ждём пока библиотека инициализируется
    if (window.grecaptcha) {
      window.grecaptcha.ready(() => {
        renderCaptcha()
      })
    } else {
      emit('error', 'Капча не загрузилась')
    }
  }, { manual: false })
})
</script>

<template>
  <div class="base-captcha">
    <div ref="captchaRef" />
    <p v-if="error" class="captcha-error">{{ error }}</p>
  </div>
</template>

<style scoped>
.captcha-error {
  color: red;
  font-size: 14px;
}
</style> -->




<!-- <BaseCaptcha
  class="base-schedule-form__captcha"
  :site-key="'ВАШ_SITE_KEY'"
  :error="formData.captcha.error"
  :invisible="false"
  @success="(val) => captchaHandler(val, 'success')"
  @error="(val) => captchaHandler(val, 'error')"
  @expired="(val) => captchaHandler(val, 'expired')"
  @inited="(val) => captchaHandler(val, 'inited')"
/> -->