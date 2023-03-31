from django import template

from my_plant_app.main.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return len(Profile.objects.all()) > 0
