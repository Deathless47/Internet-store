from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def sample_text(string):
    return f'My shop {string}'


# времени написать интересный тег нету!

