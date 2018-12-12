from django.db import models

# Create your models here.

class Team(models.Model):
	"""docstring for Player"""
	name = models.CharField(max_length=20, blank=False)

class Player(models.Model):
	"""docstring for Player"""
	name = models.CharField(max_length=20, blank=False)
	number = models.IntegerField(blank=False)
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
	score = models.IntegerField(blank=True)
