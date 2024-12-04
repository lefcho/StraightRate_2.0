# Generated by Django 5.1.3 on 2024-12-04 21:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0007_alter_movie_options_alter_videogame_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videogame',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
