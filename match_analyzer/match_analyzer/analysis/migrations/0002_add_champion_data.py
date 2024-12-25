from django.db import migrations

def add_champion_data(apps, schema_editor):
    Champion = apps.get_model('analysis', 'Champion')
    
    champions_data = [
        # A
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
            'name': 'Akali',
            'playstyle_tags': ['assassin', 'stealth', 'mobile'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Akshan',
            'playstyle_tags': ['marksman', 'assassin', 'mobile'],
            'role': 'mid',
            'difficulty': 6
        },
        {
            'name': 'Alistar',
            'playstyle_tags': ['tank', 'support', 'engage'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Amumu',
            'playstyle_tags': ['tank', 'engage', 'aoe'],
            'role': 'jungle',
            'difficulty': 3
        },
        {
            'name': 'Anivia',
            'playstyle_tags': ['mage', 'control', 'zone'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Annie',
            'playstyle_tags': ['mage', 'burst', 'stun'],
            'role': 'mid',
            'difficulty': 3
        },
        {
            'name': 'Aphelios',
            'playstyle_tags': ['marksman', 'hypercarry', 'versatile'],
            'role': 'bot',
            'difficulty': 9
        },
        {
            'name': 'Ashe',
            'playstyle_tags': ['marksman', 'utility', 'cc'],
            'role': 'bot',
            'difficulty': 4
        },
        {
            'name': 'Aurelion Sol',
            'playstyle_tags': ['mage', 'roaming', 'zone'],
            'role': 'mid',
            'difficulty': 8
        },
        {
            'name': 'Azir',
            'playstyle_tags': ['mage', 'zone', 'scaling'],
            'role': 'mid',
            'difficulty': 9
        },

        # B
        {
            'name': 'Bard',
            'playstyle_tags': ['support', 'roaming', 'utility'],
            'role': 'support',
            'difficulty': 8
        },
        {
            'name': 'Belveth',
            'playstyle_tags': ['fighter', 'mobile', 'scaling'],
            'role': 'jungle',
            'difficulty': 6
        },
        {
            'name': 'Blitzcrank',
            'playstyle_tags': ['tank', 'support', 'hook'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Brand',
            'playstyle_tags': ['mage', 'burst', 'aoe'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Braum',
            'playstyle_tags': ['tank', 'support', 'peel'],
            'role': 'support',
            'difficulty': 5
        },
        {
            'name': 'Briar',
            'playstyle_tags': ['fighter', 'assassin', 'lifesteal'],
            'role': 'jungle',
            'difficulty': 7
        },

        # C
        {
            'name': 'Caitlyn',
            'playstyle_tags': ['marksman', 'poke', 'zone'],
            'role': 'bot',
            'difficulty': 5
        },
        {
            'name': 'Camille',
            'playstyle_tags': ['fighter', 'mobile', 'single-target'],
            'role': 'top',
            'difficulty': 7
        },
        {
            'name': 'Cassiopeia',
            'playstyle_tags': ['mage', 'dps', 'zone'],
            'role': 'mid',
            'difficulty': 8
        },
        {
            'name': 'Chogath',
            'playstyle_tags': ['tank', 'scaling', 'sustain'],
            'role': 'top',
            'difficulty': 3
        },
        {
            'name': 'Corki',
            'playstyle_tags': ['marksman', 'poke', 'hybrid'],
            'role': 'mid',
            'difficulty': 6
        },

        # D
        {
            'name': 'Darius',
            'playstyle_tags': ['fighter', 'juggernaut', 'execute'],
            'role': 'top',
            'difficulty': 4
        },
        {
            'name': 'Diana',
            'playstyle_tags': ['assassin', 'fighter', 'engage'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Dr. Mundo',
            'playstyle_tags': ['tank', 'juggernaut', 'sustain'],
            'role': 'top',
            'difficulty': 3
        },
        {
            'name': 'Draven',
            'playstyle_tags': ['marksman', 'aggressive', 'snowball'],
            'role': 'bot',
            'difficulty': 8
        },

        # E
        {
            'name': 'Ekko',
            'playstyle_tags': ['assassin', 'mobile', 'burst'],
            'role': 'jungle',
            'difficulty': 7
        },
        {
            'name': 'Elise',
            'playstyle_tags': ['mage', 'jungle', 'early-game'],
            'role': 'jungle',
            'difficulty': 8
        },
        {
            'name': 'Evelynn',
            'playstyle_tags': ['assassin', 'stealth', 'burst'],
            'role': 'jungle',
            'difficulty': 6
        },
        {
            'name': 'Ezreal',
            'playstyle_tags': ['marksman', 'poke', 'mobile'],
            'role': 'bot',
            'difficulty': 6
        },

        # F
        {
            'name': 'Fiddlesticks',
            'playstyle_tags': ['mage', 'jungle', 'aoe'],
            'role': 'jungle',
            'difficulty': 7
        },
        {
            'name': 'Fiora',
            'playstyle_tags': ['fighter', 'duelist', 'mobile'],
            'role': 'top',
            'difficulty': 8
        },
        {
            'name': 'Fizz',
            'playstyle_tags': ['assassin', 'mobile', 'trickster'],
            'role': 'mid',
            'difficulty': 6
        },

        # G
        {
            'name': 'Galio',
            'playstyle_tags': ['tank', 'mage', 'anti-mage'],
            'role': 'mid',
            'difficulty': 5
        },
        {
            'name': 'Gangplank',
            'playstyle_tags': ['fighter', 'global', 'scaling'],
            'role': 'top',
            'difficulty': 9
        },
        {
            'name': 'Garen',
            'playstyle_tags': ['fighter', 'juggernaut', 'sustain'],
            'role': 'top',
            'difficulty': 2
        },
        {
            'name': 'Gnar',
            'playstyle_tags': ['fighter', 'tank', 'transform'],
            'role': 'top',
            'difficulty': 7
        },
        {
            'name': 'Gragas',
            'playstyle_tags': ['tank', 'engage', 'burst'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Graves',
            'playstyle_tags': ['marksman', 'jungle', 'burst'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Gwen',
            'playstyle_tags': ['fighter', 'ap', 'skirmisher'],
            'role': 'top',
            'difficulty': 6
        },

        # H
        {
            'name': 'Hecarim',
            'playstyle_tags': ['fighter', 'engage', 'mobile'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Heimerdinger',
            'playstyle_tags': ['mage', 'zone', 'turrets'],
            'role': 'mid',
            'difficulty': 6
        },

        # I
        {
            'name': 'Illaoi',
            'playstyle_tags': ['fighter', 'juggernaut', 'zone'],
            'role': 'top',
            'difficulty': 6
        },
        {
            'name': 'Irelia',
            'playstyle_tags': ['fighter', 'mobile', 'burst'],
            'role': 'top',
            'difficulty': 8
        },
        {
            'name': 'Ivern',
            'playstyle_tags': ['support', 'jungle', 'utility'],
            'role': 'jungle',
            'difficulty': 7
        },

        # J
        {
            'name': 'Janna',
            'playstyle_tags': ['support', 'disengage', 'enchanter'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Jarvan IV',
            'playstyle_tags': ['fighter', 'engage', 'gank'],
            'role': 'jungle',
            'difficulty': 4
        },
        {
            'name': 'Jax',
            'playstyle_tags': ['fighter', 'scaling', 'split-push'],
            'role': 'top',
            'difficulty': 5
        },
        {
            'name': 'Jayce',
            'playstyle_tags': ['fighter', 'poke', 'transform'],
            'role': 'top',
            'difficulty': 7
        },
        {
            'name': 'Jhin',
            'playstyle_tags': ['marksman', 'utility', 'execute'],
            'role': 'bot',
            'difficulty': 6
        },
        {
            'name': 'Jinx',
            'playstyle_tags': ['marksman', 'hypercarry', 'aoe'],
            'role': 'bot',
            'difficulty': 5
        },

        # K
        {
            'name': "K'Sante",
            'playstyle_tags': ['tank', 'fighter', 'transform'],
            'role': 'top',
            'difficulty': 7
        },
        {
            'name': "Kai'Sa",
            'playstyle_tags': ['marksman', 'assassin', 'hybrid'],
            'role': 'bot',
            'difficulty': 6
        },
        {
            'name': 'Kalista',
            'playstyle_tags': ['marksman', 'mobile', 'objective'],
            'role': 'bot',
            'difficulty': 8
        },
        {
            'name': 'Karma',
            'playstyle_tags': ['mage', 'support', 'poke'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Karthus',
            'playstyle_tags': ['mage', 'global', 'farm'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Kassadin',
            'playstyle_tags': ['assassin', 'scaling', 'mobile'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Katarina',
            'playstyle_tags': ['assassin', 'mobile', 'reset'],
            'role': 'mid',
            'difficulty': 8
        },
        {
            'name': 'Kayle',
            'playstyle_tags': ['fighter', 'scaling', 'hybrid'],
            'role': 'top',
            'difficulty': 6
        },
        {
            'name': 'Kayn',
            'playstyle_tags': ['fighter', 'assassin', 'transform'],
            'role': 'jungle',
            'difficulty': 7
        },
        {
            'name': 'Kennen',
            'playstyle_tags': ['mage', 'engage', 'aoe'],
            'role': 'top',
            'difficulty': 5
        },
        {
            'name': "Kha'Zix",
            'playstyle_tags': ['assassin', 'isolation', 'evolve'],
            'role': 'jungle',
            'difficulty': 6
        },
        {
            'name': 'Kindred',
            'playstyle_tags': ['marksman', 'jungle', 'scaling'],
            'role': 'jungle',
            'difficulty': 7
        },
        {
            'name': 'Kled',
            'playstyle_tags': ['fighter', 'engage', 'remount'],
            'role': 'top',
            'difficulty': 7
        },
        {
            'name': "Kog'Maw",
            'playstyle_tags': ['marksman', 'hypercarry', 'artillery'],
            'role': 'bot',
            'difficulty': 6
        },

        # L
        {
            'name': 'LeBlanc',
            'playstyle_tags': ['assassin', 'burst', 'mobility'],
            'role': 'mid',
            'difficulty': 8
        },
        {
            'name': 'Lee Sin',
            'playstyle_tags': ['fighter', 'mobility', 'playmaker'],
            'role': 'jungle',
            'difficulty': 9
        },
        {
            'name': 'Leona',
            'playstyle_tags': ['tank', 'engage', 'cc'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Lillia',
            'playstyle_tags': ['mage', 'speed', 'dot'],
            'role': 'jungle',
            'difficulty': 6
        },
        {
            'name': 'Lissandra',
            'playstyle_tags': ['mage', 'cc', 'engage'],
            'role': 'mid',
            'difficulty': 5
        },
        {
            'name': 'Lucian',
            'playstyle_tags': ['marksman', 'mobile', 'burst'],
            'role': 'bot',
            'difficulty': 6
        },
        {
            'name': 'Lulu',
            'playstyle_tags': ['support', 'enchanter', 'utility'],
            'role': 'support',
            'difficulty': 5
        },
        {
            'name': 'Lux',
            'playstyle_tags': ['mage', 'support', 'artillery'],
            'role': 'mid',
            'difficulty': 3
        },

        # M
        {
            'name': 'Malphite',
            'playstyle_tags': ['tank', 'engage', 'aoe'],
            'role': 'top',
            'difficulty': 2
        },
        {
            'name': 'Malzahar',
            'playstyle_tags': ['mage', 'push', 'suppress'],
            'role': 'mid',
            'difficulty': 3
        },
        {
            'name': 'Maokai',
            'playstyle_tags': ['tank', 'cc', 'sustain'],
            'role': 'support',
            'difficulty': 3
        },
        {
            'name': 'Master Yi',
            'playstyle_tags': ['assassin', 'melee-carry', 'reset'],
            'role': 'jungle',
            'difficulty': 4
        },
        {
            'name': 'Miss Fortune',
            'playstyle_tags': ['marksman', 'aoe', 'lane-bully'],
            'role': 'bot',
            'difficulty': 2
        },

        # N
        {
            'name': 'Nami',
            'playstyle_tags': ['support', 'enchanter', 'cc'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Nasus',
            'playstyle_tags': ['fighter', 'scaling', 'split-push'],
            'role': 'top',
            'difficulty': 3
        },
        {
            'name': 'Nautilus',
            'playstyle_tags': ['tank', 'engage', 'cc'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Neeko',
            'playstyle_tags': ['mage', 'cc', 'deception'],
            'role': 'mid',
            'difficulty': 5
        },
        {
            'name': 'Nidalee',
            'playstyle_tags': ['assassin', 'poke', 'transform'],
            'role': 'jungle',
            'difficulty': 8
        },
        {
            'name': 'Nilah',
            'playstyle_tags': ['fighter', 'marksman', 'scaling'],
            'role': 'bot',
            'difficulty': 6
        },
        {
            'name': 'Nocturne',
            'playstyle_tags': ['assassin', 'global', 'dive'],
            'role': 'jungle',
            'difficulty': 4
        },
        {
            'name': 'Nunu & Willump',
            'playstyle_tags': ['tank', 'objective', 'engage'],
            'role': 'jungle',
            'difficulty': 4
        },

        # O
        {
            'name': 'Olaf',
            'playstyle_tags': ['fighter', 'unstoppable', 'sustain'],
            'role': 'top',
            'difficulty': 3
        },
        {
            'name': 'Orianna',
            'playstyle_tags': ['mage', 'control', 'utility'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Ornn',
            'playstyle_tags': ['tank', 'forge', 'engage'],
            'role': 'top',
            'difficulty': 5
        },

        # P
        {
            'name': 'Pantheon',
            'playstyle_tags': ['fighter', 'roam', 'burst'],
            'role': 'top',
            'difficulty': 4
        },
        {
            'name': 'Poppy',
            'playstyle_tags': ['tank', 'peel', 'anti-mobility'],
            'role': 'top',
            'difficulty': 6
        },
        {
            'name': 'Pyke',
            'playstyle_tags': ['support', 'assassin', 'execute'],
            'role': 'support',
            'difficulty': 7
        },

        # Q
        {
            'name': 'Qiyana',
            'playstyle_tags': ['assassin', 'elements', 'combo'],
            'role': 'mid',
            'difficulty': 8
        },
        {
            'name': 'Quinn',
            'playstyle_tags': ['marksman', 'roam', 'duelist'],
            'role': 'top',
            'difficulty': 5
        },

        # R
        {
            'name': 'Rakan',
            'playstyle_tags': ['support', 'engage', 'mobility'],
            'role': 'support',
            'difficulty': 5
        },
        {
            'name': 'Rammus',
            'playstyle_tags': ['tank', 'taunt', 'armor'],
            'role': 'jungle',
            'difficulty': 3
        },
        {
            'name': 'RekSai',
            'playstyle_tags': ['fighter', 'tunneling', 'early-game'],
            'role': 'jungle',
            'difficulty': 6
        },
        {
            'name': 'Rell',
            'playstyle_tags': ['tank', 'engage', 'cc'],
            'role': 'support',
            'difficulty': 5
        },
        {
            'name': 'Renekton',
            'playstyle_tags': ['fighter', 'lane-bully', 'sustain'],
            'role': 'top',
            'difficulty': 3
        },
        {
            'name': 'Rengar',
            'playstyle_tags': ['assassin', 'stealth', 'burst'],
            'role': 'jungle',
            'difficulty': 7
        },
        {
            'name': 'Riven',
            'playstyle_tags': ['fighter', 'mobility', 'combo'],
            'role': 'top',
            'difficulty': 8
        },
        {
            'name': 'Rumble',
            'playstyle_tags': ['mage', 'fighter', 'zone-control'],
            'role': 'top',
            'difficulty': 6
        },
        {
            'name': 'Ryze',
            'playstyle_tags': ['mage', 'combo', 'realm-warp'],
            'role': 'mid',
            'difficulty': 7
        },

        # S
        {
            'name': 'Samira',
            'playstyle_tags': ['marksman', 'combo', 'style'],
            'role': 'bot',
            'difficulty': 6
        },
        {
            'name': 'Sejuani',
            'playstyle_tags': ['tank', 'engage', 'cc'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Senna',
            'playstyle_tags': ['support', 'marksman', 'scaling'],
            'role': 'support',
            'difficulty': 6
        },
        {
            'name': 'Seraphine',
            'playstyle_tags': ['mage', 'support', 'enchanter'],
            'role': 'support',
            'difficulty': 4
        },
        {
            'name': 'Sett',
            'playstyle_tags': ['fighter', 'juggernaut', 'suppression'],
            'role': 'top',
            'difficulty': 4
        },
        {
            'name': 'Shaco',
            'playstyle_tags': ['assassin', 'deceive', 'traps'],
            'role': 'jungle',
            'difficulty': 7
        },
        {
            'name': 'Shen',
            'playstyle_tags': ['tank', 'global', 'utility'],
            'role': 'top',
            'difficulty': 5
        },
        {
            'name': 'Shyvana',
            'playstyle_tags': ['fighter', 'dragon', 'hybrid'],
            'role': 'jungle',
            'difficulty': 4
        },
        {
            'name': 'Singed',
            'playstyle_tags': ['tank', 'poison', 'unique'],
            'role': 'top',
            'difficulty': 6
        },
        {
            'name': 'Sion',
            'playstyle_tags': ['tank', 'scaling', 'undead'],
            'role': 'top',
            'difficulty': 5
        },
        {
            'name': 'Sivir',
            'playstyle_tags': ['marksman', 'waveclear', 'utility'],
            'role': 'bot',
            'difficulty': 4
        },
        {
            'name': 'Skarner',
            'playstyle_tags': ['fighter', 'suppress', 'spires'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Sona',
            'playstyle_tags': ['support', 'enchanter', 'aura'],
            'role': 'support',
            'difficulty': 2
        },
        {
            'name': 'Soraka',
            'playstyle_tags': ['support', 'healer', 'global'],
            'role': 'support',
            'difficulty': 3
        },
        {
            'name': 'Swain',
            'playstyle_tags': ['mage', 'drain-tank', 'sustain'],
            'role': 'mid',
            'difficulty': 5
        },
        {
            'name': 'Sylas',
            'playstyle_tags': ['mage', 'fighter', 'ultimate-stealer'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Syndra', 
            'playstyle_tags': ['mage', 'burst', 'control'],
            'role': 'mid',
            'difficulty': 7
        },

        # T
        {
            'name': 'Tahm Kench',
            'playstyle_tags': ['tank', 'support', 'utility'],
            'role': 'top',
            'difficulty': 5
        },
        {
            'name': 'Taliyah',
            'playstyle_tags': ['mage', 'roamer', 'control'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Talon',
            'playstyle_tags': ['assassin', 'roamer', 'parkour'],
            'role': 'mid', 
            'difficulty': 6
        },
        {
            'name': 'Taric',
            'playstyle_tags': ['support', 'tank', 'enchanter'],
            'role': 'support',
            'difficulty': 5
        },
        {
            'name': 'Teemo',
            'playstyle_tags': ['marksman', 'ap', 'trapper'],
            'role': 'top',
            'difficulty': 3
        },
        {
            'name': 'Thresh',
            'playstyle_tags': ['support', 'tank', 'catcher'],
            'role': 'support', 
            'difficulty': 7
        },
        {
            'name': 'Tristana',
            'playstyle_tags': ['marksman', 'scaling', 'reset'],
            'role': 'bot',
            'difficulty': 4
        },
        {
            'name': 'Trundle',
            'playstyle_tags': ['fighter', 'duelist', 'anti-tank'],
            'role': 'jungle',
            'difficulty': 3
        },
        {
            'name': 'Tryndamere',
            'playstyle_tags': ['fighter', 'split-push', 'crit'],
            'role': 'top',
            'difficulty': 4
        },
        {
            'name': 'Twisted Fate',
            'playstyle_tags': ['mage', 'roamer', 'utility'],
            'role': 'mid',
            'difficulty': 6
        },
        {
            'name': 'Twitch',
            'playstyle_tags': ['marksman', 'stealth', 'aoe'],
            'role': 'bot',
            'difficulty': 6
        },

        # U
        {
            'name': 'Udyr',
            'playstyle_tags': ['fighter', 'stance', 'speed'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Urgot',
            'playstyle_tags': ['fighter', 'tank', 'execute'],
            'role': 'top',
            'difficulty': 6
        },

        # V
        {
            'name': 'Varus',
            'playstyle_tags': ['marksman', 'artillery', 'poke'],
            'role': 'bot',
            'difficulty': 6
        },
        {
            'name': 'Vayne',
            'playstyle_tags': ['marksman', 'duelist', 'true-damage'],
            'role': 'bot',
            'difficulty': 8
        },
        {
            'name': 'Veigar',
            'playstyle_tags': ['mage', 'scaling', 'burst'],
            'role': 'mid',
            'difficulty': 4
        },
        {
            'name': "Vel'Koz",
            'playstyle_tags': ['mage', 'artillery', 'true-damage'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Vex',
            'playstyle_tags': ['mage', 'anti-mobility', 'burst'],
            'role': 'mid',
            'difficulty': 5
        },
        {
            'name': 'Vi',
            'playstyle_tags': ['fighter', 'diver', 'engage'],
            'role': 'jungle',
            'difficulty': 4
        },
        {
            'name': 'Viego',
            'playstyle_tags': ['fighter', 'assassin', 'possession'],
            'role': 'jungle',
            'difficulty': 7
        },
        {
            'name': 'Viktor',
            'playstyle_tags': ['mage', 'control', 'scaling'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Vladimir',
            'playstyle_tags': ['mage', 'sustain', 'scaling'],
            'role': 'mid',
            'difficulty': 6
        },
        {
            'name': 'Volibear',
            'playstyle_tags': ['fighter', 'tank', 'diver'],
            'role': 'top',
            'difficulty': 4
        },

        # W
        {
            'name': 'Warwick',
            'playstyle_tags': ['fighter', 'sustain', 'pursue'],
            'role': 'jungle',
            'difficulty': 3
        },
        {
            'name': 'Wukong',
            'playstyle_tags': ['fighter', 'engage', 'trickster'],
            'role': 'top',
            'difficulty': 4
        },

        # X
        {
            'name': 'Xayah',
            'playstyle_tags': ['marksman', 'self-peel', 'aoe'],
            'role': 'bot',
            'difficulty': 6
        },
        {
            'name': 'Xerath',
            'playstyle_tags': ['mage', 'artillery', 'siege'],
            'role': 'mid',
            'difficulty': 7
        },
        {
            'name': 'Xin Zhao',
            'playstyle_tags': ['fighter', 'engage', 'early-game'],
            'role': 'jungle',
            'difficulty': 4
        },

        # Y
        {
            'name': 'Yasuo',
            'playstyle_tags': ['fighter', 'windwall', 'mobility'],
            'role': 'mid',
            'difficulty': 9
        },
        {
            'name': 'Yone',
            'playstyle_tags': ['fighter', 'assassin', 'mixed-damage'],
            'role': 'mid',
            'difficulty': 8
        },
        {
            'name': 'Yorick',
            'playstyle_tags': ['fighter', 'split-push', 'summon'],
            'role': 'top',
            'difficulty': 6
        },
        {
            'name': 'Yuumi',
            'playstyle_tags': ['support', 'enchanter', 'untargetable'],
            'role': 'support',
            'difficulty': 4
        },

        # Z
        {
            'name': 'Zac',
            'playstyle_tags': ['tank', 'engage', 'sustain'],
            'role': 'jungle',
            'difficulty': 5
        },
        {
            'name': 'Zed',
            'playstyle_tags': ['assassin', 'shadow', 'burst'],
            'role': 'mid',
            'difficulty': 8
        },
        {
            'name': 'Zeri',
            'playstyle_tags': ['marksman', 'mobility', 'kiting'],
            'role': 'bot',
            'difficulty': 7
        },
        {
            'name': 'Ziggs',
            'playstyle_tags': ['mage', 'artillery', 'siege'],
            'role': 'mid',
            'difficulty': 5
        },
        {
            'name': 'Zilean',
            'playstyle_tags': ['support', 'utility', 'revive'],
            'role': 'support',
            'difficulty': 6
        },
        {
            'name': 'Zoe',
            'playstyle_tags': ['mage', 'burst', 'pick'],
            'role': 'mid',
            'difficulty': 8
        },
        {
            'name': 'Zyra',
            'playstyle_tags': ['mage', 'support', 'zone-control'],
            'role': 'support',
            'difficulty': 6
        }
    ]  # Make sure this closing bracket is present

    # Remove duplicate entries and create champions
    unique_champions = {champ['name']: champ for champ in champions_data}.values()
    Champion.objects.bulk_create([
        Champion(**champion_data)
        for champion_data in unique_champions
    ])

def remove_champion_data(apps, schema_editor):
    Champion = apps.get_model('analysis', 'Champion')
    Champion.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_champion_data, remove_champion_data),
    ]