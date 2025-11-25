<script setup lang="ts">
import { api } from "~/api";
const { $api } = useNuxtApp();

const modalsStore = useModalsStore();

const {
  productName = "Футболка хлопковая",
  productId = "a96ef041-bb6a-44ab-a48d-3faefbb6baba",
} = defineProps<{
  productName?: string;
  productId?: string;
}>();

let captchaInstance = null;
const images = ref([]);
const fileInput = ref(null);

const triggerFileInput = () => {
  fileInput.value.click();
};

const handleImageUpload = (event) => {
  const files = Array.from(event.target.files);
  const remainingSlots = 3 - images.value.length;

  if (files.length > remainingSlots) {
    alert(`Можно загрузить только ${remainingSlots} дополнительных фото`);
    return;
  }

  files.slice(0, remainingSlots).forEach((file) => {
    if (file.size > 5 * 1024 * 1024) {
      alert("Файл слишком большой. Максимальный размер: 5MB");
      return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
      images.value.push({
        file,
        preview: e.target.result,
      });
    };
    reader.readAsDataURL(file);
  });
};

const removeImage = (index) => {
  images.value.splice(index, 1);
};

const getImageUrl = (image) => {
  return image.preview || URL.createObjectURL(image.file);
};

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface FeedbackForm {
  message: FormField<string>;
  email: FormField<string>;
  name: FormField<string>;
  captcha: FormField<string>;
  rating: FormField<number>;
  advantages: FormField<string>;
  disadvantages: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  name: { value: "", error: "", required: true },
  email: { value: "", error: "", required: true },
  message: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
  rating: { value: 5, error: "", required: true },
  advantages: { value: "", error: "", required: true },
  disadvantages: { value: "", error: "", required: true },
});

function clearForm() {
  Object.keys(formData).forEach((key) => {
    if (formData[key as keyof typeof formData] === "rating") {
      formData[key as keyof typeof formData].value = 5;
      formData[key as keyof typeof formData].error = "";
    } else {
      formData[key as keyof typeof formData].value = "";
      formData[key as keyof typeof formData].error = "";
    }
  });
}

async function submit() {
  console.log("formData", formData);
  // if (validateForm(formData)) return;
  try {
    const res = await $api(api.products.createReview(productId), {
      method: "POST",
      body: {
        user: "71e37f71-0008-4bcf-b985-fa7512b08293",
        name: formData.name.value,
        email: formData.email.value,
        description: formData.message.value,
        product: productId,
        advantages: formData.advantages.value,
        disadvantages: formData.disadvantages.value,
        rating: formData.rating.value,
      },
    });
    console.log("asdasdsad", res);
    modalsStore.openModal("success");
    clearForm();
  } catch (e) {
    console.log("error", e);
  }
}

function captchaHandler(val, eventName) {
  if (eventName === "success") {
    formData.captcha.value = val;
    formData.captcha.error = "";
  } else if (eventName === "error" || eventName === "expired") {
    formData.captcha.value = "";
    formData.captcha.error = "Необходимо пройти антиспам проверку";
  } else if (eventName === "inited") {
    captchaInstance = val;
  }
}
</script>
<template>
  <div class="modal-review">
    <form class="modal-content" @submit.prevent="submit">
      <div class="modal-header">
        <h2 class="modal-title">Оставить отзыв</h2>
        <p class="product-name">О товаре: {{ productName }}</p>
      </div>

      <RatingComponent v-model:rating-value="formData.rating.value" />

      <div class="review-form">
        <div class="form-row">
          <div class="form-group">
            <label for="name">Ваше имя *</label>

            <BaseInput
              v-model:input-value="formData.name.value"
              radius="8px"
              placeholder="Иван Иванов"
            />
          </div>

          <div class="form-group">
            <label for="email">Email</label>

            <BaseInput
              v-model:input-value="formData.email.value"
              radius="8px"
              placeholder="example@mail.com"
              :disabled="true"
            />
          </div>
        </div>

        <div class="form-group">
          <label for="review">Отзыв *</label>

          <BaseInputTextArea
            v-model:textarea-value="formData.message.value"
            radius="8px"
            placeholder="Поделитесь впечатлениями о товаре"
          />
          <span class="char-counter"
            >{{ formData.message.value.length }}/500</span
          >
        </div>

        <div class="form-group">
          <label for="advantages">Достоинства</label>

          <BaseInputTextArea
            v-model:textarea-value="formData.advantages.value"
            radius="8px"
            placeholder="Что вам понравилось?"
          />
        </div>

        <div class="form-group">
          <label for="disadvantages">Недостатки</label>

          <BaseInputTextArea
            v-model:textarea-value="formData.disadvantages.value"
            radius="8px"
            placeholder="Что можно улучшить?"
          />
        </div>
        <!-- <BaseCaptchaVisible
          :error="formData.captcha.error"
          @success="(val) => captchaHandler(val, 'success')"
          @error="(err) => captchaHandler(err, 'error')"
          @expired="() => captchaHandler(null, 'expired')"
          @inited="(val) => captchaHandler(val, 'inited')"
        /> -->
        <div class="image-upload">
          <label>Добавить фото (макс. 3)</label>
          <div class="upload-area" @click="triggerFileInput">
            <div v-if="images.length === 0" class="upload-placeholder">
              <svg
                width="40"
                height="40"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M19 13H13V19H11V13H5V11H11V5H13V11H19V13Z"
                  fill="#d38f56"
                />
              </svg>
              <p>Нажмите чтобы загрузить фото</p>
            </div>
            <div v-else class="image-preview-container">
              <div
                v-for="(image, index) in images"
                :key="index"
                class="image-preview"
              >
                <img :src="getImageUrl(image)" alt="Превью фото" />
                <button class="remove-image" @click.stop="removeImage(index)">
                  &times;
                </button>
              </div>
              <div
                v-if="images.length < 3"
                class="add-more"
                @click.stop="triggerFileInput"
              >
                +
              </div>
            </div>
            <input
              ref="fileInput"
              type="file"
              accept="image/*"
              multiple
              style="display: none"
              @change="handleImageUpload"
            />
          </div>
          <p class="upload-hint">Форматы: JPG, PNG. Максимальный размер: 5MB</p>
        </div>
        <BaseButton
          label="Отправить отзыв"
          size="lg"
          radius="8px"
          style="width: 100%"
        />
      </div>
      <BaseButtonClose
        top="15px"
        right="15px"
        :size="30"
        @click="modalsStore.closeModal('review')"
      />
    </form>
  </div>
</template>
<style scoped lang="scss">
.modal-review {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-height: 90vh;
  width: 100%;
  max-width: 700px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch; /* Для плавного скролла на iOS */
}

.modal-content {
  position: relative;
  background-color: $white;
  box-shadow: 0 10px 25px rgba($black, 0.2);
  padding: 2.5rem;
}

.modal-header {
  margin-bottom: 2rem;
  text-align: center;
}

.modal-title {
  font-family: $ff_title;
  font-size: 1.75rem;
  color: $txt;
  margin: 0 0 0.5rem;
  font-weight: 700;
}

.product-name {
  font-family: $ff_second;
  color: $accent-dark;
  margin: 0;
  font-weight: 500;
  font-size: 1.1rem;
}

.review-form {
  display: flex;
  flex-direction: column;
  gap: 1.75rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;

  @media (max-width: $tablet) {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }
}

.form-group {
  @include form-group;
  position: relative;

  label {
    font-family: $ff_second;
    color: $txt;
    font-size: 0.95rem;
    font-weight: 500;
  }

  //   input,
  //   textarea {
  //     font-family: $ff_main;
  //     padding: 0.85rem 1.25rem;
  //     border: 1px solid #e0e0e0;
  //     border-radius: $btn_radius;
  //     transition: $default_transition;
  //     width: 100%;
  //     background-color: #f9f9f9;

  //     &:focus {
  //       outline: none;
  //       border-color: $accent;
  //       box-shadow: 0 0 0 2px rgba($accent, 0.15);
  //       background-color: $white;
  //     }
  //   }

  textarea {
    min-height: 120px;
    resize: vertical;
  }
}

.char-counter {
  position: absolute;
  right: 0.75rem;
  bottom: 0.75rem;
  font-family: $ff_second;
  font-size: 0.8rem;
  color: #999;
}

.image-upload {
  margin-top: 0.5rem;

  label {
    font-family: $ff_second;
    color: $txt;
    font-size: 0.95rem;
    font-weight: 500;
    display: block;
    margin-bottom: 0.75rem;
  }

  .upload-area {
    border: 2px dashed #e0e0e0;
    border-radius: $btn_radius;
    padding: 1.5rem;
    cursor: pointer;
    transition: $default_transition;

    &:hover {
      border-color: $accent;
      background-color: rgba($accent, 0.05);
    }
  }

  .upload-placeholder {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    color: $accent-dark;

    p {
      margin: 0;
      font-family: $ff_second;
      font-size: 0.95rem;
    }
  }

  .image-preview-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;

    @media (max-width: $tablet) {
      grid-template-columns: repeat(2, 1fr);
    }

    @media (max-width: $mobile) {
      grid-template-columns: 1fr;
    }
  }

  .image-preview {
    position: relative;
    height: 120px;
    border-radius: 8px;
    overflow: hidden;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .remove-image {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
      width: 24px;
      height: 24px;
      background-color: rgba($black, 0.7);
      color: $white;
      border: none;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.1rem;
      transition: $default_transition;

      &:hover {
        background-color: $error;
      }
    }
  }

  .add-more {
    height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px dashed $accent;
    border-radius: 8px;
    color: $accent;
    font-size: 2rem;
    font-weight: 300;
    transition: $default_transition;

    &:hover {
      background-color: rgba($accent, 0.1);
    }
  }

  .upload-hint {
    margin-top: 0.75rem;
    font-family: $ff_second;
    font-size: 0.85rem;
    color: #999;
    text-align: center;
  }
}

.submit-button {
  font-family: $ff_main;
  background-color: $accent;
  color: $white;
  border: none;
  border-radius: $btn_radius;
  padding: 1rem;
  font-size: 1.1rem;
  font-weight: 500;
  cursor: pointer;
  transition: $default_transition;
  margin-top: 1rem;
  width: 100%;

  &:hover {
    background-color: $accent-dark;
    box-shadow: $btn-accent-hover-shadow;
  }

  &:active {
    background-color: $btn-accent-active;
    transform: translateY(2px);
  }
}

@media (max-width: $tablet) {
  .modal-content {
    padding: 1.75rem;
  }

  .modal-title {
    font-size: 1.5rem;
  }

  .product-name {
    font-size: 1rem;
  }
}

@media (max-width: $mobile) {
  .modal-content {
    padding: 1.5rem;
  }

  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>
