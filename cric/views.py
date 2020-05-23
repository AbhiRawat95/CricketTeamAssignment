from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.views.generic import ListView
from cric.models import CricketTeam,TeamPlayers,MatchStats,PointsTable
from cric.serializers import CricketTeamSerializer,PlayerListSerializer,MatchesListSerializer,PointListSerializer


class CricketTeamList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CricketTeamSerializer

    def list(self, request, *args, **kwargs):
        queryset = CricketTeam.objects.all()
        twc = self.get_serializer(queryset, many=True)

        data = {"is_status": True, "message": "",
                                    "data": twc.data,
                     }
        return JsonResponse(data, status=status.HTTP_200_OK)

class TeamPlayerList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerListSerializer

    def get(self,request,team_id):
        players = TeamPlayers.objects.filter(team=team_id)
        serializer = PlayerListSerializer(players, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK,safe=False)


class MatchScheduleList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MatchesListSerializer

    def list(self, request, *args, **kwargs):
        queryset = MatchStats.objects.all()
        match_details = self.get_serializer(queryset, many=True)

        data = {"is_status": True, "message": "",
                                    "data": match_details.data,
                     }
        return JsonResponse(data, status=status.HTTP_200_OK)


class PointTableList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PointListSerializer

    def list(self, request, *args, **kwargs):
        queryset = PointsTable.objects.all()
        point_details = self.get_serializer(queryset, many=True)

        data = {"is_status": True, "message": "",
                                    "data": point_details.data,
                     }
        return JsonResponse(data, status=status.HTTP_200_OK)


#Template Section Views

class TeamListingView(ListView):
    model = CricketTeam
    context_object_name = 'teams'
    template_name = 'team_list.html'

    def get_queryset(self):
        return CricketTeam.objects.all()


class TeamDetailsView(ListView):
    model = TeamPlayers
    template_name = 'team_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TeamDetailsView, self).get_context_data(**kwargs)
        players_list = TeamPlayers.objects.filter(team=self.kwargs['team_id'])
        context['teamdetails'] = players_list
        context['team_title']=players_list[0].team
        return context

class PointsTableListingView(ListView):
    model = PointsTable
    context_object_name = 'points'
    template_name = 'points_table.html'

    def get_queryset(self):
        return PointsTable.objects.all()

class MatchScheduleListingView(ListView):
    model = MatchStats
    context_object_name = 'stats'
    template_name = 'match_stats.html'

    def get_queryset(self):
        return MatchStats.objects.all()