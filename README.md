Django Cricket Management App

This is a Django based app in which we have a Cricket Team, Players, Players Stats,Match Stats, and Points Table models in the cric app of the project.
Data Creation and updating can be done from the admin panel.

I have created both REST APIs and template-based to which can be used as per your case.
All the APIs can be accessed by only authenticated users( Please make sure you are logged in before accessing these APIs).

APIs Endpoints are as following : 
1. Cricket Team List - http://127.0.0.1:8000/cric/rest-api/team-list/
2. Points Table - http://127.0.0.1:8000/cric/rest-api/points-table/
3. Players Details List ( Based on Team includes the player stats) - http://127.0.0.1:8000/cric/rest-api/team-player-list/<team_id>
4. Match List - http://127.0.0.1:8000/cric/rest-api/match-list/
5. Match Schedule Generator - http://127.0.0.1:8000/cric/match-schedule-generator/

Template URLs : 
1. Cricket Team List - http://127.0.0.1:8000/cric/team-list/
2. Points Table - http://127.0.0.1:8000/cric/points-table/
3. Players Detail List - http://127.0.0.1:8000/cric/team-details/<team_id>

Signal assures that any change in the Match stat model updates the points table model and assign the points to the winning team.
Match Schedule APIs create home and away matches for all the teams in the CricketTeam model.