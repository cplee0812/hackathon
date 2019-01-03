from django.shortcuts import render, redirect
from football.models import Team, Player, Match, MatchStat, broadcast_msg
import datetime
import time
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from football.forms import DocumentForm
from django import forms
# Create your views here.


def mainpage(request):

	Matches = Match.objects.all
    
	return render(request,"fb_mainpage.html",locals())

def gamepage(request, id):

	MatchStats = MatchStat.objects.get(id=id)
	nowtime = datetime.datetime.now().strftime('%H:%M:%S')
	nowtimes = str(nowtime)
	_match = MatchStats.match
	msgs = broadcast_msg.objects.filter(match = _match)
	#try:
	
	#except broadcast_msg.DoesNotExist:
		#broadcast_msg = Nones

	return render(request,"fb_gamepage.html",locals())

def edit(request, id):
	broadcast_msgs = broadcast_msg.objects.filter(id=id)
	MatchStats = MatchStat.objects.get(id=id)
	nowtimes = datetime.datetime.now().strftime('%H:%M:%S')
	msgs = broadcast_msg.objects.filter(id=id)
	return render(request, 'edit.html', locals())

def edit_msg(request, id):
	class newmsg(forms.ModelForm):
		class Meta:
			model = broadcast_msg
			fields = '__all__'	
	MatchStats = MatchStat.objects.get(id=id)
	nowtimes = datetime.datetime.now().strftime('%H:%M:%S')
	_match = MatchStats.match
	msgs = broadcast_msg.objects.filter(match = _match)
	form = newmsg()

	if request.method == 'POST':
		form = newmsg(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/fb_gamepage/%s" %id)	
	else:
		return render(request, 'edit_msg.html', locals())
	

	#broadcast_msgs = broadcast_msg.objects.filter(id=id)
	#MatchStats = MatchStat.objects.get(id=id)
	#nowtimes = datetime.datetime.now().strftime('%H:%M:%S')
	#msgs = broadcast_msg.objects.filter(id=id)

def update(request, id):
	MatchStats = MatchStat.objects.get(id=id)
	MatchStats.host_score = request.POST['host_score']
	MatchStats.away_score = request.POST['away_score']
	MatchStats.save()
	return redirect("/fb_gamepage/%s" %id)

#def update_msg(request, id): #give up using time module to count lol #ask user key in time on their own
#	_id = Match.id
#	_happenmin = request.POST.get('minnute')
#	_happensec = request.POST.get('second')
#	_message = request.POST.get('msg')
#	_happentime = str(_happenmin) + ": " + str(_happensec)
#	broadcast_msg.objects.create(happened_time = _happentime, message = _message, Match_id=_id)#, match = _id)
#	return redirect("/fb_gamepage/%s" %id)

def host_score_plus1(request, id):
	if id:
		MatchStats = MatchStat.objects.get(id=id)
		score = MatchStats.host_score
		score += 1
		MatchStats.host_score = score
		MatchStats.save()
	return redirect("/fb_gamepage/%s" %id)


def away_score_plus1(request, id):
	if id:
		MatchStats = MatchStat.objects.get(id=id)
		score = MatchStats.away_score
		score += 1
		MatchStats.away_score = score
		MatchStats.save()
	return redirect("/fb_gamepage/%s" %id)
