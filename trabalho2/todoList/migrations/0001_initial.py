# Generated by Django 3.1 on 2020-12-01 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(help_text='digite a mensagem', max_length=200)),
                ('prazo', models.DateField(help_text='digite a data da entrega')),
            ],
        ),
    ]
