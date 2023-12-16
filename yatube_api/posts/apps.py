"""App configuration."""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Class for app configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
