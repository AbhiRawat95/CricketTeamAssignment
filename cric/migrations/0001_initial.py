# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CricketTeam',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('team_logo', models.URLField(max_length=4096, verbose_name='Team Logo')),
                ('club_state', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'CricketTeam',
            },
        ),
        migrations.CreateModel(
            name='MatchStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('away_team', models.ForeignKey(related_name='away_team', to='cric.CricketTeam')),
                ('home_team', models.ForeignKey(related_name='home_team', to='cric.CricketTeam')),
                ('winner_team', models.ForeignKey(related_name='winners', to='cric.CricketTeam')),
            ],
            options={
                'verbose_name': 'MatchStats',
            },
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_matches', models.PositiveIntegerField(null=True, blank=True)),
                ('total_runs', models.PositiveIntegerField(null=True, verbose_name='Total Runs', blank=True)),
                ('total_wickets', models.PositiveIntegerField(null=True, verbose_name='Total Wickets', blank=True)),
                ('total_centuries', models.PositiveIntegerField(null=True, verbose_name='Total Centuries', blank=True)),
                ('total_fifties', models.PositiveIntegerField(null=True, verbose_name='Total Fifties', blank=True)),
                ('highest_score', models.PositiveIntegerField(null=True, verbose_name='Highest Score', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'ordering': ['number_matches'],
                'verbose_name': 'PlayerStats',
            },
        ),
        migrations.CreateModel(
            name='PointsTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.PositiveIntegerField(default=0)),
                ('team', models.OneToOneField(related_name='point_team', on_delete=django.db.models.deletion.PROTECT, to='cric.CricketTeam', max_length=50)),
            ],
            options={
                'ordering': ['points'],
                'verbose_name': 'PointsTable',
            },
        ),
        migrations.CreateModel(
            name='TeamPlayers',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('player_image', models.URLField(max_length=4096, null=True, verbose_name='Player Image', blank=True)),
                ('jersey_number', models.PositiveIntegerField(unique=True)),
                ('origin_country', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'ordering': ['first_name'],
                'verbose_name': 'TeamPlayers',
            },
        ),
        migrations.AddField(
            model_name='playerstats',
            name='player',
            field=models.ForeignKey(related_name='player', on_delete=django.db.models.deletion.PROTECT, verbose_name='TeamPlayers', to='cric.TeamPlayers'),
        ),
    ]
