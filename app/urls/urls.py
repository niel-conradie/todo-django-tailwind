from django.urls import path

from app.views import HomePageView


app_name = "app"
urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
]
