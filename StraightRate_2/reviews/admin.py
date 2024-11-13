from django.contrib import admin

from StraightRate_2.reviews.models import VideoGameReview, MovieReview


@admin.register(VideoGameReview)
class VideoGameReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    pass
