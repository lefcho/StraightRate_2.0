from django import template

from StraightRate_2.media.models import MovieGenre

register = template.Library()


@register.simple_tag(name='movie_genres')
def movie_genres():
    return MovieGenre.objects.all()
