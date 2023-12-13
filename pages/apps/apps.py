from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    Django configuration class for the "pages" app.

    Parameters:
    - AppConfig (class): Class representing a Django application and its configuration.

    Fields:
    - default_auto_field (str): The default auto field for the app, set to "django.db.models.BigAutoField".
    - name (str): The name of the app, set to "pages".
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "pages"
