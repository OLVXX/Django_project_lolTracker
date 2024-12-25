from .models import Champion

def get_champion_recommendations(match_history):
    """Generate champion recommendations based on player's match history"""
    
    # Analyze player performance patterns
    playstyles = set()
    preferred_roles = {}
    
    for match in match_history:
        # Count role frequencies
        if match.role in preferred_roles:
            preferred_roles[match.role] += 1
        else:
            preferred_roles[match.role] = 1
            
        # Get champion playstyle tags
        champion = Champion.objects.filter(name=match.champion).first()
        if champion:
            playstyles.update(champion.playstyle_tags)
    
    # Get most played role
    preferred_role = max(preferred_roles.items(), key=lambda x: x[1])[0] if preferred_roles else None
    
    # Find champions that match player's playstyle
    recommended_champions = Champion.objects.filter(
        role=preferred_role,
        playstyle_tags__contains=list(playstyles)
    ).exclude(
        name__in=[match.champion for match in match_history]
    )[:5]
    
    return list(recommended_champions)
