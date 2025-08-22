from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]

        def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({"class": "form-control"})

            self.fields["due_date"].widget.attrs["class"] += "my-custom=datepicker"


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "Всі"),
        ("Треба робити", "Треба робити"),
        ("В процесі", "В процесі"),
        ("Зроблено", "Зроблено")
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус")

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs.update({"class": "form-control"})



