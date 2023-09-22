from django.urls import path

from pages.views import IndexPageView


app_name = "pages"
urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
]
