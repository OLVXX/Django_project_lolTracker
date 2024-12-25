from django.db import models

class Player(models.Model):
    summoner_name = models.CharField(max_length=100)
    summoner_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.summoner_name

class Match(models.Model):
    match_id = models.CharField(max_length=100, unique=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    kda = models.CharField(max_length=10)
    farm = models.IntegerField()
    damage = models.IntegerField()

    def __str__(self):
        return self.match_id

class Champion(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    playstyle_tags = models.JSONField()
    role = models.CharField(max_length=20, db_index=True)
    difficulty = models.IntegerField()
    similar_champions = models.ManyToManyField('self', blank=True, symmetrical=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'role']),
        ]

    def __str__(self):
        return self.name