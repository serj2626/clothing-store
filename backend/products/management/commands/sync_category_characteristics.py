from django.core.management.base import BaseCommand

from products.models import Category, CategoryCharacteristic, ProductVariant


class Command(BaseCommand):
    help = "Синхронизирует характеристики категорий на основе вариантов товаров"

    def handle(self, *args, **options):
        self.stdout.write("Начинаем синхронизацию характеристик категорий...\n")

        categories = Category.objects.all()
        created_count = 0
        skipped_count = 0

        for category in categories:
            self.stdout.write(f"Обработка категории: {category.name}")

            # Все варианты товаров в категории
            variants = ProductVariant.objects.filter(product__category=category)

            colors = variants.values_list("color", flat=True).distinct()
            sizes = variants.values_list("size", flat=True).distinct()

            if not colors and not sizes:
                self.stdout.write("  → Нет характеристик. Пропускаем.\n")
                skipped_count += 1
                continue

            # Удаляем старые характеристики
            CategoryCharacteristic.objects.filter(category=category).delete()

            # Создаём новые
            for color_id in colors:
                for size_id in sizes:
                    CategoryCharacteristic.objects.create(
                        category=category,
                        color_id=color_id,
                        size_id=size_id,
                    )
                    created_count += 1

            self.stdout.write(f"  → Создано комбинаций: {len(colors) * len(sizes)}\n")

        self.stdout.write("\nГотово!")
        self.stdout.write(f"Всего создано: {created_count}")
        self.stdout.write(f"Категорий без характеристик: {skipped_count}")
