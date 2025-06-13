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
        link: "/about",
      },
      {
        label: "Контакты",
        link: "/contacts",
      },
    ],
  },
  {
    label: "ПОЛЕЗНОЕ",
    link: "/",
    children: [
      {
        label: "Оплата и доставка",
        link: "/delivery",
      },
      {
        label: "Условия возврата",
        link: "/return",
      },
      {
        label: "Бонусная система",
        link: "/bonus",
      },
    ],
  },
  {
    label: "ПОКУПАТЕЛЮ",
    link: "/",
    children: [
      {
        label: "Избранное",
        link: "/favorite",
      },
      {
        label: "Публичная оферта",
        link: "/offerta",
      },
      {
        label: "Политика конфиденциальности",
        link: "/policy",
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
