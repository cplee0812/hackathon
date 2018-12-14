from django.db import models
from django import forms

# Create your models here.

class Team(models.Model):
	"""docstring for Player"""
	name = models.CharField(max_length=20, blank=False)
	contact = models.CharField(max_length=20, blank=False, default=None)

	def __str__(self):
		return self.name

class Player(models.Model):
	"""docstring for Player"""
	name = models.CharField(max_length=20, blank=False)
	number = models.IntegerField(blank=False)
	is_captain = models.BooleanField(blank=False, default=False)
	team = models.ForeignKey(Team, on_delete=models.PROTECT)

#	def __init__(self, arg):
#		super(Player, self).__init__()
#		self.arg = arg

class Match(models.Model):
	"""docstring for Player"""
	name = models.CharField(max_length=20, blank=False)
	starttime1 = models.TimeField(blank=False)
	duration1 = models.IntegerField(blank=False)
	starttime2 = models.TimeField(blank=False)
	duration2 = models.IntegerField(blank=False)
	team1 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='Home Team +')
	team2 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='Away Team +')

	def __str__(self):
		return self.name

class MatchStat(models.Model):
	match = models.ForeignKey(Match, on_delete=models.PROTECT)
	host_score = models.IntegerField(blank=True)
	away_score = models.IntegerField(blank=True)
