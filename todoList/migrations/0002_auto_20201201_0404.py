# Generated by Django 3.1 on 2020-12-01 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='texto',
            field=models.CharField(max_length=200),
        ),
    ]