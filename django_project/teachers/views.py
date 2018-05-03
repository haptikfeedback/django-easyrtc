from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from rooms.models import Room
from . import models
from . import forms
from rooms.decorators import group_required


# Create your views here.
@group_required('teacher')
def add_member(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.user == room.owner:
        user = get_object_or_404(User, pk=request.POST["user_id"])
        room.users.add(user)
        return redirect('edit_room', pk=room.pk)

@group_required('teacher')
def remove_member(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.user == room.owner:    
        user = get_object_or_404(User, pk=request.POST["user_id"])
        room.users.remove(user)
        return redirect('edit_room', pk=room.pk)
        
@group_required('teacher')
def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    users = User.objects.exclude(rooms__in=[room])
    if request.user == room.owner:
        return render(request, "teacher/edit_room.html", {'room': room, 'users': users})

@group_required('teacher')
def create_room(request):
    if request.method == "POST":
        form = forms.RoomForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.owner = request.user
            model_instance.save()
            return redirect('/')
    else:
        form = forms.RoomForm()
        return render(request, "teacher/create_room.html", {'form': form})