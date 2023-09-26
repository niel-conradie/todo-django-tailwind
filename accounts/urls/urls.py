from django.urls import path

from accounts.views import (
    CustomLoginView,
    custom_logout_view,
    custom_profile_change_view,
    custom_profile_view,
    custom_signup_view,
)


app_name = "accounts"
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", custom_logout_view, name="logout"),
    path("signup/", custom_signup_view, name="signup"),
    path("profile/<str:pk>/", custom_profile_view, name="profile"),
    path("profile/<str:pk>/change/", custom_profile_change_view, name="profile_change"),
]
