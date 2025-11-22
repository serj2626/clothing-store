export interface IActiveFilters {
  [key: string]: Set<string>;
}

export interface ISelectActiveFilters {
  [key: string]: string[];
}

export interface IToogledFilters {
  charSlug: string;
  value: string;
}

export interface IOrdering {
  name: string;
  slug: string;
}