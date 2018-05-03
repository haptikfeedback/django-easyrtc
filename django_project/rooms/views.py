from .models import Room
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from .decorators import group_required


def index(request):
    return render(request, 'home.html') 

@login_required
def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if room in request.user.rooms.all():
        return render(request, 'rooms/multiparty.html',{'room':room})
    else:
        return redirect("index")

@login_required
def user_room_list(request):
    rooms = request.user.rooms.all()
    users = User.objects.all()
    return render(request, "accounts/user_room_list.html", {'rooms': rooms, 'users': users})

@group_required(['teacher'])
def techer_room_list(request):
    rooms = request.user.rooms.all()
    return render(request, "accounts/user_room_list.html", {'rooms': rooms})



