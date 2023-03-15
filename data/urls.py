from django.urls import path

from .views import analyse, get_teams, get_players, get_player_state


urlpatterns = [
    path('analyse/', analyse, name='prediction'),
    path('getTeams/', get_teams, name='get teams'),
    path('getPlayers/', get_players, name='get teams'),
    path('getPlayerState/', get_player_state, name='get player states')
]

