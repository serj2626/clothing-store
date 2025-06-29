export interface ICategoryResponse {
  id: string;
  name: string;
  slug: string;
  image: string | null;
  children?: ICategoryResponse[];
  is_active: boolean;
}

interface IBrandProduct {
  id: string;
  name: string;
  description: string;
  country: string;
  image: null | string;
}

interface IProductImage {
  id: number | string;
  image: string;
}

interface IProductVariant {
  color: string;
  color_name: string;
  size: string;
  quantity: number;
}

interface IProductDetails {
  id: number;
  title: string;
  description: string;
}

interface IPhotoReview {
  id: number;
  alt: string;
  image: string;
}

export interface IReview {
  id: string;
  description: string;
  name: string;
  email: string;
  advantages: string;
  disadvantages: string;
  rating: number;
  is_published: boolean;
  likes?: [];
  dislikes?: [];
  time_age: string;
  created_at: string;
  updated_at: string;
  photos: IPhotoReview[];
}

export interface IReviewResponse {
  current: number;
  next: null | number;
  previous: null | number;
  count: number;
  results: IReview[];
}

export interface IProduct {
  id: string;
  brand: null | IBrandProduct;
  title: string;
  category: string;
  avatar: string;
  price: string;
  currency: string;
  is_active: boolean;
  count_likes: number;
  count_reviews: number;
  total_count: number | null;
  variants?: IProductVariant[] | null;
  images?: IProductImage[] | null;
  details?: IProductDetails[];
  liked: boolean;
}

export interface IProductResponse {
  current: number;
  next: null | number;
  previous: null | number;
  count: number;
  results: IProduct[];
}

export interface IContactsResponse {
  type: string;
  second_type: string;
  value: string;
}
