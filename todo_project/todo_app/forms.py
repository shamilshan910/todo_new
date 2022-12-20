from django import forms
from .models import task_holder

class todo_form(forms.ModelForm):
    class Meta:
        model=task_holder
        fields=['name','priority','date']
