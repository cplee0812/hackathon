from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.template import loader
from django.conf.urls.static import static
from football.models import Team, Player, Match, MatchStat, broadcast_msg
from datetime import datetime
import time
# Create your views here.


def mainpage(request):

    return render(request,"fb_mainpage.html",locals())

def gamepage(request):

    if request.method == 'POST':
        nowtime = datetime.now()#.strftime('%H:%M:%S')
        starttime = #request.Match.starttime1#.strftime('%H:%M:%S')
        time = (nowtime - starttime).seconds
        _message = request.POST.get('msg')
        broadcast_msg.objects.create(happened_time=nowtime, message=_message)
		
    msgs = broadcast_msg.objects.all()

    return render(request,"fb_gamepage.html",locals())