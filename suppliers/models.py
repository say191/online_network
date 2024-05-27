from django.db import models
from users.models import User
from products.models import Product
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Supplier(models.Model):
    TYPE = (
        ('FA', 'factory'),
        ('RN', 'retail network'),
        ('IE', 'ip'),
    )
    LEVEL = (
        (0, 'zero level'),
        (1, 'first level'),
        (2, 'second level'),
    )
    product = models.ManyToManyField(Product, verbose_name='product')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author', **NULLABLE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, verbose_name='supplier', related_name='related_suppliers', **NULLABLE)
    title = models.CharField(max_length=70, verbose_name='title')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='country')
    city = models.CharField(max_length=50, verbose_name='city')
    street = models.CharField(max_length=50, verbose_name='street')
    house = models.CharField(max_length=15, verbose_name='house')
    type = models.CharField(choices=TYPE, verbose_name='type')
    level = models.IntegerField(choices=LEVEL, verbose_name='level', **NULLABLE)
    debt = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='debt', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='created_at')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'
