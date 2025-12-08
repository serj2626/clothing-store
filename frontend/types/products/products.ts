import type { IPagination } from "../common/pagination";

export interface IBrand {
  id: string;
  country: string;
  image: string | null;
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

export interface ILastProduct {
  id: string;
  brand: string;
  title: string;
  avatar: string;
  is_active: boolean;
  sku: string;
  price: string;
}

export interface IProduct extends ILastProduct {
  category: string;
  count_likes?: number;
  count_reviews?: number;
  total_count: number;
  variants?: IProductVariant[];
  liked?: boolean;
}

export interface IProductResponse extends IPagination {
  results: IProduct[];
}
