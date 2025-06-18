<script setup lang="ts">
import { api } from "~/api";
const { $api } = useNuxtApp();

defineProps<{
  currentStep: number;
}>();
const emit = defineEmits(["update:currentStep"]);
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
    await $api<ISubscribeResponse>(api.users.register, {
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
  <form class="auth-form-register" @submit.prevent="submit">
    <!-- Шаг 1: Контактные данные -->
    <div v-if="currentStep === 1" class="step-1">
      <div class="auth-form-register__group">
        <label for="email">Email</label>
        <BaseInput
          v-model:input-value="formData.email.value"
          radius="8px"
          type="email"
          placeholder="your@email.com"
        />
      </div>

      <div class="auth-form-register__group">
        <label for="phone">Телефон</label>
        <BaseInput
          v-model:input-value="formData.phone.value"
          radius="8px"
          type="text"
          placeholder="Ваш номер телефона"
        />
      </div>

      <div class="auth-form-register__group">
        <label for="password">Пароль</label>
        <BaseInput
          v-model:input-value="formData.password.value"
          radius="8px"
          type="password"
          placeholder="••••••••"
        />
      </div>

      <div class="auth-form-register__group">
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
        style="width: 100%; margin-top: 20px;"
      />
    </div>

    <!-- Шаг 2: Личные данные -->
    <div v-if="currentStep === 2" class="step-2">
      <div class="auth-form-register__group">
        <label for="firstName">Имя</label>
        <BaseInput
          v-model:input-value="formData.firstName.value"
          radius="8px"
          type="text"
          placeholder="Ваше имя"
        />
      </div>

      <div class="auth-form-register__group">
        <label for="lastName">Фамилия</label>
        <BaseInput
          v-model:input-value="formData.lastName.value"
          radius="8px"
          type="text"
          placeholder="Ваша фамилия"
        />
      </div>

      <div class="auth-form-register__group">
        <label for="city">Город</label>
        <BaseInput
          v-model:input-value="formData.city.value"
          radius="8px"
          type="text"
          placeholder="Ваш город"
        />
      </div>

      <div class="auth-form-register__group">
        <label for="address">Адрес доставки</label>
        <BaseInput
          v-model:input-value="formData.street.value"
          radius="8px"
          type="text"
          placeholder="Ваш город"
        />
      </div>

      <div class="auth-form-register__actions">
        <BaseButtonOutline
          label="Назад"
          size="lg"
          radius="8px"
          style="width: 100%"
          @click="emit('update:currentStep', 1)"
        />
        <BaseButton
          label="Зарегистрироваться"
          size="lg"
          radius="8px"
          style="width: 100%"
        />
      </div>
    </div>
    <div class="auth-form-register__footer">
      Уже есть аккаунт?
      <NuxtLink to="/auth/login" class="auth-form-register__footer-link">
        Войти
      </NuxtLink>
    </div>
  </form>
</template>
<style scoped lang="scss">
.auth-form-register {
  margin-top: 50px;

  &__group {
    @include form-group;
    label {
      display: block;
      margin-block: 8px;
      font-size: 14px;
      color: $txt;
      font-weight: 500;
    }
  }
  &__actions {
    display: flex;
    gap: 15px;
    margin-top: 30px;
  }
  &__footer {
    margin-top: 30px;
    text-align: center;
    font-size: 14px;
    color: $txt;
    &-link {
      color: $accent;
      text-decoration: none;
      font-weight: 500;
      transition: $default_transition;

      &:hover {
        color: $accent-dark;
        text-decoration: underline;
      }
    }
  }
}
</style>
