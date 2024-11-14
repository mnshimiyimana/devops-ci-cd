import os
import pytest
from django.urls import resolve, reverse
from todo_app.views import TodoItemViewSet

os.environ["DJANGO_SETTINGS_MODULE"] = "todo_project.settings"


@pytest.mark.urls("todo_project.urls")
class TestURLConfiguration:
    def test_admin_url(self):
        assert reverse("admin:index") == "/admin/"
        assert resolve("/admin/").view_name == "admin:index"

    def test_todo_list_url(self):
        assert reverse("todo-list") == "/api/todos/"
        assert resolve("/api/todos/").func.cls == TodoItemViewSet

    def test_todo_detail_url(self):
        assert reverse("todo-detail", args=[1]) == "/api/todos/1/"
        assert resolve("/api/todos/1/").func.cls == TodoItemViewSet

    def test_api_auth_url(self):
        assert reverse("rest_framework:login") == "/api-auth/login/"
        assert resolve("/api-auth/login/").view_name == "rest_framework:login"
