import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Remember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный номер воспоминания")

    title = models.CharField(max_length=200, help_text='Название воспоминания')
    description = models.TextField(max_length=2000, help_text='Описание воспоминания')
    id_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    map_coordinates = models.CharField(max_length=100, help_text="Координаты карты", default='0.0;0.0')

    def __str__(self):
        return f'{self.id}, {self.title}'

    def get_absolute_url(self):
        return reverse('remember_detail', args=[str(self.id)])
