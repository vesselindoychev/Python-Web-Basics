from django import template

from car_collection_app.main.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return len(Profile.objects.all()) > 0
