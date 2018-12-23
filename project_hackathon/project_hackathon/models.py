from django.db import models

# Create your models here.

"""class Player(models.Model):
	"""docstring for Player"""
	name = models.CharField(max_length=20, blank=False)
	number = models.InteferField(blank=False)
	team = models.ForeignKey(Team)
#	def __init__(self, arg):
#		super(Player, self).__init__()
#		self.arg = arg

class Team(models.Model):
	"""docstring for Player"""
	name = models.CharField(max_length=20, blank=False)

class Match(models.Model):
	"""docstring for Player"""
	name = models.CharField(max_length=20, blank=False)
	starttime1 = models.TimeField(blank=False)
	duration1 = models.InteferField(blank=False)
	starttime2 = models.TimeField(blank=False)
	duration2 = models.InteferField(blank=False)
	team1 = models.ForeignKey(Team)
	team2 = models.ForeignKey(Team)
	score = models.InteferField()"""
