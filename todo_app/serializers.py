from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TodoItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class TodoItemSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = TodoItem
        fields = [
            "id",
            "title",
            "description",
            "created_date",
            "due_date",
            "status",
            "status_display",
            "user",
        ]
        read_only_fields = ["created_date", "user"]
