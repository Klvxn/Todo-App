from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Todo(models.Model):

    todo = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-date_created",)
        verbose_name = "To-do"
        verbose_name_plural = "To-dos"

    def __str__(self):
        return f"{self.todo}"

    def get_absolute_url(self):
        return reverse("mytodo:todo-detail", args=[self.pk])
