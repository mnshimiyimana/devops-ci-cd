from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings
from .models import TodoItem
from .serializers import TodoItemSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        todo_item = serializer.save(user=self.request.user)
        self._send_notification_email(todo_item, "created")

    def perform_update(self, serializer):
        todo_item = serializer.save()
        if "status" in self.request.data:
            self._send_notification_email(todo_item, "updated")

    def _send_notification_email(self, todo_item, action):
        subject = f"Todo Item {action.title()}"
        message = f"""
        Your todo item has been {action}:
        
        Title: {todo_item.title}
        Status: {todo_item.get_status_display()}
        Due Date: {todo_item.due_date}
        """

        send_mail(
            subject,
            message,
            "noreply@todoapp.com",
            [self.request.user.email],
            fail_silently=True,
        )

    @action(detail=False, methods=["get"])
    def status_counts(self, request):
        counts = {}
        for status, _ in TodoItem.STATUS_CHOICES:
            counts[status] = self.get_queryset().filter(status=status).count()
        return Response(counts)
