from django.contrib import admin

from StraightRate_2.common.models import MovieReviewLike, VideoGameReviewLike


@admin.register(MovieReviewLike)
class MovieReviewLikeAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoGameReviewLike)
class VideoGameReviewLikeAdmin(admin.ModelAdmin):
    pass
