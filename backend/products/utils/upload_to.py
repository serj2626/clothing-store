from transliterate import slugify as ru_slugify


def get_path_for_product(instance, filename):
    return f"""
    products/{ru_slugify(instance.brand.name) or 'non'}/
    {ru_slugify(instance.category.name)}/{instance.title}/
    {str(filename).lower()}"""


def get_path_for_product_variant(instance, filename):
    return f"""
    products/{ru_slugify(instance.product.brand.slug) or 'non'}/
    {ru_slugify(instance.product.category.name)}/{instance.product.title}/{instance.size}/{instance.color.title}/
    {str(filename).lower()}"""
