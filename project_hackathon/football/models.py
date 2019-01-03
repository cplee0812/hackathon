from __future__ import unicode_literals
from django.db import models
from django import forms
from django_auto_one_to_one import AutoOneToOneModel

# Create your models here.

class Team(models.Model):
	"""docstring for Player"""
	team_name = models.CharField(max_length=20, blank=False)
	jersey_color = models.CharField(max_length=20, blank=False, default=None)
	player_number = models.IntegerField(blank=False, default=None)
	#description = models.CharField(max_length=255, blank=False, default=None)
	jersey_image = models.FileField(upload_to='documents/',null=True)
	uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.team_name

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
	location = [
		['NTU SPN', 'NTU Sports Center(New)'],
		['NTU SPO', 'NTU Sports Center(Old)'],
		['NTU PG', 'NTU Playground'],
		['NTUST SP', 'NTUST Sports Center'],
		['NTUST PG', 'NTUST Playground']
	]
	date_Y = [
		['2019', '2019'], ['2020', '2020'], ['2021', '2021'], ['2022', '2022'], ['2023', '2023'], ['2024', '2024']
	]
	date_M = [
		['Jan', '1'], ['Feb', '2'], ['Mar', '3'], ['Apl', '4'], ['May', '5'], ['Jun', '6'],
		['Jul', '7'], ['Aug', '8'], ['Sep', '9'], ['Oct', '10'], ['Nov', '11'], ['Dec', '12']
	]
	date_D = [
		['First', '1st'], ['Second', '2nd'], ['Third', '3rd'], ['Forth', '4th'], ['Fifth', '5th'], ['Sixth', '6th'],
		['Seventh', '7th'], ['Eighth', '8th'], ['Ninth', '9th'], ['Tenth', '10th'],['Eleventh', '11th'], ['Twelfth', '12th'],
		['Thirteenth', '13th'], ['Fourteenth', '14th'], ['Fifteenth', '15th'], ['Sixteenth', '16th'], ['Seventeenth', '17th'], ['Eighteenth', '18th'],
		['Nineteenth', '19th'], ['Twentieth', '20th'], ['Twenty-first', '21st'], ['Twenty-second', '22nd'],['Twenty-third', '23rd'], ['Twenty-fourth', '24th'],
		['Twenty-fifth', '25th'], ['Twenty-sixth', '26th'], ['Twenty-seventh', '27th'], ['Twenty-eighth', '28th'],['Twenty-ninth', '29th'], ['Thirtieth', '30th'],
		['Thirty-first', '31st']
	]
	name = models.CharField(max_length=20, blank=False)
	location = models.CharField(max_length = 100, choices = location)
	date_Y = models.CharField(max_length = 100, choices = date_Y)
	date_M = models.CharField(max_length = 100, choices = date_M)
	date_D = models.CharField(max_length = 100, choices = date_D)
	starttime1 = models.TimeField(blank=False, help_text="Format:'HH:MM'")
	duration1 = models.IntegerField(blank=False, default=50)
	starttime2 = models.TimeField(blank=False, help_text="Format:'HH:MM'")
	duration2 = models.IntegerField(blank=False, default=50)
	team1 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='Home Team +')
	team2 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='Away Team +')

	def __str__(self):
		return self.name

class MatchStat(AutoOneToOneModel(Match)):
	match = models.ForeignKey(Match, on_delete=models.PROTECT)
	host_score = models.IntegerField(blank=True, default=0)
	away_score = models.IntegerField(blank=True, default=0)
