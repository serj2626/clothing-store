import type { IProduct } from "~/types";
import type { IReviewItem } from "~/types/reviews/reviews";
import { api } from "~/api";

export const useProductDetailStore = defineStore("productDetail", () => {
  // PRODUCT
  const product = ref<IProduct | null>(null);

  // LOADING
  const loading = ref(false);
  // IMAGES
  const images = ref<IProductImage[]>([]);
  // VARIANTS
  const variants = ref<IProductVariant[]>([]);

  // REVIEWS
  const reviews = ref<IReviewItem[]>([]);
  const currentPage = ref<number>(1);
  const nextPage = ref<number | null>(null);
  const prevPage = ref<number | null>(null);
  const countReviews = ref<number>(0);
  const errorGetReviews = ref<string | null>(null);

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
      setDataByProductStore(data);
    } finally {
      loading.value = false;
    }
  };

  async function fetchAllReviews(
    page: number = 1,
    page_size: number = 5,
    productId: string
  ) {
    const { $api } = useNuxtApp();
    try {
      const res = await $api<IReviewResponse>(
        api.products.commentsList(productId),
        {
          query: {
            page,
            page_size,
          },
        }
      );

      if (res.results) {
        if (page > 1) {
          reviews.value = [...reviews.value, ...res.results];
        } else {
          reviews.value = res.results;
        }
      }

      currentPage.value = page;
      countReviews.value = res.count ?? 0;
      nextPage.value = res.next;
      prevPage.value = res.previous;

      return res;
    } catch (e: unknown) {
      if (e instanceof Error) {
        errorGetReviews.value = e.message;
      } else {
        errorGetReviews.value = "Произошла ошибка получения отзывов";
      }
      throw e;
    }
  }

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

  function clearData() {
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

    reviews.value = [];
    images.value = [];
    variants.value = [];
  }

  return {
    product,
    variants,
    reviews,
    images,
    fetchProduct,
    fetchAllReviews,
    loading,
    clearDataByProductStore,
    clearData,
    countReviews,
    currentPage,
    nextPage,
    prevPage,
  };
});
