export interface ICatalogResponse {
    id:        string;
    name:      string;
    slug:      string;
    image:     null | string;
    children:  ICatalogResponse[];
    is_active: boolean;
}