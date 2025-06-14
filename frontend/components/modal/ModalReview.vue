<script setup lang="ts">
const modalsStore = useModalsStore();
defineProps({
  productName: {
    type: String,
    default: "Футболка хлопковая",
  },
});

const rating = ref(0);
const name = ref("");
const email = ref("");
const review = ref("");
const advantages = ref("");
const disadvantages = ref("");
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
</script>
<template>
  <div class="modal-review">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title">Оставить отзыв</h2>
        <p class="product-name">О товаре: {{ productName }}</p>
      </div>

      <div class="rating-section">
        <p class="rating-label">Ваша оценка:</p>
        <div class="stars">
          <span
            v-for="star in 5"
            :key="star"
            class="star"
            :class="{ active: star <= rating }"
            @click="rating = star"
          >
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12 17.27L18.18 21L16.54 13.97L22 9.24L14.81 8.63L12 2L9.19 8.63L2 9.24L7.46 13.97L5.82 21L12 17.27Z"
                :fill="star <= rating ? $accent - dark : '#ddd'"
              />
            </svg>
          </span>
        </div>
      </div>

      <div class="review-form">
        <div class="form-row">
          <div class="form-group">
            <label for="name">Ваше имя *</label>

            <BaseInput
              v-model:input-value="name"
              radius="8px"
              placeholder="Иван Иванов"
            />
          </div>

          <div class="form-group">
            <label for="email">Email</label>

            <BaseInput
              v-model:input-value="email"
              radius="8px"
              placeholder="example@mail.com"
            />
          </div>
        </div>

        <div class="form-group">
          <label for="review">Отзыв *</label>

          <BaseInputTextArea
            v-model:input-value="review"
            radius="8px"
            placeholder="Поделитесь впечатлениями о товаре"
          />
          <span class="char-counter">{{ review.length }}/500</span>
        </div>

        <div class="form-group">
          <label for="advantages">Достоинства</label>

          <BaseInputTextArea
            v-model:input-value="advantages"
            radius="8px"
            placeholder="Что вам понравилось?"
          />
        </div>

        <div class="form-group">
          <label for="disadvantages">Недостатки</label>

          <BaseInputTextArea
            v-model:input-value="disadvantages"
            radius="8px"
            placeholder="Что можно улучшить?"
          />
        </div>

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
          @click="modalsStore.closeModal('review')"
        />
      </div>
      <BaseButtonClose
        top="15px"
        right="15px"
        :size="30"
        @click="modalsStore.closeModal('review')"
      />
    </div>
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

.rating-section {
  margin-bottom: 2rem;
  text-align: center;
}

.rating-label {
  font-family: $ff_second;
  color: $txt;
  margin: 0 0 0.75rem;
  font-size: 1rem;
  font-weight: 500;
}

.stars {
  display: flex;
  justify-content: center;
  gap: 0.75rem;
}

.star {
  cursor: pointer;
  transition: $default_transition;

  &:hover {
    transform: scale(1.1);
  }

  &.active {
    svg path {
      fill: $accent-dark;
    }
  }
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
