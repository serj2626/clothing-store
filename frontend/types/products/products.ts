import type { IPagination } from "../common/pagination";

export interface IBrand {
  id: string;
  country: string;
  image: string;
  name: string;
  description: string;
  slug: string;
}

export interface IProductVariant {
  id: number;
  color: string;
  color_code: string;
  size: string;
  quantity: number;
  status: string;
  image: string;
}

export interface IProduct {
  id: string;
  sku: string;
  brand: IBrand;
  title: string;
  category: string;
  avatar: string;
  is_active: boolean;
  count_likes: number;
  count_reviews: number;
  total_count: number;
  variants: IProductVariant[];
  liked: boolean;
  price: string;
}

export interface IProductResponse extends IPagination {
  results: IProduct[];
}
