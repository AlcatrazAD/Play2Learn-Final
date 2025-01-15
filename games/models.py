from django.db import models

# Create your models here.
class GameScore(models.Model):

    MATH = "MATH"
    ANAGRAM = "ANAGRAM" 

    GAME_CHOICES = [
        (MATH, "Math Facts"),
        (ANAGRAM, "Anagram Hunt")
    ]

    MULTIPLICATION = 'x'
    DIVISION = '/'
    SUBTRACTION = '-'
    ADDITION = '+'
    NONAPPLICABLE = 'n/a'

    OPERATIONS = [
     (MULTIPLICATION, 'x'),
     (DIVISION, '/'),
     (SUBTRACTION,'-'),
     (ADDITION,'+'),
     (NONAPPLICABLE,'N/A'),
    
    ]

    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    operation = models.TextField(choices=OPERATIONS, default=ADDITION)
    max_number = models.IntegerField()
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
