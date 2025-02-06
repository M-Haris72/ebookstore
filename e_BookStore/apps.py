from django.apps import AppConfig

class EBookStoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e_BookStore'

    def ready(self):
        import e_BookStore.signals  # Connects signals for the Profile model
