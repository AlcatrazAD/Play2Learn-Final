from django.shortcuts import render

import json

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from games.models import GameScore, Game, Gamed

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



def user_scores(request):
    game_id = request.GET.get('game_id')  # Get the game ID from the query string
    if not game_id:
        return JsonResponse({"error": "game_id is required"}, status=400)

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return JsonResponse({"error": "Game not found"}, status=404)

    scores = Gamed.objects.filter(user=request.user, game=game).order_by('-created_at')
    scores_data = [{"score": score.score, "created_at": score.created_at} for score in scores]

    return JsonResponse({"game": game.name, "scores": scores_data})


def game_list(request):
    games = Game.objects.all()
    games_data = [{"id": game.id, "name": game.name} for game in games]
    return JsonResponse({"games": games_data})