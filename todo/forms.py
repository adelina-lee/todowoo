from django.forms import ModelForm
from .models import Todo


# Create TodoForm class + your own fields
class TodoForm(ModelForm):  # Inherit from ModelForm
    class Meta:
        model = Todo  # from models.py
        fields = ['title', 'memo', 'important']  # we want the title, memo, and important in the to-do creation
