from django.urls import path

from pages.views import (
    home_page_view,
    index_page_view,
)


app_name = "pages"
urlpatterns = [
    path("", index_page_view, name="index"),
    path("home/", home_page_view, name="home"),
]
