export interface ICategoryResponse {
  id: string;
  name: string;
  slug: string;
  image: string | null;
  children?: ICategoryResponse[];
  is_active: boolean;
}

interface IbrandProduct {
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
export interface IProduct {
  id: string;
  brand: null | IbrandProduct;
  title: string;
  category: string;
  avatar: string;
  price: string;
  currency: string;
  is_active: boolean;
  count_likes: number;
  count_reviews: number;
  total_count: number | null;
  variants: IProductVariant[];
  images: IProductImage[];
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
