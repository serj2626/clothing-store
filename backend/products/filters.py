import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.NumberFilter(field_name='category')
    brand = django_filters.NumberFilter(field_name='brand')
    gender = django_filters.CharFilter(field_name='gender')

    class Meta:
        model = Product
        fields = ['category', 'brand', 'gender']
