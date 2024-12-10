from django.contrib import admin

from StraightRate_2.reviews.models import VideoGameReview, MovieReview


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'rating', 'like_count', 'last_edited')
    list_filter = ('rating', 'movie', 'user')
    list_display_links = ('movie', 'user',)
    search_fields = ('movie__title', 'user__username', 'comment')
    readonly_fields = ('last_edited', 'like_count')

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes'


@admin.register(VideoGameReview)
class VideoGameReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'user', 'rating', 'like_count', 'last_edited')
    list_display_links = ('game', 'user',)
    list_filter = ('rating', 'game', 'user')
    search_fields = ('game__title', 'user__username', 'comment')
    readonly_fields = ('last_edited', 'like_count')

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes'
