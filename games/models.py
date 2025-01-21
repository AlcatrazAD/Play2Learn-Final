from django.db import models
from django.conf import settings

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=15)
    
    def _str_(self):
        return self.name


class Gamed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="scores")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="scores")
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.name} - {self.score}"


         

class GameScore(models.Model):

    MATH = "MATH"
    ANAGRAM = "ANAGRAM" 

    GAME_CHOICES = [
        (MATH, "Math Facts"),
        (ANAGRAM, "Anagram Hunt")
    ]

    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    operation = models.CharField(max_length=10, default='+' )
    max_number = models.IntegerField(default=0)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
