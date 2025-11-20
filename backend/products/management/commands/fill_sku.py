from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):
    help = "Заполняет поле SKU для всех существующих товаров"

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        self.stdout.write(f"Найдено товаров: {products.count()}")

        for product in products:
            sku = product.generate_sku()
            Product.objects.filter(pk=product.pk).update(sku=sku)
            self.stdout.write(f"SKU для {product.title} установлен: {sku}")

        self.stdout.write(self.style.SUCCESS("Все SKU заполнены!"))
