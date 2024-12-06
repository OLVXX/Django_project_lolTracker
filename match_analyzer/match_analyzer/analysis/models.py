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