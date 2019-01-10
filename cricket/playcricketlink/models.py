# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from cricket.core import models as coremodels

class PlayCricketLinker(models.Model):
    pc_id = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Match(PlayCricketLinker):
    match = models.ForeignKey(coremodels.Match, on_delete=models.CASCADE,
                              related_name='pc_match_link')


class Team(PlayCricketLinker):
    team = models.ForeignKey(coremodels.Team, on_delete=models.CASCADE, related_name='pc_team_link')


class Club(PlayCricketLinker):
    club = models.ForeignKey(coremodels.Club, on_delete=models.CASCADE, related_name='pc_club_link')


class Umpire(PlayCricketLinker):
    umpire = models.ForeignKey(coremodels.Umpire, on_delete=models.CASCADE,
                               related_name='pc_umpire_link')


class Scorer(PlayCricketLinker):
    scorer = models.ForeignKey(coremodels.Scorer, on_delete=models.CASCADE,
                               related_name='pc_scorer_link')


class Competition(PlayCricketLinker):
    competition = models.ForeignKey(coremodels.Competition, on_delete=models.CASCADE,
                                    related_name='pc_competition_link')


class League(PlayCricketLinker):
    league = models.ForeignKey(coremodels.Competition, on_delete=models.CASCADE,
                               related_name='pc_league_link')


class Ground(PlayCricketLinker):
    ground = models.ForeignKey(coremodels.Ground, on_delete=models.CASCADE,
                               related_name='pc_ground_link')


class Player(PlayCricketLinker):
    player = models.ForeignKey(coremodels.Player, on_delete=models.CASCADE,
                               related_name='pc_player_link')


