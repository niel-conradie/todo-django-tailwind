from django.forms import ModelForm, CharField, TextInput, TimeField, TimeInput

from todo.models import TaskModel


class TaskModelForm(ModelForm):
    """
    A Django form used to create and update instances of the TaskModel model.

    Fields:
    - title (CharField): CharField with a label, max length, min length, and placeholder attributes.
    - time_start (TimeField): TimeField with a label and type attribute.
    - time_end (TimeField): TimeField with a label and type attribute.

    Class:
    - Meta: Provides metadata for the TaskModelForm class in Django.

    Methods:
    - __init__(self, *args, **kwargs): Initializes the form instance. Sets the label and required properties of the day field.
    """

    title = CharField(
        label="Title",
        max_length=15,
        min_length=2,
        required=True,
        widget=TextInput(
            attrs={
                "placeholder": "Task",
            },
        ),
    )

    time_start = TimeField(
        label="Time Start",
        required=True,
        widget=TimeInput(
            attrs={
                "type": "time",
            },
        ),
    )

    time_end = TimeField(
        label="Time End",
        required=True,
        widget=TimeInput(
            attrs={
                "type": "time",
            },
        ),
    )

    class Meta:
        """
        Provides metadata for the TaskModelForm class in Django.

        Fields:
        - title (CharField): The title of the task.
        - day (ForeignKey): The day associated with the task.
        - time_start (TimeField): The start time of the task.
        - time_end (TimeField): The end time of the task.
        """

        model = TaskModel
        fields = (
            "title",
            "day",
            "time_start",
            "time_end",
        )

    def __init__(self, *args, **kwargs):
        """
        Initializes the TaskModelForm instance.

        Sets the label and required properties of the day field.
        """

        super(TaskModelForm, self).__init__(*args, **kwargs)

        self.fields["day"].label = "Day"
        self.fields["day"].required = True
