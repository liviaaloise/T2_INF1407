# Generated by Django 3.1 on 2020-12-01 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0002_auto_20201201_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='privada',
            field=models.BooleanField(default=False),
        ),
    ]
