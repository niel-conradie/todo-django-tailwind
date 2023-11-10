from django import forms

from app.models import TaskModel


class TaskModelForm(forms.ModelForm):
    title = forms.CharField(
        label="Task",
        max_length=100,
        min_length=2,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "",
                "placeholder": "Task Title",
            },
        ),
    )

    time_start = forms.TimeField(
        label="Time Start",
        required=True,
        widget=forms.TimeInput(
            attrs={
                "class": "",
                "type": "time",
            },
        ),
    )

    time_end = forms.TimeField(
        label="Time End",
        required=True,
        widget=forms.TimeInput(
            attrs={
                "class": "",
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

        self.fields[
            "title"
        ].help_text = (
            '<span class=""><small>Required. 100 characters or fewer.</small></span>'
        )

        self.fields["day"].label = "Day"
        self.fields["day"].required = True
        self.fields[
            "day"
        ].help_text = '<span class=""><small>Required. Day of the Week.</small></span>'

        self.fields[
            "time_start"
        ].help_text = '<span class=""><small>Required. Time of the Day.</small></span>'

        self.fields[
            "time_end"
        ].help_text = '<span class=""><small>Required. Time of the Day.</small></span>'
