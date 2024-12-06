# forms.py
from django import forms

REGION_CHOICES = [
    ('euw1', 'Europe West'),
    ('eun1', 'Europe Nordic & East'),
    ('na1', 'North America'),
    ('kr', 'Korea'),
    ('br1', 'Brazil'),
]

class SummonerForm(forms.Form):
    summoner_name = forms.CharField(
        label='Riot ID', 
        max_length=100,
        help_text='Enter your full Riot ID (e.g., OLVX#999)'
    )
    region = forms.ChoiceField(choices=REGION_CHOICES, label='Region')

    def clean_summoner_name(self):
        summoner_name = self.cleaned_data['summoner_name']
        if '#' not in summoner_name:
            raise forms.ValidationError('Please enter your full Riot ID including the hashtag and number (e.g., OLVX#999)')
        
        # Split on first '#' only
        parts = summoner_name.split('#', 1)
        if len(parts) != 2:
            raise forms.ValidationError('Invalid Riot ID format')
            
        name, tag = parts
        if not name or not tag:
            raise forms.ValidationError('Both name and tag are required')
            
        if not tag.isalnum():
            raise forms.ValidationError('Tag should only contain letters and numbers')
            
        return summoner_name