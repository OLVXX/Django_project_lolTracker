from django.db import migrations

def add_champion_data(apps, schema_editor):
    Champion = apps.get_model('analysis', 'Champion')
    
    champions_data = [
        {
            'name': 'Aatrox',
            'playstyle_tags': ['fighter', 'drain tank', 'aoe'],
            'role': 'top',
            'difficulty': 6
        },
        {
            'name': 'Ahri', 
            'playstyle_tags': ['mage', 'assassin', 'mobile'],
            'role': 'mid',
            'difficulty': 5
        },
        {
            'name': 'Miss Fortune',
            'playstyle_tags': ['marksman', 'burst', 'aoe'],
            'role': 'bot',
            'difficulty': 3
        }
    ]

    for champ_data in champions_data:
        Champion.objects.create(**champ_data)

class Migration(migrations.Migration):
    dependencies = [
        ('analysis', '0002_champion'),
    ]

    operations = [
        migrations.RunPython(add_champion_data)
    ]