import json
from django.shortcuts import render
from .forms import SummonerForm
import requests
from urllib.parse import quote
from time import sleep
from requests.exceptions import RequestException
from django.http import JsonResponse
from .services.champion_recommender import ChampionRecommender
from .recommendations import get_champion_recommendations


API_KEY = 'RGAPI-9dbf1bdd-c2c7-4efb-b3b4-d9b4f205e192'
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds
BATCH_SIZE = 5  # Number of matches to process at once
BATCH_DELAY = 1.2  # Delay between batches in seconds

def make_request(url, max_retries=MAX_RETRIES):
    """Make API request with retries"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 503:
                if attempt < max_retries - 1:
                    print(f"Service unavailable, retrying in {RETRY_DELAY} seconds...")
                    sleep(RETRY_DELAY)
                    continue
            print(f"Error: {response.status_code} - {response.text}")
            raise Exception(f"API request failed: {response.status_code} - {get_error_message(response)}")
        except RequestException as e:
            if attempt < max_retries - 1:
                print(f"Request failed, retrying in {RETRY_DELAY} seconds... Error: {str(e)}")
                sleep(RETRY_DELAY)
                continue
            raise Exception(f"Request failed after {max_retries} attempts: {str(e)}")
    raise Exception("Max retries exceeded")

def get_error_message(response):
    """Get friendly error message based on status code"""
    try:
        data = response.json()
        if 'status' in data:
            if response.status_code == 503:
                return "Riot API is temporarily unavailable. Please try again in a few minutes."
            return data['status'].get('message', 'Unknown error')
    except:
        pass
    return f"HTTP {response.status_code}"

def get_riot_id_data(summoner_name, tag_line, region):
    """Get account data using Riot ID"""
    regional_endpoint = get_regional_endpoint(region)
    encoded_name = quote(summoner_name)
    encoded_tag = quote(tag_line)
    url = f'https://{regional_endpoint}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{encoded_name}/{encoded_tag}?api_key={API_KEY}'
    return make_request(url)

def get_summoner_by_puuid(puuid, region):
    """Get summoner data using PUUID"""
    url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={API_KEY}'
    return make_request(url)

def get_regional_endpoint(region):
    """Map region codes to regional routing values"""
    routing = {
        'euw1': 'europe',
        'eun1': 'europe',
        'ru': 'europe',
        'tr1': 'europe',
        'na1': 'americas',
        'br1': 'americas',
        'la1': 'americas',
        'la2': 'americas',
        'kr': 'asia',
        'jp1': 'asia'
    }
    return routing.get(region.lower())

def get_match_history(puuid, region, start=0, count=20):
    """Get match history using v5 endpoint"""
    regional_endpoint = get_regional_endpoint(region)
    if not regional_endpoint:
        raise ValueError(f"Invalid region: {region}")
    
    url = f'https://{regional_endpoint}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={API_KEY}'
    return make_request(url)

def get_match_details(match_id, region):
    """Get match details using v5 endpoint"""
    regional_endpoint = get_regional_endpoint(region)
    if not regional_endpoint:
        raise ValueError(f"Invalid region: {region}")
    
    url = f'https://{regional_endpoint}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}'
    return make_request(url)

def process_match(match_id, puuid, region):
    """Process a single match and return formatted data"""
    match_detail = get_match_details(match_id, region)
    participant = next(
        p for p in match_detail['info']['participants'] 
        if p['puuid'] == puuid
    )
    
    return {
        'gameId': match_id,
        'champion': participant['championName'],
        'kills': participant['kills'],
        'deaths': participant['deaths'],
        'assists': participant['assists'],
        'cs': participant['totalMinionsKilled'] + participant['neutralMinionsKilled'],
        'damage': participant['totalDamageDealtToChampions'],
        'gold': participant['goldEarned'],
        'win': participant['win'],
        'gameDuration': match_detail['info']['gameDuration'] // 60,
        'gameMode': match_detail['info']['gameMode']
    }

def process_matches_in_batches(match_ids, puuid, region):
    """Process matches in batches to avoid rate limiting"""
    processed_matches = []
    
    for i in range(0, len(match_ids), BATCH_SIZE):
        batch = match_ids[i:i + BATCH_SIZE]
        for match_id in batch:
            try:
                match_data = process_match(match_id, puuid, region)
                processed_matches.append(match_data)
            except Exception as e:
                if "429" in str(e):  # Rate limit error
                    print(f"Rate limit hit, waiting longer...")
                    sleep(BATCH_DELAY * 2)  # Wait twice as long
                    try:
                        match_data = process_match(match_id, puuid, region)
                        processed_matches.append(match_data)
                    except:
                        continue  # Skip this match if it still fails
                else:
                    print(f"Error processing match {match_id}: {e}")
                    continue
        
        sleep(BATCH_DELAY)  # Wait between batches
    
    return processed_matches

def analyze_matches(request):
    """Main view function for analyzing matches"""
    if request.method == 'POST':
        form = SummonerForm(request.POST)
        if form.is_valid():
            try:
                # Handle initial form submission
                summoner_name, tag = form.cleaned_data['summoner_name'].split('#', 1)
                region = form.cleaned_data['region']
                
                # Get account and summoner data
                account_data = get_riot_id_data(summoner_name, tag, region)
                summoner_data = get_summoner_by_puuid(account_data['puuid'], region)
                
                # Handle AJAX requests for loading more matches
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    try:
                        data = json.loads(request.body)
                        puuid = data.get('puuid')
                        start = data.get('start', 0)
                        count = data.get('count', 5)  # Reduced from 20 to 5 to prevent rate limit issues

                        match_ids = get_match_history(puuid, region, start=start, count=count)
                        processed_matches = [
                            process_match(match_id, puuid, region)
                            for match_id in match_ids
                        ]

                        return JsonResponse({
                            'matches': processed_matches,
                            'has_more': len(match_ids) == count
                        })
                    except Exception as e:
                        return JsonResponse({'error': str(e)}, status=400)

                # Handle initial page load
                match_count = int(request.GET.get('count', 10))  # Reduced from 20 to 10
                match_ids = get_match_history(account_data['puuid'], region, count=match_count)
                processed_matches = [
                    process_match(match_id, account_data['puuid'], region)
                    for match_id in match_ids
                ]
                
                # Prepare context for template
                context = {
                    'summoner': {
                        'name': account_data['gameName'],
                        'level': summoner_data['summonerLevel'],
                        'profileIconId': summoner_data['profileIconId']
                    },
                    'account': {
                        'region': region,
                        'tagLine': account_data['tagLine'],
                        'puuid': account_data['puuid']
                    },
                    'matches': processed_matches,
                    'current_count': len(processed_matches),
                    'has_more': len(match_ids) == match_count
                }
                
                return render(request, 'analysis/results.html', context)
                
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                return render(request, 'analysis/analyze.html', {'form': form, 'error': error_msg})
    
    # GET request - show empty form
    form = SummonerForm()
    return render(request, 'analysis/analyze.html', {'form': form})


# Add this new view function
def get_champion_recommendations(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            puuid = data.get('puuid')
            region = data.get('region')
            
            # Get last 20 matches instead of 50 to reduce rate limiting
            match_ids = get_match_history(puuid, region, count=20)
            matches = process_matches_in_batches(match_ids, puuid, region)
            
            # Get recommendations
            recommender = ChampionRecommender()
            recommendations = recommender.get_recommendations(matches)
            
            return JsonResponse({
                'recommendations': [
                    {
                        'name': champ.name,
                        'role': champ.role,
                        'difficulty': champ.difficulty,
                        'playstyle': champ.playstyle_tags
                    }
                    for champ in recommendations
                ]
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

def get_recommendations(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        puuid = data.get('puuid')
        region = data.get('region')
        
        # Get recent matches
        matches = get_match_history(puuid, region)
        recommendations = get_champion_recommendations(matches)
        
        return JsonResponse({
            'recommendations': [
                {
                    'name': champ.name,
                    'role': champ.role,
                    'difficulty': champ.difficulty,
                    'playstyle': champ.playstyle_tags
                } for champ in recommendations
            ]
        })
    return JsonResponse({'error': 'Invalid request method'}, status=400)