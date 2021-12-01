from django.contrib import admin
from .models import Todo


# Customize what the admin UI looks like
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todo, TodoAdmin)
