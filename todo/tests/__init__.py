from todo.tests.models.day import DayModelTests
from todo.tests.models.task import TaskModelTests
from todo.tests.views.convert import TaskConvertViewTests
from todo.tests.views.create import TaskCreateViewTests
from todo.tests.views.delete import TaskDeleteViewTests
from todo.tests.views.reset import TaskResetViewTests
from todo.tests.views.update import TaskUpdateViewTests


__all__ = [
    DayModelTests,
    TaskModelTests,
    TaskConvertViewTests,
    TaskCreateViewTests,
    TaskDeleteViewTests,
    TaskResetViewTests,
    TaskUpdateViewTests,
]
