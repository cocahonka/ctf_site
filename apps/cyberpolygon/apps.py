from django.apps import AppConfig


class CyberpolygonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cyberpolygon"
    verbose_name = "Киберполигон"

    def ready(self):
        import apps.cyberpolygon.signals
