import { HeroIcons } from "../icons/types/hero-icons";

interface IHeaderLink {
  title: string;
  name: string;
  to: string;
}

export const headerLinks: IHeaderLink[] = [
  { title: "Главная", name: "index", to: "/" },
  { title: "Каталог", name: "catalog", to: "/#catalog" },
  { title: "О нас", name: "about", to: "/about" },
  { title: "Контакты", name: "contacts", to: "/contacts" },
];

interface IHeaderIconLink {
  icon: string;
  name: string;
  to: string;
}

export const headerIconLinks: IHeaderIconLink[] = [
  {
    name: "account",
    icon: HeroIcons.USER_SOLID,
    to: "/account",
  },
  {
    name: "favorite",
    icon: HeroIcons.HEART_SOLID,
    to: "/favorite",
  },
  {
    name: "basket",
    icon: HeroIcons.BASKET,
    to: "/basket",
  },
];

interface IModalMenu {
  title: string;
  url: string;
  icon?: string;
}

export const menuModalLinks: IModalMenu[] = [
  { title: "Главная", url: "/", icon: HeroIcons.HOME_SOLID },
  { title: "Каталог", url: "/catalog", icon: HeroIcons.CATALOG_SOLID },
  { title: "О нас", url: "/about", icon: HeroIcons.ABOUT_SOLID },
  { title: "Контакты", url: "/contacts", icon: HeroIcons.PHONE_SOLID },
  { title: "Личный кабинет", url: "/account", icon: HeroIcons.USER_SOLID },
  { title: "Избранное", url: "/favorite", icon: HeroIcons.HEART_SOLID },
  { title: "Корзина", url: "/basket", icon: HeroIcons.BASKET },
];
