<script setup lang="ts">
import { api } from "~/api";
const { $api } = useNuxtApp();

const currentStep = ref(1);

const modalsStore = useModalsStore();

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface ISubscribeResponse {
  message: string;
  status: string;
}

interface FeedbackForm {
  email: FormField<string>;
  phone: FormField<string>;
  password: FormField<string>;
  passwordConfirm: FormField<string>;
  firstName: FormField<string>;
  lastName: FormField<string>;
  city: FormField<string>;
  street: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  email: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  password: { value: "", error: "", required: true },
  passwordConfirm: { value: "", error: "", required: true },
  firstName: { value: "", error: "", required: true },
  lastName: { value: "", error: "", required: true },
  city: { value: "", error: "", required: true },
  street: { value: "", error: "", required: true },
});

async function submit() {
  try {
    const res = await $api<ISubscribeResponse>(api.users.register, {
      method: "POST",
      body: {
        email: formData.email.value,
        phone: formData.phone.value,
        password: formData.password.value,
        password2: formData.passwordConfirm.value,
      },
    });
    modalsStore.openModal("success");
    clearForm(formData);
  } catch (e) {
    console.log("error", e);
  }
}

// const validateStep1 = () => {
//   let isValid = true;
//   errors.value = {
//     email: "",
//     phone: "",
//     password: "",
//     confirmPassword: "",
//   };

//   // Валидация email
//   if (!formData.value.email) {
//     errors.value.email = "Введите email";
//     isValid = false;
//   } else if (!/^\S+@\S+\.\S+$/.test(formData.value.email)) {
//     errors.value.email = "Введите корректный email";
//     isValid = false;
//   }

//   // Валидация телефона
//   if (!formData.value.phone) {
//     errors.value.phone = "Введите телефон";
//     isValid = false;
//   } else if (formData.value.phone.replace(/\D/g, "").length < 11) {
//     errors.value.phone = "Введите корректный телефон";
//     isValid = false;
//   }

//   // Валидация пароля
//   if (!formData.value.password) {
//     errors.value.password = "Введите пароль";
//     isValid = false;
//   } else if (formData.value.password.length < 8) {
//     errors.value.password = "Пароль должен содержать минимум 8 символов";
//     isValid = false;
//   }

//   // Подтверждение пароля
//   if (formData.value.password !== formData.value.confirmPassword) {
//     errors.value.confirmPassword = "Пароли не совпадают";
//     isValid = false;
//   }

//   if (isValid) {
//     currentStep.value = 2;
//   }
// };

// const handleSubmit = async () => {
//   // Валидация второго шага
//   let isValid = true;
//   errors.value = {
//     firstName: "",
//     lastName: "",
//     city: "",
//     address: "",
//   };

//   if (!formData.value.firstName) {
//     errors.value.firstName = "Введите имя";
//     isValid = false;
//   }

//   if (!formData.value.lastName) {
//     errors.value.lastName = "Введите фамилию";
//     isValid = false;
//   }

//   if (!formData.value.city) {
//     errors.value.city = "Введите город";
//     isValid = false;
//   }

//   if (!formData.value.address) {
//     errors.value.address = "Введите адрес";
//     isValid = false;
//   }

//   if (isValid) {
//     try {
//       // Отправка данных на сервер Django
//       const response = await $fetch("/api/auth/register/", {
//         method: "POST",
//         body: JSON.stringify(formData.value),
//       });

//       // Перенаправление после успешной регистрации
//       navigateTo("/account");
//     } catch (error) {
//       console.error("Ошибка регистрации:", error);
//       // Обработка ошибок сервера
//     }
//   }
// };
</script>
<template>
  <div class="auth-page">
    <div class="auth-container">
      <!-- Логотип -->
      <div class="logo">
        <h1 class="logo-text">ClothCrash</h1>
      </div>

      <!-- Прогресс-бар -->
      <div class="progress-steps">
        <div
          class="step"
          :class="{ active: currentStep === 1, completed: currentStep > 1 }"
          @click="currentStep = 1"
        >
          <span class="step-number">1</span>
          <span class="step-label">Контактные данные</span>
        </div>
        <div class="step-line"></div>
        <div
          class="step"
          :class="{ active: currentStep === 2, completed: currentStep > 2 }"
          @click="currentStep = 2"
        >
          <span class="step-number">2</span>
          <span class="step-label">Личные данные</span>
        </div>
      </div>

      <!-- Форма регистрации -->
      <form class="register-form" @submit.prevent="submit">
        <!-- Шаг 1: Контактные данные -->
        <div v-if="currentStep === 1" class="step-1">
          <div class="form-group">
            <label for="email">Email</label>
            <BaseInput
              v-model:input-value="formData.email.value"
              radius="8px"
              type="email"
              placeholder="your@email.com"
            />
          </div>

          <div class="form-group">
            <label for="phone">Телефон</label>
            <BaseInput
              v-model:input-value="formData.phone.value"
              radius="8px"
              type="text"
              placeholder="Ваш номер телефона"
            />
          </div>

          <div class="form-group">
            <label for="password">Пароль</label>
            <BaseInput
              v-model:input-value="formData.password.value"
              radius="8px"
              type="password"
              placeholder="••••••••"
            />
          </div>

          <div class="form-group">
            <label for="confirmPassword">Подтвердите пароль</label>
            <BaseInput
              v-model:input-value="formData.passwordConfirm.value"
              radius="8px"
              type="password"
              placeholder="••••••••"
            />
          </div>

          <BaseButton
            label="Продолжить"
            size="lg"
            radius="8px"
            style="width: 100%"
          />
        </div>

        <!-- Шаг 2: Личные данные -->
        <div v-if="currentStep === 2" class="step-2">
          <div class="form-group">
            <label for="firstName">Имя</label>
            <BaseInput
              v-model:input-value="formData.firstName.value"
              radius="8px"
              type="password"
              placeholder="Ваше имя"
            />
          </div>

          <div class="form-group">
            <label for="lastName">Фамилия</label>
            <BaseInput
              v-model:input-value="formData.lastName.value"
              radius="8px"
              type="password"
              placeholder="Ваша фамилия"
            />
          </div>

          <div class="form-group">
            <label for="city">Город</label>
            <BaseInput
              v-model:input-value="formData.city.value"
              radius="8px"
              type="password"
              placeholder="Ваш город"
            />
          </div>

          <div class="form-group">
            <label for="address">Адрес доставки</label>
            <BaseInput
              v-model:input-value="formData.street.value"
              radius="8px"
              type="password"
              placeholder="Ваш город"
            />
          </div>

          <div class="form-actions">
            <BaseButtonOutline
              label="Назад"
              size="lg"
              radius="8px"
              style="width: 100%"
            />
            <BaseButton
              label="Зарегистрироваться"
              size="lg"
              radius="8px"
              style="width: 100%"
            />
          </div>
        </div>
      </form>

      <div class="auth-footer">
        Уже есть аккаунт?
        <NuxtLink to="/auth/login" class="login-link">Войти</NuxtLink>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f5f5;
  font-family: $ff_main;
  padding: 20px;
}

.auth-container {
  width: 100%;
  max-width: 500px;
  background-color: $white;
  border-radius: $btn_radius;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  padding: 40px;
}

.logo {
  text-align: center;
  margin-bottom: 30px;
}

.logo-text {
  font-family: $ff_title;
  font-size: 28px;
  color: $accent-dark;
  font-weight: 700;
}

.progress-steps {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 30px;
  position: relative;
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  z-index: 1;
}

.step-number {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-color: #e0e0e0;
  color: $txt;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 500;
  transition: $default_transition;
}

.step-label {
  margin-top: 8px;
  font-size: 14px;
  color: #757575;
  transition: $default_transition;
}

.step-line {
  position: absolute;
  top: 18px;
  left: 25%;
  right: 25%;
  height: 2px;
  background-color: #e0e0e0;
  z-index: 0;
}

.step.active .step-number,
.step.completed .step-number {
  background-color: $accent;
  color: $white;
}

.step.active .step-label,
.step.completed .step-label {
  color: $txt;
  font-weight: 500;
}

.register-form {
  margin-top: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-size: 14px;
  color: $txt;
  font-weight: 500;
}

.form-input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #e0e0e0;
  border-radius: $btn_radius;
  font-family: $ff_second;
  font-size: 16px;
  transition: $default_transition;
}

.form-input:focus {
  border-color: $accent;
  outline: none;
  box-shadow: 0 0 0 2px rgba($accent, 0.2);
}

.form-input.error {
  border-color: $error;
}

.error-message {
  display: block;
  margin-top: 6px;
  font-size: 12px;
  color: $error;
}

.btn-next,
.btn-submit {
  width: 100%;
  padding: 14px;
  background-color: $accent;
  color: $white;
  border: none;
  border-radius: $btn_radius;
  font-family: $ff_second;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: $default_transition;
}

.btn-next:hover,
.btn-submit:hover {
  background-color: $accent-dark;
  box-shadow: $btn-accent-hover-shadow;
}

.btn-back {
  width: 100%;
  padding: 14px;
  background-color: transparent;
  color: $accent;
  border: 1px solid $accent;
  border-radius: $btn_radius;
  font-family: $ff_second;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: $default_transition;
}

.btn-back:hover {
  background-color: rgba($accent, 0.1);
}

.form-actions {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

.form-actions button {
  flex: 1;
}

.auth-footer {
  margin-top: 30px;
  text-align: center;
  font-size: 14px;
  color: #757575;
}

.login-link {
  color: $accent;
  text-decoration: none;
  font-weight: 500;
  transition: $default_transition;
}

.login-link:hover {
  color: $accent-dark;
  text-decoration: underline;
}

@media (max-width: $tablet) {
  .auth-container {
    padding: 30px;
  }
}

@media (max-width: $mobile) {
  .auth-container {
    padding: 20px;
  }

  .form-actions {
    flex-direction: column;
  }
}
</style>
