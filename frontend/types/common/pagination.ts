export interface IPagination {
  current: number;
  next: null | number;
  previous: null | number;
  count: number;
  total_pages: number;
}