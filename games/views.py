from django.shortcuts import render
import json
from django.http import JsonResponse
from games.models import GameScore

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"


def record_score(request):
    data = json.loads(request.body)

    user_name = data["user-name"]
    game = data["games"]
    score = data["score"]
    operations = data["operations"]
    max_number = data["max-number"]

    new_score = GameScore(user_name=user_name, game=game, score=score, operations=operations, max_number=max_number)
    new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)