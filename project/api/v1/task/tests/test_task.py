from apps.file.models import File
from apps.task.models import Task, TaskTypeChoices
from apps.user.models import User
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase


class TaskTests(APITestCase):
    def setUp(self):
        # Создаем пользователя через mixer и аутентифицируем его
        self.user = mixer.blend(User, username="testuser")
        self.user.set_password("testpassword")
        self.user.save()
        self.client.force_authenticate(user=self.user)

        # Создаем файлы, которые будем добавлять в attachments задачи
        self.file1 = mixer.blend(File)
        self.file2 = mixer.blend(File)

    def test_create_task(self):
        # URL для создания задачи
        url = reverse("api_v1:api-root:task-list")

        # Данные для создания задачи
        data = {
            "name": "Test Task",
            "description": "Description of test task",
            "status": TaskTypeChoices.OPEN,
            "due_date": "2024-11-12T19:57:40.476Z",
            "attachments": [
                str(self.file1.id),
                str(self.file2.id),
            ],  # IDs созданных файлов
            "assignees": [
                str(self.user.id)
            ],  # ID пользователя как назначенного исполнителя
            "creator": str(self.user.id),  # ID пользователя как создателя задачи
        }

        # Выполняем POST-запрос для создания задачи
        response = self.client.post(url, data, format="json")

        # Проверяем статус ответа и содержание созданного объекта задачи
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

        # Получаем созданную задачу и проверяем поля
        task = Task.objects.get()
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.description, "Description of test task")
        self.assertEqual(task.status, TaskTypeChoices.OPEN)
        self.assertEqual(task.due_date.isoformat(), "2024-11-12T19:57:40.476000+00:00")
        self.assertEqual(list(task.attachments.all()), [self.file1, self.file2])
        self.assertIn(self.user, task.assignees.all())
        self.assertEqual(task.creator, self.user)


class TaskDeleteTests(APITestCase):
    def setUp(self):
        # Создаем и аутентифицируем пользователя
        self.user = mixer.blend(User, username="testuser")
        self.user.set_password("testpassword")
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.task = mixer.blend(Task, creator=self.user, assignees=self.user)
        # Создаем задачу

    def test_delete_task(self):
        # URL для удаления задачи (используем task-detail для конкретной задачи)
        url = reverse("api_v1:api-root:task-detail", args=[str(self.task.id)])

        # Выполняем DELETE-запрос для удаления задачи
        response = self.client.delete(url)
        # Проверяем статус ответа и отсутствие задачи в базе данных
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.filter(id=self.task.id).count(), 0)
