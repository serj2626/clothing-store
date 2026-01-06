export interface IReviewItem {
  id: number;
  name: string;
  text: string;
  advantages: string;
  disadvantages: string;
  rating: number;
  date: string;
  verified: boolean;
}

export const comments = ref<IReviewItem[]>([
  {
    id: 1,
    name: "Иван Иванович",
    text: "Все очень хорошо! Качество превзошло ожидания, ткань приятная к телу, не мнется. Буду заказывать еще!",
    advantages: "Отлично сидит",
    disadvantages: "Цена",
    rating: 5,
    date: "2 дня назад",
    verified: true,
  },
  {
    id: 2,
    name: "Мария Петрова",
    text: "Качество ткани порадовало, приятный цвет, хорошо тянется. Очень довольна покупкой!",
    advantages: "Мягкая и приятная ткань",
    disadvantages: "Долго ждала доставку",
    rating: 4,
    date: "1 неделю назад",
    verified: true,
  },
  {
    id: 3,
    name: "Алексей Смирнов",
    text: "Размер совпал идеально, как по меркам. Сидит как влитой, рекомендую!",
    advantages: "Соответствие размеру",
    disadvantages: "Нет ярких расцветок",
    rating: 5,
    date: "3 дня назад",
    verified: false,
  },
  {
    id: 4,
    name: "Екатерина Кузнецова",
    text: "Стильная и удобная одежда для повседневной носки. Носится хорошо, не выцветает.",
    advantages: "Современно выглядит",
    disadvantages: "Скользит на гладкой поверхности",
    rating: 4,
    date: "2 недели назад",
    verified: true,
  },
  {
    id: 5,
    name: "Дмитрий Орлов",
    text: "Товар соответствует описанию на 100%. Качественные материалы и хороший пошив.",
    advantages: "Приятная цена",
    disadvantages: "Швы немного торчат",
    rating: 4,
    date: "5 дней назад",
    verified: true,
  },
  {
    id: 6,
    name: "Ольга Соколова",
    text: "Хорошо подошло на подарок. Получатель был доволен, выглядит стильно и современно.",
    advantages: "Красивый цвет",
    disadvantages: "Не очень плотная ткань",
    rating: 3,
    date: "1 месяц назад",
    verified: false,
  },
  {
    id: 7,
    name: "Никита Волков",
    text: "Супер качество за свои деньги. Рекомендую к покупке, не пожалеете!",
    advantages: "Надёжный материал",
    disadvantages: "Нет вариантов размера XL",
    rating: 5,
    date: "2 недели назад",
    verified: true,
  },
  {
    id: 8,
    name: "Алина Федорова",
    text: "Очень комфортно носить каждый день. Не сковывает движения, приятная ткань.",
    advantages: "Удобная посадка",
    disadvantages: "Цвет отличается от фото",
    rating: 4,
    date: "3 дня назад",
    verified: true,
  },
  {
    id: 9,
    name: "Сергей Павлов",
    text: "Покупкой доволен полностью. Соотношение цена/качество на высоте.",
    advantages: "Простая стирка, не садится",
    disadvantages: "Маленький выбор моделей",
    rating: 5,
    date: "1 неделю назад",
    verified: false,
  },
  {
    id: 10,
    name: "Елена Никитина",
    text: "Заказ пришёл быстро, упаковка целая. Очень приятный на ощупь материал.",
    advantages: "Красиво смотрится",
    disadvantages: "Ткань могла бы быть плотнее",
    rating: 4,
    date: "4 дня назад",
    verified: true,
  },
]);
