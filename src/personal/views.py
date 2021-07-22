from django.shortcuts import render, redirect
from django.conf import settings

DEBUG = True

def chats_screen_view(request, *args, **kwargs):
	context = {}
	context['debug_mode'] = settings.DEBUG
	context['debug'] = DEBUG
	context['room_id'] = kwargs.get("room_id")
	return render(request, "personal/chats.html", context)

def home_screen_view(request):
	context = {}
	context['debug_mode'] = settings.DEBUG
	context['debug'] = DEBUG
	return render(request, "personal/home.html", context)
