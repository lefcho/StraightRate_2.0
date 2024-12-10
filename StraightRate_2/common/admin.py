from django.contrib import admin

from StraightRate_2.common.models import MovieReviewLike, VideoGameReviewLike


@admin.register(MovieReviewLike)
class MovieReviewLikeAdmin(admin.ModelAdmin):
    list_display_links = ('movie_review',)
    list_display = ('id', 'movie_review', 'user',)
    list_filter = ('movie_review__movie', 'user',)
    search_fields = ('movie_review__movie__title', 'user__username',)


@admin.register(VideoGameReviewLike)
class VideoGameReviewLikeAdmin(admin.ModelAdmin):
    list_display_links = ('game_review',)
    list_display = ('id', 'game_review', 'user',)
    list_filter = ('game_review__game', 'user',)
    search_fields = ('game_review__game__title', 'user__username',)
