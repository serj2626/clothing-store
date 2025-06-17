import type {
  IProduct,
  IProductImage,
  IProductVariant,
  IReview,
} from "~/types";

import { api } from "~/api";

export const useProductDetailStore = defineStore("productDetail", () => {
  const product = ref<IProduct>({
    id: "",
    brand: null,
    title: "",
    category: "",
    avatar: "",
    price: "",
    currency: "",
    is_active: true,
    count_likes: 0,
    count_reviews: 0,
    total_count: 0,
    details: [],
  });
  const reviews = ref<IReview[]>([]);
  const loading = ref(false);
  const images = ref<IProductImage[]>([]);
  const variants = ref<IProductVariant[]>([]);

  function setDataByProductStore(data: IProduct) {
    product.value.id = data.id;
    product.value.brand = data.brand;
    product.value.title = data.title;
    product.value.category = data.category;
    product.value.avatar = data.avatar;
    product.value.price = data.price;
    product.value.currency = data.currency;
    product.value.is_active = data.is_active;
    product.value.count_likes = data.count_likes;
    product.value.count_reviews = data.count_reviews;
    product.value.total_count = data.total_count;
    product.value.details = data.details;
  }

  const fetchProduct = async (id: string) => {
    const { $api } = useNuxtApp();
    loading.value = true;
    try {
      const data: IProduct = await $api(api.products.detail(id));

      images.value = data.images || [];
      variants.value = data.variants || [];
      reviews.value = data.reviews || [];
      setDataByProductStore(data);
    } finally {
      loading.value = false;
    }
  };

  const clearDataByProductStore = () => {
    product.value.id = "";
    product.value.brand = null;
    product.value.title = "";
    product.value.category = "";
    product.value.avatar = "";
    product.value.price = "";
    product.value.currency = "";
    product.value.is_active = true;
    product.value.count_likes = 0;
    product.value.count_reviews = 0;
    product.value.total_count = 0;

    images.value = [];
    variants.value = [];
    reviews.value = [];
  };

  return {
    product,
    variants,
    reviews,
    images,
    fetchProduct,
    loading,
    clearDataByProductStore,
  };
});
