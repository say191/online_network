from django.db import models
from django.utils import timezone
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author', **NULLABLE)
    title = models.CharField(max_length=50, verbose_name='title')
    model = models.CharField(max_length=50, verbose_name='model')
    release_date = models.DateTimeField(default=timezone.now, verbose_name='release_date')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
