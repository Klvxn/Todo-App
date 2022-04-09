from django import forms
from .models import Todo


class TodoForm(forms.Form):
    model = Todo
    todo = forms.CharField(min_length=3, widget=forms.TextInput(attrs={'placeholder':'Create todo'}))
    note = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Add a short note'}))


class EditTodoForm(forms.ModelForm):
    note = forms.CharField(required=False, widget=forms.TextInput(), empty_value='')

    class Meta:
        model = Todo
        fields = ['todo', 'note', 'completed']

