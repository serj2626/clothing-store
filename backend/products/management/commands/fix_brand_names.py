from django.core.management.base import BaseCommand

from products.models import Brand


class Command(BaseCommand):
    help = "Приводит названия всех категорий к title()"

    def handle(self, *args, **options):
        brands = Brand.objects.all()
        updated = 0
        self.stdout.write(f"Найдено брендов: {brands.count()}")

        for cat in brands:
            fixed = cat.name.title()

            if cat.name != fixed:
                cat.name = fixed
                cat.save(update_fields=["name"])
                updated += 1
                self.stdout.write(self.style.SUCCESS(f"Updated: {fixed}"))

        self.stdout.write(self.style.WARNING(f"Готово! Обновлено {updated} брендов."))
