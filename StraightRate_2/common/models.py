from django.contrib.auth import get_user_model
from django.db import models
from StraightRate_2.reviews.models import MovieReview, VideoGameReview

UserModel = get_user_model()


class MovieReviewLike(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'movie_review'],
                name='unique_movie_review_like'
            )
        ]

    movie_review = models.ForeignKey(
        to=MovieReview,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='liked_movie_reviews'
    )


class VideoGameReviewLike(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'game_review'],
                name='unique_game_review_like'
            )
        ]

    game_review = models.ForeignKey(
        to=VideoGameReview,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='liked_game_reviews'
    )

