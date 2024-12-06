from django.shortcuts import render
from .forms import SummonerForm
import requests
from urllib.parse import quote
from time import sleep
from requests.exceptions import RequestException

API_KEY = 'RGAPI-ea6d33a4-9e14-4c5c-bb5c-839e32b0c86d'
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds

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
    """Get account data using Riot ID (username#tagline)"""
    regional_endpoint = get_regional_endpoint(region)
    encoded_name = quote(summoner_name)
    encoded_tag = quote(tag_line)
    url = f'https://{regional_endpoint}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{encoded_name}/{encoded_tag}?api_key={API_KEY}'
    print(f"Calling Account API: {url}")
    return make_request(url)

def get_summoner_by_puuid(puuid, region):
    """Get summoner data using PUUID"""
    url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={API_KEY}'
    print(f"Calling Summoner API: {url}")
    return make_request(url)

def get_regional_endpoint(region):
    """Map region codes to regional routing values for Riot API v5"""
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

def get_match_history(puuid, region):
    """Get match history using v5 endpoint"""
    regional_endpoint = get_regional_endpoint(region)
    if not regional_endpoint:
        raise ValueError(f"Invalid region: {region}")
    
    url = f'https://{regional_endpoint}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=5&api_key={API_KEY}'
    print(f"Calling Match History API: {url}")
    return make_request(url)

def get_match_details(match_id, region):
    """Get match details using v5 endpoint"""
    regional_endpoint = get_regional_endpoint(region)
    if not regional_endpoint:
        raise ValueError(f"Invalid region: {region}")
    
    url = f'https://{regional_endpoint}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}'
    print(f"Calling Match Details API: {url}")
    return make_request(url)

def analyze_matches(request):
    """Main view function for analyzing matches"""
    if request.method == 'POST':
        form = SummonerForm(request.POST)
        if form.is_valid():
            summoner_name = form.cleaned_data['summoner_name']
            region = form.cleaned_data['region']
            
            try:
                # Split Riot ID properly
                name, tag = summoner_name.split('#', 1)
                
                # Get Riot ID data first
                account_data = get_riot_id_data(name, tag, region)
                print("Account Data:", account_data)
                
                if 'puuid' not in account_data:
                    raise Exception("Player not found")
                
                # Get summoner data using PUUID
                summoner_data = get_summoner_by_puuid(account_data['puuid'], region)
                print("Summoner Data:", summoner_data)
                
                # Get match history
                match_ids = get_match_history(account_data['puuid'], region)
                print("Match IDs:", match_ids)
                
                matches = []
                for match_id in match_ids[:5]:
                    try:
                        match_detail = get_match_details(match_id, region)
                        matches.append(match_detail)
                    except Exception as e:
                        print(f"Error fetching match {match_id}: {str(e)}")
                        continue
                
                return render(request, 'analysis/results.html', {
                    'summoner': summoner_data,
                    'matches': matches,
                    'account': account_data
                })
                
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                print(error_msg)
                return render(request, 'analysis/analyze.html', {'form': form, 'error': error_msg})
    else:
        form = SummonerForm()
    return render(request, 'analysis/analyze.html', {'form': form})