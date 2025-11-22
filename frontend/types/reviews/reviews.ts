import type { IPagination } from "../common/pagination";

export interface IReviewsResponse extends IPagination {
  results: IReviewItem[];
}

export interface IReviewItem {
  id: string;
  description: string;
  time_age: string;
  is_published: boolean;
  advantages: string;
  disadvantages: string;
  rating: number;
  user: IReviewUser;
  product: string;
  count_likes: number;
  count_dislikes: number;
  photos: IReviewPhoto[];
  replies: IReviewReply[];
}

export interface IReviewUser {
  email: string;
  first_name: string | null;
  last_name: string | null;
}

export interface IReviewPhoto {
  image: string;
}

export interface IReviewReply {
  author: string;
  description: string;
}
