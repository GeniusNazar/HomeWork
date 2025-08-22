from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOICES = [
        ("Треба робити", "Треба робити"),
        ("В процесі", "В процесі"),
        ("Зроблено", "Зроблено")
    ]

    PRIORITY_CHOICES = [
        ("Не обов'язково", "Не обов'язково"),
        ("Бажано", "Бажано"),
        ("Обов'язково", "Обов'язково")
    ]

    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title

