from django.shortcuts import render

# Create your views here.


def mainpage(request):

    return render(request,"fb_mainpage.html",locals())

def gamepage(request):

    return render(request,"fb_gamepage.html",locals())