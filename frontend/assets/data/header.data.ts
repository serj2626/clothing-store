import { HeroIcons } from "../icons/types/hero-icons";

interface IHeaderLink {
  title: string;
  name: string;
  to: string;
}

export const headerLinks: IHeaderLink[] = [
  { title: "Главная", name: "index", to: "/" },
  { title: "Каталог", name: "catalog", to: "/catalog" },
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
    icon: HeroIcons.user,
    to: "/account",
  },
  {
    name: "favorite",
    icon: HeroIcons.heart,
    to: "/favorite",
  },
  {
    name: "basket",
    icon: HeroIcons.basket,
    to: "/basket",
  },
];

interface IModalMenu {
  title: string;
  url: string;
  icon?: string;
}

export const menuModalLinks: IModalMenu[] = [
  { title: "Главная", url: "/", icon: HeroIcons.home },
  { title: "Каталог", url: "/catalog", icon: HeroIcons.catalog },
  { title: "О нас", url: "/about", icon: HeroIcons.about },
  { title: "Контакты", url: "/contacts", icon: HeroIcons.PHONE },
  { title: "Личный кабинет", url: "/account", icon: HeroIcons.user },
  { title: "Избранное", url: "/favorite", icon: HeroIcons.heart },
  { title: "Корзина", url: "/basket", icon: HeroIcons.basket },
];
