from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    """Home page view"""
    return render(request, 'analysis/home.html')

def analyze_matches(request):
    """Match analysis view"""
    return render(request, 'analysis/analyze.html', {'form': None})

def get_champion_recommendations(request):
    """Recommendations API endpoint"""
    return JsonResponse({'status': 'Coming soon'})
