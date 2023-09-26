from django.urls import path

from accounts.views import CustomLoginView, custom_logout_view


app_name = "accounts"
urlpatterns = [
    path(route="login/", view=CustomLoginView.as_view(), name="login"),
    path(route="logout/", view=custom_logout_view, name="logout"),
]
