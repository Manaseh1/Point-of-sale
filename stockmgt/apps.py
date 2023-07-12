from django.apps import AppConfig

class StockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stockmgt'

    def ready(self):
        import stockmgt.signals  # Import signals module

