from itertools import permutations
from cric.models import *

def match_schedule_generator():
    teams = CricketTeam.objects.all()
    matches_list = permutations(list(teams),2)
    for i in matches_list:
        MatchStats.objects.create(home_team=i[0],away_team=i[1],winner_team=None)
    return True