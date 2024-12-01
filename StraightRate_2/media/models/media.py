from django.db import models
from django.db.models import Avg

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

    approved = models.BooleanField(
        default=False,
    )

    def get_average_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 1) if avg_rating is not None else None


class Movie(AbstractMedia):
    class Meta:
        permissions = [
            ('can_approve_movies', 'Can approve movies'),
        ]

    genres = models.ManyToManyField(
        to=MovieGenre,
        related_name='movies',
    )

    directors = models.ManyToManyField(
        to=Director,
        related_name='movies',
        verbose_name='Directors',
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
    class Meta:
        permissions = [
            ('can_approve_games', 'Can approve video games'),
        ]

    genres = models.ManyToManyField(
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
