import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User

# class TestTodoApi:
#     client = APIClient()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def common_user():
    return User.objects.create_user(
        username="admin313d",
        password="A/12345678",
        is_verified=True,
    )


@pytest.mark.django_db
class TestTodoApi:
    client = APIClient()

    def test_get_Todo_response_200_status(self, api_client):
        url = reverse("todo_app:api-v1:todo-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_Todo_response_401_status(self, api_client):
        url = reverse("todo_app:api-v1:todo-list")
        data = {
            "title": "test",
            "detail": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_Todo_response_201_status(self, common_user, api_client):
        url = reverse("todo_app:api-v1:todo-list")
        data = {
            "title": "test",
            "detail": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data, format="json")
        assert response.status_code == 201, response.data

    def test_create_Todo_invalid_data_response_400_status(
        self, common_user, api_client
    ):
        url = reverse("todo_app:api-v1:todo-list")
        data = {
            "title": "test",
            "content": "description",
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
