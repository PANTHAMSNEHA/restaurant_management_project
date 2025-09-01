from django import template

register = template.Library()

@register.filter

def format_datetime(value):
    return value.strftime("%A, %d %B %Y- %I:%M %p")