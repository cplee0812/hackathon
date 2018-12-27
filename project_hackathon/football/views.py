from django.shortcuts import render, redirect
from football.models import Team, Player, Match, MatchStat

# Create your views here.


def mainpage(request):

	Matches = Match.objects.all
	return render(request,"fb_mainpage.html",locals())

def gamepage(request, id):

	MatchStats = MatchStat.objects.get(id=id)

	return render(request,"fb_gamepage.html",locals())

def edit(request, id):
	MatchStats = MatchStat.objects.get(id=id)
	return render(request, 'edit.html', locals())

def update(request, id):
	MatchStats.host_score = request.POST['host_score']
	MatchStats.away_score = request.POST['away_score']
	MatchStats.save()
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
