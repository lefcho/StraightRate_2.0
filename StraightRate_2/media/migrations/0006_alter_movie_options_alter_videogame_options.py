# Generated by Django 5.1.3 on 2024-12-01 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_alter_movie_options_alter_videogame_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'permissions': [('can_approve_movies', 'Can approve movies')]},
        ),
        migrations.AlterModelOptions(
            name='videogame',
            options={'permissions': [('can_approve_games', 'Can approve video games')]},
        ),
    ]
