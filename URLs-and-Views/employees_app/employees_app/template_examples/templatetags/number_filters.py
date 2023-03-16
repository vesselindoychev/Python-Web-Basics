from django import template

register = template.Library()


@register.filter
def increase_by(value, number):
    return value + number