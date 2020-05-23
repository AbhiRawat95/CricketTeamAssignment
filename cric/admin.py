from django.contrib import admin

# Register your models here.

from django.contrib import admin

from cric.models import CricketTeam,TeamPlayers,PointsTable,MatchStats,PlayerStats
from django.core.exceptions import ValidationError



class CricketTeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'team_logo', 'club_state', 'date_created', 'date_updated')

class TeamPlayersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team','player_image', 'jersey_number', 'origin_country', 'date_created',
                    'date_updated')

class MatchStatsAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'winner_team', 'date_created', 'date_created')

class PointsTableAdmin(admin.ModelAdmin):
    list_display = ('team', 'points')

class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'number_matches', 'total_runs', 'total_wickets', 'total_centuries', 'total_fifties',
                    'highest_score', 'date_created','date_updated')


admin.site.register(CricketTeam,CricketTeamAdmin)
admin.site.register(TeamPlayers, TeamPlayersAdmin)
admin.site.register(MatchStats, MatchStatsAdmin)
admin.site.register(PointsTable, PointsTableAdmin)
admin.site.register(PlayerStats, PlayerStatsAdmin)