# analysis/templatetags/match_filters.py
from django import template

register = template.Library()

@register.filter
def calculate_kda(kills_and_assists, deaths):
    try:
        if deaths == 0:
            return "Perfect"
        return "{:.2f}".format(float(kills_and_assists) / float(deaths))
    except (ValueError, ZeroDivisionError, TypeError):
        return "0.00"

@register.simple_tag
def kda_ratio(kills, assists, deaths):
    try:
        if deaths == 0:
            return "Perfect"
        return "{:.2f}".format((float(kills) + float(assists)) / float(deaths))
    except (ValueError, ZeroDivisionError, TypeError):
        return "0.00"

@register.filter
def divideby(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def intcomma(value):
    try:
        return "{:,}".format(int(value))
    except (ValueError, TypeError):
        return value