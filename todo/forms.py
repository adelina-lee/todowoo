from django.forms import ModelForm
from .models import Todo

# Create TodoForm class + your own fields
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']

