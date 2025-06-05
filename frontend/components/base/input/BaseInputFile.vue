<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const fileName = defineModel("inputFile");
const fileInputRef = ref<HTMLInputElement | null>(null);
const totalName = ref("");

const totalFileName = computed(() => {
  if (totalName.value.length > 6) {
    const ext = totalName.value.split(".");
    return `${ext[0].slice(0, 6)}...${ext[1]}`;
  }
  return totalName.value;
});

function handleFileChange(event: Event) {
  console.log("event file", event);
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0] ?? null;

  if (file) {
    fileName.value = file;
    totalName.value = file.name;
    console.log("file", file);
  }
}

function clearFile() {
  fileName.value = "";
  if (fileInputRef.value) fileInputRef.value.value = "";
}
</script>
<template>
  <div class="base-input-file">
    <input
      type="file"
      id="fileInput"
      class="base-input-file__input"
      ref="fileInputRef"
      @change="handleFileChange"
    />
    <label for="fileInput" class="base-input-file__label">
      📁 Выбери файл
    </label>

    <div v-if="fileName" class="base-input-file__info">
      <p class="base-input-file__name">
        <span class="base-input-file__name-check">
          <Icon
            class="base-input-file__name-check-icon"
            :name="HeroIcons.CHECK"
            size="18"
          />
        </span>
        {{ totalFileName }}
      </p>
      <button class="base-input-file__remove" @click="clearFile">
        Удалить <Icon :name="HeroIcons.CLOSE" size="22" />
      </button>
    </div>
  </div>
</template>
<style scoped lang="scss">
.base-input-file {
  display: flex;
  align-items: center;
  justify-content: space-between;

  &__input {
    display: none;
  }

  &__label {
    display: inline-block;
    padding: 10px 20px;
    background-color: transparent;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    transition: box-shadow 0.3s ease;

    &:hover {
      box-shadow: 0 0 10px white;
    }
  }

  &__info {
    display: flex;
    gap: 10px;
    align-items: center;
    font-size: 14px;
  }

  &__name {
    color: $txt;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 5px;
    &-check {
      display: flex;
      align-items: center;
      background-color: green;
      color: $white;
    }
  }

  &__remove {
    position: relative;
    display: flex;
    align-items: center;
    color: $error;
    font-size: 14px;
    cursor: pointer;
    transition: color 0.2s;
    &:before {
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0;
      height: 1px;
      background-color: $error;
    }

    &:hover:before {
      transition: width 0.2s ease;
      width: 100%;
    }
  }
}
</style>
