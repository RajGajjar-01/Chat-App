from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room

def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

def room(request, slug):
    room = Room.objects.get(slug=slug)

    return render(request, 'room/room.html', {'room': room})

def home(request):
    return render(request, 'chatApplication/home.html')

def landing(request):
    return render(request, 'chatApplication/landing.html')