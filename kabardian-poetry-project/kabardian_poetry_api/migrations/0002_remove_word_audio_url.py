# Generated by Django 5.0.6 on 2024-05-13 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kabardian_poetry_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='audio_url',
        ),
    ]