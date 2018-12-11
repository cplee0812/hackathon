from django.db import models


    class match_imfo(models.Model):
        game_num = models.IntegerField()
        game_starttime = models.DateTimeField()

        #兩個starttime，兩個endtime，
        game_place = models.CharField()

        def __init__(self):
            return self.game_num


    class gamelog(models.Model):
        
        score = 


    #class livebroadcast(models.Model):
        



    # Create your models here.

