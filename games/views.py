from django.shortcuts import render

import json

from django.http import JsonResponse

from games.models import GameScore

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class GameScoreView(TemplateView):
    template_name = "games-scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoreView, self).get_context_data(**kwargs)
        context['anagram_score'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_score'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context


def record_score(request):
    data = json.loads(request.body)

    user_name = data["user-name"]
    game = data["game"]
    score = data["score"]
    operation = data["operation"]
    max_number = data["max-number"]
    

    new_score = GameScore(user_name=user_name, game=game, score=score, operation=operation, max_number=max_number)
    new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)