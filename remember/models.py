import uuid
from django.db import models
from django.urls import reverse
# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный номер пользователя")

    first_name = models.CharField(max_length=100, help_text='Имя пользователя')
    last_name = models.CharField(max_length=100, help_text='Фамилия пользователя')
    log_in = models.BooleanField(help_text='Состояние авторизации пользователя')
    facebook_id = models.CharField(max_length=100, help_text='Facebook ID пользователя')

    def __str__(self):
        return f'{self.id}, {self.first_name}, {self.last_name}'


class Remember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный номер воспоминания")

    title = models.CharField(max_length='200', help_text='Название воспоминания')
    description = models.TextField(max_length=2000, help_text='Описание воспоминания')
    remembers = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id}, {self.title}'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])