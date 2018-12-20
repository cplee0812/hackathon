from django.db import models
from django.conf import settings

# Create your models here.

class Create_The_Game(models.Model):
	Type = models.CharField(max_length = 50, blank = False)
	Date = models.CharField(max_length = 50, blank = False)
	Number = models.CharField(max_length = 50, blank = False)
	default_pos = models.CharField(max_length = 50, blank = False)
	pos = models.CharField(max_length = 100, blank = True)
	Host_Name = models.CharField(max_length = 100, blank = False)
	Host_ID = models.CharField(max_length = 20, blank = False)
	Host_Phone_Number = models.CharField(max_length = 20, blank = False)
	def __str__(self):
		return self.Type + " " + self.Date + " " + self.Number + " " + self.default_pos + " " + self.pos + " " + self.Host_Name + " " + self.Host_ID + " " + self.Host_Phone_Number

class test(models.Model):
	test1 = models.CharField(max_length = 10, blank = False)
		
