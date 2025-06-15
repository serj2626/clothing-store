<script setup>
const { $config } = useNuxtApp()

const props = defineProps({
  badge: {
    type: String, // 'bottomright' | 'bottomleft' | 'inline'
    default: 'inline'
  },
  autoVerify: {
    type: Boolean,
    default: false
  }
})

const captchaEl = ref(null)
const widgetId = ref(null)
const sitekey = $config.public.googleRecaptchaPublicKey
const emit = defineEmits(['success', 'error', 'expired'])

function initCaptcha() {
  widgetId.value = window.grecaptcha.render(captchaEl.value, {
    sitekey: sitekey,
    size: 'invisible',
    badge: props.badge,
    callback: (token) => emit('success', token),
    'expired-callback': () => emit('expired'),
    'error-callback': () => emit('error', 'reCAPTCHA error')
  })

  if (props.autoVerify) {
    execute()
  }
}

function execute() {
  if (widgetId.value) {
    window.grecaptcha.execute(widgetId.value)
  }
}

function reset() {
  if (widgetId.value) {
    window.grecaptcha.reset(widgetId.value)
  }
}

function getResponse() {
  if (widgetId.value) {
    return window.grecaptcha.getResponse(widgetId.value)
  }
  return null
}

onMounted(() => {
  if (!window.grecaptcha) {
    const script = document.createElement('script')
    script.src = `https://www.google.com/recaptcha/api.js?render=explicit`
    script.onload = initCaptcha
    document.head.appendChild(script)
  } else {
    initCaptcha()
  }
})

defineExpose({
  execute,
  reset,
  getResponse
})
</script>

<template>
  <div ref="captchaEl" class="invisible-recaptcha"></div>
</template>

<style scoped>
.invisible-recaptcha {
  display: none;
}
</style>


<!-- 


2. Использование в форме
vue
<script setup>
const form = ref({
  name: '',
  email: '',
  message: ''
})

const recaptcha = ref(null)
const isSubmitting = ref(false)
const submitError = ref('')

const handleSubmit = () => {
  if (!form.value.name || !form.value.email) {
    submitError.value = 'Заполните обязательные поля'
    return
  }
  
  // Запускаем невидимую капчу
  recaptcha.value.execute()
}

const onCaptchaSuccess = async (token) => {
  try {
    isSubmitting.value = true
    
    const response = await $fetch('/api/contact', {
      method: 'POST',
      body: {
        ...form.value,
        'g-recaptcha-response': token
      }
    })
    
    // Очистка формы после успешной отправки
    form.value = { name: '', email: '', message: '' }
    submitError.value = ''
    
  } catch (error) {
    submitError.value = error.message || 'Ошибка при отправке формы'
  } finally {
    isSubmitting.value = false
    recaptcha.value.reset()
  }
}
</script>

<template>
  <form @submit.prevent="handleSubmit" class="contact-form">
    <div class="form-group">
      <label>Имя *</label>
      <input v-model="form.name" required>
    </div>
    
    <div class="form-group">
      <label>Email *</label>
      <input v-model="form.email" type="email" required>
    </div>
    
    <div class="form-group">
      <label>Сообщение</label>
      <textarea v-model="form.message"></textarea>
    </div>
    
    <Recaptcha 
      ref="recaptcha" 
      badge="inline"
      @success="onCaptchaSuccess"
      @error="(err) => submitError.value = err"
    />
    
    <div v-if="submitError" class="error-message">
      {{ submitError }}
    </div>
    
    <button type="submit" :disabled="isSubmitting">
      {{ isSubmitting ? 'Отправка...' : 'Отправить' }}
    </button>
  </form>
</template> -->



<!-- Ключевые особенности невидимой reCAPTCHA:
Автоматический вызов - капча срабатывает при отправке формы

Поведение:

Для "нормальных" пользователей - проверка проходит незаметно

Для подозрительных - показывается challenge

Позиция бейджа - можно выбрать где отображать логотип

Интеграция:

Не требует действий пользователя (кроме подозрительных случаев)

Минимальное вмешательство в UX

Дополнительные настройки:
Для тестирования добавьте ?captcha=test к URL - капча будет всегда проходить

В консоли разработчика можно вызвать grecaptcha.execute() для ручного тестирования

Для отладки проверяйте параметры запроса к /siteverify

Этот подход обеспечит защиту от ботов без лишних действий со стороны пользователей. -->