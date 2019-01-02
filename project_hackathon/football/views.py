from django.shortcuts import render, redirect
from football.models import Team, Player, Match, MatchStat, broadcast_msg
import datetime
import time
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from football.forms import DocumentForm
# Create your views here.


def mainpage(request):

	Matches = Match.objects.all
    
	return render(request,"fb_mainpage.html",locals())

def gamepage(request, id):

	MatchStats = MatchStat.objects.get(id=id)
	nowtime = datetime.datetime.now().strftime('%H:%M:%S')
	nowtimes = str(nowtime)
	lis1 = list(broadcast_msg.objects.get(id=id))
	msgs = all(lis1)
	#try:
	
	#except broadcast_msg.DoesNotExist:
		#broadcast_msg = Nones

	return render(request,"fb_gamepage.html",locals())

def edit(request, id):
	MatchStats = MatchStat.objects.get(id=id)
	nowtimes = datetime.datetime.now().strftime('%H:%M:%S')
	return render(request, 'edit.html', locals())

def update(request, id):
	MatchStats.host_score = request.POST['host_score']
	MatchStats.away_score = request.POST['away_score']
	MatchStats.save()
	if request.POST['broadcasmsg']:
		_happentime = request.POST.get('time')
		_message = request.POST.get('msg')
		broadcast_msg.objects.Create(happentime = _happentime, message = _message)
	return redirect("/fb_gamepage/%s" %id)

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
