interface ILink {
  label: string;
  link: string;
  type?: "link" | "mailto" | "tel";
  children?: ILink[];
}

export const footerLinks: ILink[] = [
  {
    label: "КОМПАНИЯ",
    link: "/",
    children: [
      {
        label: "О нас",
        link: "/",
      },
      {
        label: "Контакты",
        link: "/",
      },
    ],
  },
  {
    label: "ПОЛЕЗНОЕ",
    link: "/",
    children: [
      {
        label: "О нас",
        link: "/",
      },
      {
        label: "Контакты",
        link: "/",
      },
      {
        label: "Бонусная система",
        link: "/",
      },
    ],
  },
  {
    label: "ПОКУПАТЕЛЮ",
    link: "/",
    children: [
      {
        label: "Избранное",
        link: "/",
      },
      {
        label: "Публичная оферта",
        link: "/",
      },
      {
        label: "Политика конфиденциальности",
        link: "/",
      },
    ],
  },
  {
    label: "КОНТАКТЫ",
    link: "/",
    children: [
      {
        label: "+38(073) 096 36 44",
        link: "/",
        type: "tel",
      },
      {
        label: "info@yanki.com",
        link: "/",
        type: "mailto",
      },
    ],
  },
];
