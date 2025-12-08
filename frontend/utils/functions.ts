interface FormField {
  value: string | boolean;
  error: string;
  required: boolean;
}

interface FormData {
  [key: string]: FormField;
}

/**
 * 
 * @param formData - форма
 * @returns 
 */
export const clearForm = (formData: FormData) => {
  for (const key in formData) {
    if (key === "remember") {
      formData[key].value = false;
      formData[key].error = "";
    } else {
      formData[key].value = "";
      formData[key].error = "";
    }
  }
};

/**
 * 
 * @param videoUrl  
 * @returns  
 */
export const getVideo = (videoUrl: string | undefined) => {
  return [useRuntimeConfig().public.mediaUrl, videoUrl].join("");
};

export const getMedia = (mediaContentUrl: string) => {
  return [useRuntimeConfig().public.mediaUrl, mediaContentUrl].join("");
};

export const formatNumber = (num: number): string => {
  return num.toLocaleString("ru-RU");
};

export const formatNumberCustom = (num: number, separator = " "): string => {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, separator);
};

export function formatDate(dateStr: string) {
  const date = new Date(dateStr);
  const day = date.getDate().toString().padStart(2, "0");
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const year = date.getFullYear();
  const hours = date.getHours().toString().padStart(2, "0");
  const minutes = date.getMinutes().toString().padStart(2, "0");
  const seconds = date.getSeconds().toString().padStart(2, "0");

  return `${year}/${month}/${day} ${hours}:${minutes}:${seconds}`;
}

export const getPhoto = (photoUrl?: string | null): string => {
  if (!photoUrl) {
    return "/img_not_found.webp";
  }

  const mediaUrl = useRuntimeConfig().public.mediaUrl;

  // Экранируем URL
  const encodedPhotoUrl = encodeURI(photoUrl);
  const cleanMediaUrl = mediaUrl.replace(/\/+$/, "");

  return `${cleanMediaUrl}/${encodedPhotoUrl}`;
};
