from django import template
from .. import models

register=template.Library()


@register.simple_tag(name='get_the_username')
def get_the_username(user):
    profile_qs = models.Player.objects.filter(user=user)
    if profile_qs:
        try:
            username=profile_qs.first().name
            response=username.strip().split()[0]
            return 'Hi, {}'.format(response)
        except :
            pass
    return ''
