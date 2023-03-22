from django import template

from petstagram.main.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return len(Profile.objects.all()) > 0