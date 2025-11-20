from transliterate import slugify as ru_slugify


def get_path_for_product(instance, filename):
    return f"""
    products/{ru_slugify(instance.brand.name) or 'non'}/
    {ru_slugify(instance.category.name)}/
    {str(filename).lower()}"""
