import { HeroIcons } from "../icons/types/hero-icons";

interface IHeaderChild {
  label: string;
  icon: string;
  link: string;
}

interface IHeaderLink {
  label: string;
  icon?: string;
  to?: string;
  type: "link" | "chat";
  children?: IHeaderChild[];
}

export const headerLinks = ref<IHeaderLink[]>([
  {
    label: "Документы",
    icon: HeroIcons.DOWN,
    type: "link",
    children: [
      {
        label: "Оферта",
        icon: "i-lucide-house",
        link: "/offerta",
      },
      {
        label: "Политика",
        icon: "i-lucide-cloud-download",
        link: "/policy",
      },
      {
        label: "Cookie",
        icon: "i-lucide-cloud-download",
        link: "/cookies",
      },
    ],
  },
  {
    label: "Услуги",
    icon: HeroIcons.DOWN,
    to: "/services",
    type: "link",
  },
  {
    label: "Поддержка",
    type: "chat",
  },
  {
    label: "Тарифы",
    to: "/tariffs",
    type: "link",
  },
  {
    label: "О компании",
    icon: HeroIcons.DOWN,
    type: "link",
    children: [
      {
        label: "О нас",
        icon: "i-lucide-house",
        link: "/about",
      },
      {
        label: "Контакты",
        icon: "heroicons:map-pin",
        link: "/contacts",
      },
    ],
  },
]);
