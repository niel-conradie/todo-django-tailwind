from django.urls import path

from app.views import (
    task_convert_view,
    task_create_view,
    task_delete_view,
    task_reset_view,
    task_update_view,
    home_page_view,
    index_page_view,
)


app_name = "app"
urlpatterns = [
    path("", index_page_view, name="index"),
    path("home/", home_page_view, name="home"),
    path("home/create/", task_create_view, name="task_create"),
    path("home/<str:slug>/<str:pk>/update/", task_update_view, name="task_update"),
    path("home/<str:slug>/<str:pk>/delete/", task_delete_view, name="task_delete"),
    path("home/<str:pk>/convert/", task_convert_view, name="task_convert"),
    path("home/reset/", task_reset_view, name="task_reset"),
]
