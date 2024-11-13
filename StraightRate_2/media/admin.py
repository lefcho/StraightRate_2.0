from django.contrib import admin
from StraightRate_2.media.models import Movie, VideoGame, MovieGenre, VideoGameGenre


@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoGameGenre)
class VideoGameGenreAdmin(admin.ModelAdmin):
    pass
