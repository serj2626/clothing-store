export interface ICategory {
  title: string;
  slug: string;
}

export const categories: ICategory[] = [
  { title: "Каталог", slug: "catalog" },
  { title: "New", slug: "new" },
  { title: "Bestsellers", slug: "bestsellers" },
  { title: "Верхняя одежда", slug: "outerwear" },
  { title: "Шубы", slug: "fur-coats" },
  { title: "Тренчи", slug: "trench-coats" },
  { title: "Пальто", slug: "coats" },
  { title: "Пуховики и жилеты", slug: "down-jackets" },
  { title: "Костюмы", slug: "suits" },
  { title: "Жакеты", slug: "jackets" },
  { title: "Платья", slug: "dresses" },
  { title: "Рубашки и блузы", slug: "shirts-blouses" },
  { title: "Юбки", slug: "skirts" },
  { title: "Футболки и топы", slug: "tshirts-tops" },
  { title: "Аксессуары", slug: "accessories" },
  { title: "Sale", slug: "sale" },
  { title: "Summer", slug: "summer" },
  { title: "Посмотреть всё", slug: "all" },
];
