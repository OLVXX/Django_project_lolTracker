from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze_matches, name='analyze_matches'),
    path('recommendations/', views.get_champion_recommendations, name='get_recommendations'),
]
