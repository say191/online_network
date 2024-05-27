# Generated by Django 5.0.6 on 2024-05-26 11:57

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='title')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('street', models.CharField(max_length=50, verbose_name='street')),
                ('house', models.CharField(max_length=15, verbose_name='house')),
                ('level', models.IntegerField(choices=[('factory', '0'), ('retail_network', '1'), ('IP', '2')], default=0, verbose_name='level')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='debt')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='created_by')),
                ('product', models.ManyToManyField(to='products.product', verbose_name='product')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_suppliers', to='suppliers.supplier', verbose_name='supplier')),
            ],
            options={
                'verbose_name': 'supplier',
                'verbose_name_plural': 'suppliers',
            },
        ),
    ]
