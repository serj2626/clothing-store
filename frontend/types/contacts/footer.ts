export interface IFooterDataResponse {
  site_name: string;
  copyright: string;
  links: IFooterLinkGroup[];
}

export interface IFooterLinkGroup {
  name: string;
  items: IFooterLinkItem[];
}

export interface IFooterLinkItem {
  name: string;
  url: string;
}
