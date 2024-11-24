from django import template

from StraightRate_2.media.models import VideoGameGenre

register = template.Library()


@register.simple_tag(name='game_genres')
def game_genres():
    return VideoGameGenre.objects.all()
