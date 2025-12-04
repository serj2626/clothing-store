export interface AvailableColors {
  title: string;
  slug: string;
}

export interface AvailableSizes {
  title: string;
}

export interface ICatalogResponse {
  id: string;
  name: string;
  slug: string;
  image?: null | string;
  children: ICatalogResponse[];
  is_active: boolean;
  has_children?: boolean;
  available_colors?: AvailableColors[];
  available_sizes?: AvailableSizes[];
}
