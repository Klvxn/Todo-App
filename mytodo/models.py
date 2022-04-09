from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.todo}'

    def get_absolute_url(self):
        return reverse("mytodo:detailpage", kwargs={'pk':self.pk})

    