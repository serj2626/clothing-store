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
  id: number;
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

interface IReview {
  id: string;
  description: string;
  created_at: string;
  updated_at: string;
  name: string;
  email: string;
  advantages: string;
  disadvantages: string;
  rating: number;
  is_published: boolean;
  user: string;
  product: string;
  likes?: [];
  dislikes?: [];
  time_age: string;
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
  reviews?: IReview[];
  details?: IProductDetails[];
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
