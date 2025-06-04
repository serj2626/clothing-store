<script setup lang="ts">
const email = ref('');
const message = ref('');
const error = ref('');

const submit = async () => {
  message.value = '';
  error.value = '';

  try {
    const { data, error: err } = await useFetch('/api/auth/reset-password', {
      method: 'POST',
      body: { email: email.value },
    });

    if (err.value) {
      error.value = err.value.data.message || 'Ошибка при отправке запроса.';
      return;
    }

    message.value =
      data?.value?.message || 'Проверьте свою почту для сброса пароля.';
  } catch (e) {
    error.value = 'Непредвиденная ошибка.';
  }
};
</script>
<template>
  <div class="reset-password">
    <h2>Сброс пароля</h2>
    <form @submit.prevent="submit">
      <div class="form-group">
        <label for="email">Email</label>
        <input
          v-model="email"
          id="email"
          type="email"
          required
          placeholder="Введите ваш email"
        />
      </div>
      <button type="submit">Отправить ссылку для сброса</button>
      <p v-if="message" class="success">{{ message }}</p>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<style scoped>
.reset-password {
  max-width: 400px;
  margin: auto;
  padding: 2rem;
}

.form-group {
  margin-bottom: 1rem;
}

.success {
  color: green;
}

.error {
  color: red;
}
</style>
