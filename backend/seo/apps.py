from django.apps import AppConfig


class SeoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "seo"
    verbose_name = "№6 Настройки SEO и Конфигурация"

    def ready(self):
        from . import signals