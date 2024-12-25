from django import template

register = template.Library()

@register.simple_tag
def calculate_kda(kills, assists, deaths):
    try:
        kills = int(kills)
        assists = int(assists)
        deaths = int(deaths)
        
        if deaths == 0:
            return "Perfect"
        return f"{((kills + assists) / deaths):.1f}"
    except (ValueError, TypeError):
        return "0.0"
