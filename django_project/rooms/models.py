from django.db import models
import uuid
from django.contrib.auth.models import User, Group
from django.conf import settings

# Create your models here.
def create_uid():
    return str(uuid.uuid4())[:8]

class Room(models.Model):
    name = models.CharField(max_length=128)
    uid = models.CharField(max_length=8, default=create_uid(), editable=False, primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_rooms', on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rooms', blank=True)
    def __str__(self):
        return (f'Teacher: {self.owner} // Room#:{self.uid}')

