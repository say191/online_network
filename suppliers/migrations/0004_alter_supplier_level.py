# Generated by Django 5.0.6 on 2024-05-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_alter_supplier_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='level',
            field=models.IntegerField(choices=[(0, 'Factory'), (1, 'Retail Network'), (2, 'Ip')], default=0, verbose_name='level'),
        ),
    ]
