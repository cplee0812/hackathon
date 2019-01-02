"""project_hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from football import views as fb_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/',views.logout),
    path('gamepage/', views.gamepage),
    path('teampage/', views.teampage),
    path('personalpage/', views.personalpage),
    path('create/', views.create),
    path('football_page/',fb_views.mainpage),
    url(r'fb_gamepage/(?P<id>\d+)$', fb_views.gamepage),
    path('basketball_page/', views.basketball_mainpage),
    path('basketball_gamepage/', views.basketball_gamepage),
    path('volleyball_gamepage/',views.volleyball_gamepage),
    path('volleyball_mainpage/',views.volleyball_mainpage),
    #path('', include('sendemail.urls')),
    path('email/',views.email),
    path('success/',views.email),
    path('check/', views.check),
    url(r'edit/(?P<id>\d+)$', fb_views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', fb_views.update, name='update'),
    url(r'^edit/host_score_plus1/(?P<id>\d+)$', fb_views.host_score_plus1, name='host_score_plus1'),
    url(r'^edit/away_score_plus1/(?P<id>\d+)$', fb_views.away_score_plus1, name='away_score_plus1'),
]
