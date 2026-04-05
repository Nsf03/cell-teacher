\"\"\"Application configuration for Cell Teacher main module.\n\nConfigures Django app settings for the main application.\n\"\"\"\nfrom django.apps import AppConfig


class MainConfig(AppConfig):
    \"\"\"Configuration class for the main app.\"\"\"\n    default_auto_field = 'django.db.models.BigAutoField'\n    name = 'main'
