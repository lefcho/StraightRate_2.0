from django import template

register = template.Library()


@register.simple_tag(name='has_permission_to_suggest')
def has_permission_to_suggest(user):
    if user.is_authenticated:
        return (user.has_perm('media.can_suggest_movies')
                and user.has_perm('media.can_suggest_games'))
    return False
