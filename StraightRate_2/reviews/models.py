from django.contrib.auth import get_user_model
from django.db import models

from StraightRate_2.media.models import Movie, VideoGame

UserModel = get_user_model()


class Review(models.Model):
    class Meta:
        abstract = True

    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        verbose_name='Rating',
    )

    comment = models.TextField(
        verbose_name='Comment',
    )

    last_edited = models.DateTimeField(
        auto_now=True,
    )


class MovieReview(Review):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'movie'],
                name='unique_movie_review'
            ),
        ]

    movie = models.ForeignKey(
        to=Movie,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Movie',
    )

    def __str__(self):
        return f'{self.user.username} gave {self.movie.title} a {self.rating}'


class VideoGameReview(Review):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'game'],
                name='unique_game_review'
            ),
        ]

    game = models.ForeignKey(
        to=VideoGame,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Video Game'
    )

    def __str__(self):
        return f'{self.user.username} gave {self.video_game.title} a {self.rating}'
