from rest_framework import serializers
from cric.models import CricketTeam,TeamPlayers,MatchStats,PointsTable

class CricketTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CricketTeam
        fields = ('id', 'title', 'team_logo')


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPlayers
        fields = ('id', 'first_name', 'last_name','player_image')



class MatchesListSerializer(serializers.ModelSerializer):
    home_team= serializers.SerializerMethodField()
    away_team= serializers.SerializerMethodField()
    winner_team= serializers.SerializerMethodField()

    def get_home_team(self,obj):
        return obj.home_team.title

    def get_away_team(self,obj):
        return obj.away_team.title

    def get_winner_team(self,obj):
        if obj.winner_team is not None:
            return obj.winner_team.title
        else:
            return 'Match Yet To be played'

    class Meta:
        model = MatchStats
        fields = ('home_team','away_team','winner_team')


class PointListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointsTable
        fields = '__all__'