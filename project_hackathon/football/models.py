from django.db import models
    
    
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

<<<<<<< HEAD
=======
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
>>>>>>> 71f748676a819045b5446a20c508ee4d10b5be63
