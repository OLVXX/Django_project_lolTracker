from django import template

register = template.Library()

@register.filter
def kda_ratio(value, deaths):
    try:
        deaths = int(deaths)
        if deaths == 0:
            return "Perfect"
        return f"{float(value)/deaths:.1f}"
    except (ValueError, TypeError):
        return "0.0"

@register.filter
def divideby(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def format_kda(value, deaths):
    try:
        deaths = int(deaths)
        if deaths == 0:
            return "Perfect"
        return f"{float(value):.1f}"
    except (ValueError, TypeError):
        return "0.0"

@register.simple_tag
def calculate_kda(kills, assists, deaths):
    try:
        kills = int(kills)
        assists = int(assists)
        deaths = int(deaths)
        
        if deaths == 0:
            return "Perfect"
        return f"{(kills + assists) / deaths:.1f}"
    except (ValueError, TypeError):
        return "0.0"

@register.filter
def intcomma(value):
    try:
        return "{:,}".format(int(value))
    except (ValueError, TypeError):
        return value