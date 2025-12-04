from products.models import Product


def generate_json_ld_by_pruduct(product: Product):
    """
    JSON-LD для продукта
    """
    product_json_ld = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": product.title or "Товар",
        "image": product.avatar.url if product.avatar else None,
        "description": product.description,
        "sku": product.sku or "",
        "brand": {
            "@type": "Brand",
            "name": product.brand.name if product.brand else "",
        },
        "offers": {
            "@type": "Offer",
            "priceCurrency": "RUB",
            "price": str(product.price),
            "availability": (
                "https://schema.org/InStock"
                if product.is_active
                else "https://schema.org/OutOfStock"
            ),
            "url": f"/products/{product.id or product.slug}/",
        },
    }

    return product_json_ld
