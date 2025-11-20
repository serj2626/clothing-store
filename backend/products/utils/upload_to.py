from transliterate import slugify as ru_slugify
import os


def get_path_for_product(instance, filename):
    brand = ru_slugify(instance.brand.name) if instance.brand else "non"
    category = (
        ru_slugify(instance.category.name) if instance.category else "category"
    )
    title = ru_slugify(instance.title)

    filename = filename.lower()

    return os.path.join(
        "products",
        brand,
        category,
        title,
        filename,
    )


def get_path_for_product_variant(instance, filename):
    product = instance.product

    brand = ru_slugify(product.brand.slug) if product.brand else "non"
    category = (
        ru_slugify(product.category.name) if product.category else "category"
    )
    title = ru_slugify(product.title)

    size = ru_slugify(instance.size)
    color = ru_slugify(instance.color.title) if instance.color else "color"

    filename = filename.lower()

    return os.path.join(
        "products",
        brand,
        category,
        title,
        size,
        color,
        filename,
    )
