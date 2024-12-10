from django.contrib import admin
from django.utils.html import format_html
from StraightRate_2.media.models import Movie, VideoGame, MovieGenre, VideoGameGenre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'approved', 'average_rating', 'date_added', 'view_poster')
    list_display_links = ('title',)
    list_filter = ('approved', 'release_date', 'genres', 'directors')
    search_fields = ('title', 'description', 'directors__first_name', 'directors__last_name')
    filter_horizontal = ('genres', 'directors')
    readonly_fields = ('date_added', 'average_rating')

    def average_rating(self, obj):
        return obj.get_average_rating()
    average_rating.short_description = 'Average Rating'

    def view_poster(self, obj):
        if obj.poster:
            return format_html('<img src="{}" style="height: 100px;" />', obj.poster.url)
        return "No Poster"
    view_poster.short_description = 'Poster Preview'


@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'approved', 'average_rating', 'developer', 'date_added', 'view_poster')
    list_display_links = ('title',)
    list_filter = ('approved', 'release_date', 'genres', 'developer')
    search_fields = ('title', 'description', 'developer__name')
    filter_horizontal = ('genres',)
    readonly_fields = ('date_added', 'average_rating')

    def average_rating(self, obj):
        return obj.get_average_rating()
    average_rating.short_description = 'Average Rating'

    def view_poster(self, obj):
        if obj.poster:
            return format_html('<img src="{}" style="height: 100px;" />', obj.poster.url)
        return "No Poster"
    view_poster.short_description = 'Poster Preview'


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    list_display_links = ('genre_name',)
    list_display = ('id', 'genre_name')
    search_fields = ('genre_name',)
    ordering = ('genre_name',)


@admin.register(VideoGameGenre)
class VideoGameGenreAdmin(admin.ModelAdmin):
    list_display_links = ('genre_name',)
    list_display = ('id', 'genre_name')
    search_fields = ('genre_name',)
    ordering = ('genre_name',)