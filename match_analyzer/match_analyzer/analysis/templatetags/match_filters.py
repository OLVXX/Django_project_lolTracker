# analysis/templatetags/match_filters.py
from django import template

register = template.Library()

@register.filter
def divisibleby(value, arg):
    """Returns integer division result"""
    return int(value) // int(arg)

@register.filter
def modulo(value, arg):
    """Returns modulo result"""
    return int(value) % int(arg)