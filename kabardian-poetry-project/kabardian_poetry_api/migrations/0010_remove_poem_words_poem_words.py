# Generated by Django 5.0.6 on 2024-05-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kabardian_poetry_api', '0009_rename_vocabulary_poem_words'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poem',
            name='words',
        ),
        migrations.AddField(
            model_name='poem',
            name='words',
            field=models.ManyToManyField(related_name='vocabulary_words', to='kabardian_poetry_api.word'),
        ),
    ]