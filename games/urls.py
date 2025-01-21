from django.urls import path
from .views import user_scores
from games.views import HomeView, MathFactsView, AnagramHuntView, GameScoreView, record_score, AboutView

app_name = 'games'
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('record-score/', record_score, name="record-score"),
    path('games-scores/', GameScoreView.as_view(), name='games-scores'),
    path('about/', AboutView.as_view(), name='about'),
     path('scores/', user_scores, name='user_scores'),
]