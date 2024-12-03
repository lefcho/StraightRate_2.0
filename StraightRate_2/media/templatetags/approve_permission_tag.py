from django import template

register = template.Library()


@register.simple_tag(name='has_permission_to_approve')
def has_permission_to_approve(user):
    if user.is_authenticated:
        return (user.has_perm('media.can_approve_movies')
                and user.has_perm('media.can_approve_games'))
    return False
