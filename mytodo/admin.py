from django.contrib import admin

from .models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = ["todo", "note", "completed", "user", "date_created"]
    list_filter = ("completed", "user")
    search_fields = ("todo", "user")
