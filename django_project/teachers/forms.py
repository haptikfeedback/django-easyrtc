from django import forms
from django.contrib.auth.models import User, Group
from rooms.models import Room
from rooms import models

class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = [
            'name',
            # 'uid',
            # 'owner',
            # 'user' = request.user,
        ]
