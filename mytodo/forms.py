from django import forms

from .models import Todo


class TodoForm(forms.Form):

    todo = forms.CharField(
        label="Todo",
        min_length=3,
        widget=forms.TextInput(attrs={"placeholder": "Add todo"}),
    )
    note = forms.CharField(
        label="Note",
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "A short note about the todo"}),
    )


class EditTodoForm(forms.ModelForm):

    note = forms.CharField(
        label="Note",
        widget=forms.Textarea(attrs={"placeholder": "A short note about the todo"}),
        empty_value="",
    )

    class Meta:
        model = Todo
        fields = ["todo", "note", "completed"]
        labels = {"todo": "Todo", "completed": "Completed"}
