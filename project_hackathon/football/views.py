from django.shortcuts import render
from football.models import broadcast_msg
from football.models import Match
from datetime import datetime
import time
# Create your views here.


def mainpage(request):

    return render(request,"fb_mainpage.html",locals())

def gamepage(request):

    if request.method == 'POST':
        nowtime = datetime.datetime.nowtime()
        starttime = request.Match.starttime1
        time = (nowtime - starttime).minutes
        _message = request.POST.get('msg')
        broadcast_msg.objects.create(happened_time=time, message=_message)
		
    msgs = broadcast_msg.objects.all()

    return render(request,"fb_gamepage.html",locals())