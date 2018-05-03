from django import forms
from django.contrib.auth.models import User, Group
from .models import Room
from . import models

class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = [
            'name',
            'uid',
            'owner',
            'users',
        ]