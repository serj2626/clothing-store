interface IBreadcrumb {
  title: string;
  url: string;
}

export const catalogPageBreadcrumbs: IBreadcrumb[] = [
  { title: "Главная", url: "/" },
  { title: "Каталог", url: "/catalog" },
];

export const aboutPageBreadcrumbs: IBreadcrumb[] = [
  { title: "Главная", url: "/" },
  { title: "О нас", url: "/about" },
];

export const contactsPageBreadcrumbs: IBreadcrumb[] = [
  { title: "Главная", url: "/" },
  { title: "Контакты", url: "/contacts" },
];

export const accountPageBreadcrumbs: IBreadcrumb[] = [
  { title: "Главная", url: "/" },
  { title: "Личный кабинет", url: "/account" },
];

export const basketPageBreadcrumbs: IBreadcrumb[] = [
  { title: "Главная", url: "/" },
  { title: "Корзина", url: "/basket" },
];

export const favoritePageBreadcrumbs: IBreadcrumb[] = [
  { title: "Главная", url: "/" },
  { title: "Избранное", url: "/favorite" },
];

export const offertaPageBreadcrumbs: IBreadcrumb[] = [
  { title: "Главная", url: "/" },
  { title: "Оферта", url: "/offerta" },
];

export const policyPageBreadcrumbs: IBreadcrumb[] = [
  { title: "Главная", url: "/" },
  { title: "Политика конфиденциальности", url: "/policy" },
];
