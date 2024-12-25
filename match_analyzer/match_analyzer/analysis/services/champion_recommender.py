from collections import Counter
from django.db.models import Q
from analysis.models import Champion

class ChampionRecommender:
    def __init__(self):
        self.similarity_weights = {
            'playstyle': 0.4,
            'role': 0.3,
            'difficulty': 0.3
        }
    
    def get_recommendations(self, match_history, num_recommendations=5):
        if not match_history:
            return []
            
        played_champions = [match['champion'] for match in match_history if match.get('champion')]
        if not played_champions:
            return []

        champion_objects = Champion.objects.filter(name__in=played_champions)
        if not champion_objects.exists():
            return []
            
        playstyles = Counter()
        roles = Counter()
        avg_difficulty = 0
        
        for champ in champion_objects:
            for tag in champ.playstyle_tags:
                playstyles[tag] += 1
            roles[champ.role] += 1
            avg_difficulty += champ.difficulty
        
        avg_difficulty /= len(champion_objects)
        
        all_champions = Champion.objects.exclude(name__in=played_champions)
        recommendations = []
        
        for champ in all_champions:
            score = self._calculate_similarity_score(
                champ,
                playstyles,
                roles,
                avg_difficulty
            )
            recommendations.append((champ, score))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return [rec[0] for rec in recommendations[:num_recommendations]]
    
    def _calculate_similarity_score(self, champion, playstyles, roles, avg_difficulty):
        playstyle_score = sum(playstyles[tag] for tag in champion.playstyle_tags)
        role_score = roles[champion.role]
        difficulty_score = 1 - abs(champion.difficulty - avg_difficulty) / 10
        
        return (
            playstyle_score * self.similarity_weights['playstyle'] +
            role_score * self.similarity_weights['role'] + 
            difficulty_score * self.similarity_weights['difficulty']
        )