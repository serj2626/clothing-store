from import_export import fields, resources
from import_export.widgets import CharWidget, ForeignKeyWidget

from .models import Brand, Category, Product


class ProductResource(resources.ModelResource):
    brand = fields.Field(
        column_name='Brand',
        attribute='brand',
        widget=ForeignKeyWidget(
            Brand,
            'name',
        ),
    )
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'),
    )
    gender = fields.Field(column_name='Gender', attribute='gender', widget=CharWidget())

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'category', 'gender')
        import_id_fields = ('id',)
        skip_unchanged = True
        report_skipped = True

    def before_import_row(self, row, **kwargs):
        # Обработка категории
        category_name = row.get('Category')
        if category_name:
            category_obj, created = Category.objects.get_or_create(name=category_name)
            row['Category'] = (
                category_obj.id
            )  # чтобы ForeignKeyWidget корректно привязался
        # Обработка бренда (может быть null)
        brand_name = row.get('Brand')
        if brand_name:
            brand_obj, created = Brand.objects.get_or_create(name=brand_name)
            row['Brand'] = brand_obj.id

    def get_instance(self, instance_loader, row):
        """
        Логика: если id указан → обновляем объект,
        иначе создаём новый
        """
        obj_id = row.get('id')
        if obj_id:
            try:
                return Product.objects.get(id=obj_id)
            except Product.DoesNotExist:
                return None
        return None

    def after_import_row(self, row, row_result, **kwargs):
        print(f"Processed Product: {row.get('title')}")
