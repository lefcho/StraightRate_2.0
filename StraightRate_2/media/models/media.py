from django.db import models

from StraightRate_2.creators.models import Developer, Director
from StraightRate_2.media.models.genres import MovieGenre, VideoGameGenre


class AbstractMedia(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=150,
        verbose_name='Title',
    )

    description = models.TextField(
        verbose_name='Description',
    )

    release_date = models.DateField(
        verbose_name='Release Date',
    )


class Movie(AbstractMedia):
    genre = models.ManyToManyField(
        to=MovieGenre,
        related_name='movies',
    )

    director = models.ForeignKey(
        to=Director,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movies',
        verbose_name='Director',
    )

    poster = models.ImageField(
        upload_to='posters/movies/',
        null=True,
        blank=True,
        verbose_name='Poster',
    )

    def __str__(self):
        return self.title


class VideoGame(AbstractMedia):
    genre = models.ManyToManyField(
        to=VideoGameGenre,
        related_name='games',
    )

    developer = models.ForeignKey(
        to=Developer,
        null=True,
        on_delete=models.SET_NULL,
        related_name='games',
        verbose_name='Developer'
    )

    poster = models.ImageField(
        upload_to='posters/games/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
