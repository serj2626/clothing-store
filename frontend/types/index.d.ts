export interface ICategoryResponse {
  name: string;
  slug: string;
  image: string;
  children?: ICategoryResponse[];
}
