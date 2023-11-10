from app.views.task.convert import task_convert_view
from app.views.task.create import task_create_view
from app.views.task.delete import task_delete_view
from app.views.task.reset import task_reset_view
from app.views.task.update import task_update_view
from app.views.home import home_page_view
from app.views.index import index_page_view


__all__ = [
    task_convert_view,
    task_create_view,
    task_delete_view,
    task_reset_view,
    task_update_view,
    home_page_view,
    index_page_view,
]
