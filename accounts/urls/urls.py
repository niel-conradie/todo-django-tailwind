from django.urls import path

from accounts.views import (
    CustomLoginView,
    custom_logout_view,
    custom_profile_view,
    custom_signup_view,
)


app_name = "accounts"
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", custom_logout_view, name="logout"),
    path("profile/<str:pk>/", custom_profile_view, name="profile"),
    path("signup/", custom_signup_view, name="signup"),
]
