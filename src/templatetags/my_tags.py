from django import template

register = template.Library()


@register.simple_tag()  # используется в index.html
def mediapath(value):
    if value:
        return f'{value}'
