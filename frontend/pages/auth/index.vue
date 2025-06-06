<template>
  <div class="auth-page">
    <div class="auth-container">
      <!-- Логотип -->
      <div class="auth-logo">
        <h1>ClothCrash</h1>
      </div>

      <!-- Переключатель форм -->
      <div class="auth-tabs">
        <button
          class="auth-tab"
          :class="{ 'auth-tab--active': isLoginForm }"
          @click="toggleForm(true)"
        >
          Вход
        </button>
        <button
          class="auth-tab"
          :class="{ 'auth-tab--active': !isLoginForm }"
          @click="toggleForm(false)"
        >
          Регистрация
        </button>
      </div>

      <!-- Форма входа -->
      <form v-if="isLoginForm" @submit.prevent="handleLogin" class="auth-form">
        <div class="form-group">
          <label for="login-email">Email</label>
          <input
            id="login-email"
            v-model="loginData.email"
            type="email"
            required
            placeholder="your@email.com"
          />
        </div>

        <div class="form-group">
          <label for="login-password">Пароль</label>
          <input
            id="login-password"
            v-model="loginData.password"
            type="password"
            required
            placeholder="••••••••"
          />
          <NuxtLink to="/forgot-password" class="forgot-password">
            Забыли пароль?
          </NuxtLink>
        </div>

        <button type="submit" class="auth-btn" :disabled="isLoading">
          <span v-if="!isLoading">Войти</span>
          <span v-else class="loader"></span>
        </button>

        <div v-if="loginError" class="error-message">
          {{ loginError }}
        </div>
      </form>

      <!-- Форма регистрации -->
      <form v-else @submit.prevent="handleRegister" class="auth-form">
        <div class="form-group">
          <label for="register-name">Имя</label>
          <input
            id="register-name"
            v-model="registerData.name"
            type="text"
            required
            placeholder="Ваше имя"
          />
        </div>

        <div class="form-group">
          <label for="register-email">Email</label>
          <input
            id="register-email"
            v-model="registerData.email"
            type="email"
            required
            placeholder="your@email.com"
          />
        </div>

        <div class="form-group">
          <label for="register-password">Пароль</label>
          <input
            id="register-password"
            v-model="registerData.password"
            type="password"
            required
            placeholder="••••••••"
            minlength="6"
          />
        </div>

        <div class="form-group">
          <label for="register-confirm">Подтвердите пароль</label>
          <input
            id="register-confirm"
            v-model="registerData.confirmPassword"
            type="password"
            required
            placeholder="••••••••"
          />
        </div>

        <button type="submit" class="auth-btn" :disabled="isLoading">
          <span v-if="!isLoading">Зарегистрироваться</span>
          <span v-else class="loader"></span>
        </button>

        <div v-if="registerError" class="error-message">
          {{ registerError }}
        </div>
      </form>

      <!-- Социальные сети -->
      <div class="auth-social">
        <p>Или войдите через</p>
        <div class="social-buttons">
          <button class="social-btn google">
            <Icon name="logos:google-icon" size="20" />
            Google
          </button>
          <button class="social-btn vk">
            <Icon name="logos:vk" size="20" />
            VK
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const authStore = useAuthStore()
const router = useRouter()

const isLoginForm = ref(true)
const isLoading = ref(false)
const loginError = ref('')
const registerError = ref('')

const loginData = reactive({
  email: '',
  password: ''
})

const registerData = reactive({
  name: '',
  email: '',
  password: '',
  confirmPassword: ''
})

const toggleForm = (showLogin: boolean) => {
  isLoginForm.value = showLogin
  loginError.value = ''
  registerError.value = ''
}

const validateRegister = () => {
  if (registerData.password !== registerData.confirmPassword) {
    registerError.value = 'Пароли не совпадают'
    return false
  }
  if (registerData.password.length < 6) {
    registerError.value = 'Пароль должен содержать минимум 6 символов'
    return false
  }
  return true
}

const handleLogin = async () => {
  try {
    isLoading.value = true
    loginError.value = ''
    const success = await authStore.login(loginData)
    
    if (success) {
      await router.push('/account')
    } else {
      loginError.value = 'Неверный email или пароль'
    }
  } catch (error) {
    loginError.value = 'Произошла ошибка при входе'
    console.error('Login error:', error)
  } finally {
    isLoading.value = false
  }
}

const handleRegister = async () => {
  if (!validateRegister()) return

  try {
    isLoading.value = true
    registerError.value = ''
    const success = await authStore.register({
      name: registerData.name,
      email: registerData.email,
      password: registerData.password
    })
    
    if (success) {
      await router.push('/account')
    } else {
      registerError.value = 'Ошибка при регистрации'
    }
  } catch (error) {
    registerError.value = 'Произошла ошибка при регистрации'
    console.error('Registration error:', error)
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped lang="scss">
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;

}

.auth-container {
  width: 100%;
  max-width: 480px;
  background-color: $white;
  border-radius: $btn_radius;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  padding: 40px;
  animation: fadeIn $default_transition;
}

.auth-logo {
  text-align: center;
  margin-bottom: 30px;
  
  h1 {
    font-family: $ff_title;
    font-size: 32px;
    color: $accent-dark;
    margin: 0;
  }
}

.auth-tabs {
  display: flex;
  margin-bottom: 30px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.auth-tab {
  flex: 1;
  padding: 12px;
  font-family: $ff_second;
  font-size: 16px;
  font-weight: 500;
  background: none;
  border: none;
  cursor: pointer;
  position: relative;
  color: rgba($txt, 0.6);
  transition: color $default_transition;

  &--active {
    color: $txt;
    font-weight: 600;

    &::after {
      content: '';
      position: absolute;
      bottom: -1px;
      left: 0;
      width: 100%;
      height: 2px;
      background-color: $accent;
      border-radius: 2px 2px 0 0;
    }
  }
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;

  label {
    font-family: $ff_second;
    font-size: 14px;
    color: $txt;
    font-weight: 500;
  }

  input {
    padding: 14px 16px;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: $btn_radius;
    font-family: $ff_second;
    font-size: 16px;
    transition: border-color $default_transition;

    &:focus {
      outline: none;
      border-color: $accent;
    }

    &::placeholder {
      color: rgba($txt, 0.4);
    }
  }
}

.forgot-password {
  align-self: flex-end;
  font-family: $ff_second;
  font-size: 12px;
  color: rgba($txt, 0.6);
  text-decoration: none;
  transition: color $default_transition;

  &:hover {
    color: $accent-dark;
  }
}

.auth-btn {
  padding: 16px;
  background-color: $accent;
  color: $white;
  border: none;
  border-radius: $btn_radius;
  font-family: $ff_second;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: 
    background-color $default_transition,
    box-shadow $default_transition;

  &:hover {
    background-color: $accent-dark;
    box-shadow: $btn-accent-hover-shadow;
  }

  &:active {
    background-color: $btn-accent-active;
  }

  &:disabled {
    background-color: rgba($accent, 0.7);
    cursor: not-allowed;
  }
}

.loader {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid $white;
  border-radius: 50%;
  border-top-color: transparent;
  animation: spin 0.8s linear infinite;
}

.error-message {
  padding: 12px;
  background-color: rgba($error, 0.1);
  border-radius: $btn_radius;
  color: $error;
  font-family: $ff_second;
  font-size: 14px;
  text-align: center;
}

.auth-social {
  margin-top: 30px;
  text-align: center;

  p {
    font-family: $ff_second;
    font-size: 14px;
    color: rgba($txt, 0.6);
    margin-bottom: 16px;
    position: relative;

    &::before,
    &::after {
      content: '';
      position: absolute;
      top: 50%;
      width: 30%;
      height: 1px;
      background-color: rgba(0, 0, 0, 0.1);
    }

    &::before {
      left: 0;
    }

    &::after {
      right: 0;
    }
  }
}

.social-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.social-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border-radius: $btn_radius;
  font-family: $ff_second;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  border: 1px solid rgba(0, 0, 0, 0.1);
  background-color: $white;
  transition: 
    background-color $default_transition,
    transform $default_transition;

  &:hover {
    transform: translateY(-2px);
  }

  &.google {
    color: #4285F4;
  }

  &.vk {
    color: #0077FF;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: $tablet) {
  .auth-container {
    padding: 30px 20px;
  }

  .social-buttons {
    flex-direction: column;
  }
}
</style>