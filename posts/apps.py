from django.apps import AppConfig


# Define the configuration for the 'posts' app
class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    