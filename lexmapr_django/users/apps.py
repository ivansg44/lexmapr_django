from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "lexmapr_django.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import lexmapr_django.users.signals  # noqa F401
        except ImportError:
            pass
