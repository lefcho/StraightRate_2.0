# Generated by Django 5.1.3 on 2024-12-01 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_rename_genre_movie_genres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videogame',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
