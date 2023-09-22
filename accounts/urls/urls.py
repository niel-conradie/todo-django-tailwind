from django.urls import path

from accounts.views import LoginPageView


app_name = "accounts"
urlpatterns = [
    path("login/", LoginPageView.as_view(), name="login"),
]
