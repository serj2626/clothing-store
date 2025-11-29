import type { IPagination } from "../common/pagination";

export interface IFaqItem {
  id: number;
  question: string;
  answer: string;
}

export interface IFaqResponse extends IPagination {
  results: IFaqItem[];
}
