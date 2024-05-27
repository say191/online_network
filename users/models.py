from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.CharField(max_length=40, verbose_name='email', unique=True)
    fio = models.CharField(max_length=40, verbose_name='fio')
    phone = models.CharField(max_length=20, verbose_name='phone', unique=True, **NULLABLE)
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.fio}"

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
