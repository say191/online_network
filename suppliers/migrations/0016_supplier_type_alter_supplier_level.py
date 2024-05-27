# Generated by Django 4.2.7 on 2024-05-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0015_alter_supplier_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='type',
            field=models.CharField(blank=True, choices=[('FA', 'factory'), ('RN', 'retail network'), ('IE', 'ip')], null=True, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='level',
            field=models.IntegerField(choices=[(0, 'zero level'), (1, 'first level'), (2, 'second level')], verbose_name='level'),
        ),
    ]
