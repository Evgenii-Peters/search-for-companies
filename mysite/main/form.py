from django.forms import ModelForm, TextInput
from .models import firm1


class TaskForm(ModelForm):
    class Meta:
        model = firm1
        fields = ["inn", "ogrn", "address", "name"]

