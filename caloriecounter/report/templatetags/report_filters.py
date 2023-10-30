from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def multiply(value, arg):
    """Multiply the value by the arg."""
    return float(value) * float(arg)

@register.filter
def dividedby(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0