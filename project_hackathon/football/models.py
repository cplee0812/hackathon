from django.db import models
<<<<<<< HEAD
    
    
=======
from django import forms

# Create your models here.

>>>>>>> e6cb70234114918acf93a8e42d0451b5e1c0af8d
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
<<<<<<< HEAD
	score = models.IntegerField(blank=True)
    
#class match_imfo(models.Model):
    #game_num = models.IntegerField()
    #game_starttime = models.DateTimeField()

        #兩個starttime，兩個endtime，
    #game_place = models.CharField(max_length)

    #def __init__(self):
        #return self.game_num


#class gamelog(models.Model):
        
    #score = 


    #class livebroadcast(models.Model):
        



    # Create your models here.


# Create your models here.    
=======

	def __str__(self):
		return self.name

class MatchStat(models.Model):
	match = models.ForeignKey(Match, on_delete=models.PROTECT)
	host_score = models.IntegerField(blank=True)
	away_score = models.IntegerField(blank=True)
>>>>>>> e6cb70234114918acf93a8e42d0451b5e1c0af8d
