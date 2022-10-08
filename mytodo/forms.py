from django import forms

from .models import Todo


class TodoForm(forms.Form):

    todo = forms.CharField(
        label="To-do",
        min_length=3,
        widget=forms.TextInput(attrs={"placeholder": "Add to-do"}),
    )
    note = forms.CharField(
        label="Note",
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "A short note about the to-do"}),
    )


class EditTodoForm(forms.ModelForm):

    note = forms.CharField(
        label="Note",
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "A short note about the to-do"}),
        empty_value="",
    )

    class Meta:
        model = Todo
        fields = ["todo", "note", "completed"]
        labels = {"todo": "To-do", "completed": "Completed"}
