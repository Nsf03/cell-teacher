"""Application configuration for Cell Teacher main module.

Configures Django app settings for the main application.
"""
from django.apps import AppConfig


class MainConfig(AppConfig):
    """Configuration class for the main app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
