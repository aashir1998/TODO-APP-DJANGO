# Generated by Django 4.2.1 on 2023-05-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(help_text='Add new task', max_length=200),
        ),
    ]
