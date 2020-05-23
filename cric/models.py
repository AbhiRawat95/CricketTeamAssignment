# Create your models here.
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import signals
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
import uuid


class CricketTeam(models.Model):
    """Our Cricket Team model consisting of the basic info about the teams
    """
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    title = models.CharField(null=False,blank=False,max_length=100)
    team_logo = models.URLField(_('Team Logo'), blank=False,
                            null=False, max_length=4096)
    club_state = models.CharField(null=False,blank=False,max_length=100)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'cric'
        ordering = ['title']
        verbose_name = _('CricketTeam')

class TeamPlayers(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    first_name = models.CharField(null=False,blank=False,max_length=100)
    last_name = models.CharField(null=True,blank=True,max_length=100)
    player_image = models.URLField(_('Player Image'),blank=True,
                              null=True, max_length=4096)
    jersey_number = models.PositiveIntegerField(unique=True,blank=False,null=False)
    origin_country = models.CharField(null=False,blank=False,max_length=100)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)
    team = models.ForeignKey(CricketTeam, db_index=True, blank=True, null=True, related_name="players_team",
                                verbose_name=_('Team'),on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        "Returns the players's full name."
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        app_label = 'cric'
        ordering = ['first_name']
        verbose_name = _('TeamPlayers')


class PlayerStats(models.Model):
    player = models.ForeignKey(TeamPlayers, db_index=True, blank=False, null=False, related_name="player",
                                verbose_name=_('TeamPlayers'),on_delete=models.PROTECT)
    number_matches = models.PositiveIntegerField(blank=True,null=True)
    total_runs = models.PositiveIntegerField(_("Total Runs"),blank=True,null=True)
    total_wickets = models.PositiveIntegerField(_("Total Wickets"),blank=True,null=True)
    total_centuries = models.PositiveIntegerField(_("Total Centuries"),blank=True,null=True)
    total_fifties = models.PositiveIntegerField(_("Total Fifties"),blank=True,null=True)
    highest_score = models.PositiveIntegerField(_("Highest Score"),blank=True,null=True)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)

    class Meta:
        app_label = 'cric'
        ordering = ['number_matches']
        verbose_name = _('PlayerStats')


class MatchStats(models.Model):
    home_team = models.ForeignKey(CricketTeam, db_index=True, blank=False, null=False, related_name="home_team")
    away_team = models.ForeignKey(CricketTeam, db_index=True, blank=False, null=False, related_name="away_team")
    winner_team = models.ForeignKey(CricketTeam, db_index=True, blank=True, null=True, related_name="winners")
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)

    def save(self, *args, **kwargs):
        if self.winner_team is not None and (self.winner_team == self.home_team or self.winner_team == self.away_team):
            super().save(*args, **kwargs)
        elif self.winner_team is None:
            super().save(*args, **kwargs)
        else:
            raise ValidationError(u'Please enter a valid team')


    class Meta:
        app_label = 'cric'
        verbose_name = _('MatchStats')

def update_points(sender, instance, created,update_fields, **kwargs):
    if not created:
        team = get_object_or_404(PointsTable, team=instance.winner_team)
        team.points +=2
        team.save()
"""Signal to increment points of the winning team"""
signals.post_save.connect(receiver=update_points, sender=MatchStats)


class PointsTable(models.Model):
    team = models.OneToOneField(CricketTeam, max_length=50, related_name='point_team',on_delete=models.PROTECT)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'cric'
        ordering = ['-points']
        verbose_name = _('PointsTable')

