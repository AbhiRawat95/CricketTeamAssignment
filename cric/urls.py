from django.conf.urls import url
from cric.views import *

urlpatterns = [
    # ---- urls for cric app  ----#
    url(r'^rest-api/team-list/$', CricketTeamList.as_view(), name='rest-team-lists'),
    url(r'^rest-api/points-table/$', PointTableList.as_view(), name='rest-points-lists'),
    url(r'^rest-api/team-player-list/(?P<team_id>[0-9a-f-]+)/$', TeamPlayerList.as_view(), name='rest-team-player-list'),
    url(r'^rest-api/match-list/$', MatchScheduleList.as_view(), name='rest-match-list'),
    url(r'^team-list/$', TeamListingView.as_view(), name='team-list'),
    url(r'^team-details/(?P<team_id>[0-9a-f-]+)/$', TeamDetailsView.as_view(), name='team-details'),
    url(r'^points-table/$', PointsTableListingView.as_view(), name='points-table'),
]