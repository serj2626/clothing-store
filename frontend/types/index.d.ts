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

interface IProductVariant {
  color: string;
  color_name: string;
  size: string;
  quantity: number;
}
export interface IproductsResponse {
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
}

export interface IContactsResponse {
  type: string;
  second_type: string;
  value: string;
}
