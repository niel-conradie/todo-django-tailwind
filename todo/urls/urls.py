from django.urls import path

from todo.views import (
    task_convert_view,
    task_create_view,
    task_delete_view,
    task_reset_view,
    task_update_view,
)


app_name = "todo"
urlpatterns = [
    path("create/", task_create_view, name="create"),
    path("<slug:slug>/<uuid:pk>/update/", task_update_view, name="update"),
    path("<slug:slug>/<uuid:pk>/delete/", task_delete_view, name="delete"),
    path("<uuid:pk>/convert/", task_convert_view, name="convert"),
    path("reset/", task_reset_view, name="reset"),
]
