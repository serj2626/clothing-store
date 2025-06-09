export interface ICategoryResponse {
  id: string;
  name: string;
  slug: string;
  image: string | null;
  children?: ICategoryResponse[];
  is_active: boolean;
}
