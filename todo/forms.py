from django import forms
from django.forms import ModelForm

from .models import *


class user_task_Forms(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = ('__all__')
class user_todo_form(forms.ModelForm):
    class Meta:
        model=UserTodo
        fields=('__all__')