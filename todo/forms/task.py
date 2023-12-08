from django import forms

from todo.models import TaskModel


class TaskModelForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        max_length=15,
        min_length=2,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Task",
            },
        ),
    )

    time_start = forms.TimeField(
        label="Time Start",
        required=True,
        widget=forms.TimeInput(
            attrs={
                "type": "time",
            },
        ),
    )

    time_end = forms.TimeField(
        label="Time End",
        required=True,
        widget=forms.TimeInput(
            attrs={
                "type": "time",
            },
        ),
    )

    class Meta:
        model = TaskModel
        fields = (
            "title",
            "day",
            "time_start",
            "time_end",
        )

    def __init__(self, *args, **kwargs):
        super(TaskModelForm, self).__init__(*args, **kwargs)

        self.fields["day"].label = "Day"
        self.fields["day"].required = True
