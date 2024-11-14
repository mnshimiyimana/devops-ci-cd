from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        title = self.title if self.title else "No Title"
        status = self.status if self.status else "Unknown Status"
        return f"{title} ({status})"

    class Meta:
        ordering = ["due_date", "created_date"]
