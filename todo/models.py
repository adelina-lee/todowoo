from django.db import models
from django.contrib.auth.models import User


# To do list
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)  # blank=True - not compulsory
    created = models.DateTimeField(auto_now_add=True, blank=True)  # Instantly specified created value at time
    datecompleted = models.DateTimeField(null=True)  # After clicking complete
    important = models.BooleanField(default=False)  # Mark important
    # Stores relationship with this to do and user - one to many relationship
    # One user can have many todos
    user = models.ForeignKey(User, on_delete=models.CASCADE)

