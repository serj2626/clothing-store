from contacts.models import FAQ


def generate_faq_json_ld():
    """
    Генерирует JSON-LD для всех FAQ и возвращает словарь для seo.json_ld
    """
    faqs = FAQ.objects.all()
    main_entity = []

    for faq in faqs:
        main_entity.append(
            {
                "@type": "Question",
                "name": faq.question,
                "acceptedAnswer": {"@type": "Answer", "text": faq.answer},
            }
        )

    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": main_entity,
    }
