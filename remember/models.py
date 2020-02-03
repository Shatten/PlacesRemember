import uuid
from django.db import models
from django.urls import reverse
# Create your models here.


class Remember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный номер воспоминания")

    title = models.CharField(max_length=200, help_text='Название воспоминания')
    description = models.TextField(max_length=2000, help_text='Описание воспоминания')

    def __str__(self):
        return f'{self.id}, {self.title}'

    def get_absolute_url(self):
        return reverse('remember-detail', args=[str(self.id)])