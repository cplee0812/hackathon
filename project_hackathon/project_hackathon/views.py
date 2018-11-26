from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.template import loader

def homepage(request):

	return render(request, 'homepage.html', locals())

def register(request):

	return render(request, 'register.html',locals())

def login(request):

	return render(request, 'login.html',locals())

def gamepage(request):

	return render(request, 'gamepage.html',locals())

def teampage(request):

	return render(request, 'teampage.html',locals())

def personalpage(request):

	return render(request, 'personalpage.html',locals())

def big_month(i):
	return (i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12)

def create(request):
	date = []
	member = []
	position = ["NTU Sport Center", "NTU Sport Center (new)", "Sports Field", "Others"]
	template = loader.get_template('create.html')
	for i in range(12):
		for j in range(31):
			if(i == 1):
				if(j < 28):
					date.append("2019/2/" + str(j + 1))
			elif(big_month(i + 1)):
				date.append("2019/" + str(i + 1) + '/' + str(j + 1))
			else:
				if(j < 30):
					date.append("2019/" + str(i + 1) + '/' + str(j + 1))
	for i in range(20):
		member.append(i + 1)
	context = {"dates" : date, "members" : member, "positions" : position}
	return HttpResponse(template.render(context, request))