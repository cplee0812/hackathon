from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

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
