from django.contrib import admin
from StraightRate_2.media.models import Movie, VideoGame


@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
