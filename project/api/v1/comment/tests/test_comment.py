import pytest
from apps.comment.models import Comment
from apps.task.models import Task
from apps.user.models import User
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase


@pytest.mark.django_db
class TestCommentAPI(APITestCase):
    def setUp(self):
        # Создаем пользователя через mixer и аутентифицируем его
        self.user = mixer.blend(User, username="testuser")
        self.user.set_password("testpassword")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_comment(self):
        self.task = mixer.blend(
            Task, name="test_task", assignees=self.user, creator=self.user
        )
        url = reverse(
            "api_v1:api-root:comment-list"
        )

        data = {
            "text": "This is a test comment",
            "task": str(self.task.id),
            "author": str(self.user.id),
        }

        response = self.client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert Comment.objects.count() == 1
        assert Comment.objects.first().text == "This is a test comment"

    def test_get_comment_list(self):
        self.task = mixer.blend(
            Task, name="test_task", assignees=self.user, creator=self.user
        )
        mixer.blend(Comment, task=self.task, author=self.user, text="Comment 1")
        mixer.blend(Comment, task=self.task, author=self.user, text="Comment 2")

        url = reverse("api_v1:api-root:comment-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 2

    def test_update_comment(self):
        self.task = mixer.blend(
            Task, name="test_task", assignees=self.user, creator=self.user
        )
        comment = mixer.blend(
            Comment, task=self.task, author=self.user, text="Old comment text"
        )

        url = reverse("api_v1:api-root:comment-detail", args=[str(comment.id)])
        data = {"text": "Updated comment text"}
        response = self.client.patch(url, data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["text"] == "Updated comment text"
