from django.apps import AppConfig


class PatternsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patterns'

    def ready(self):
        import patterns.signals
