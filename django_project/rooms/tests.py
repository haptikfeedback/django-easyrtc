from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User



from .models import Room
# Create your tests here.
class RoomModelTest(TestCase):
    room = Room.objects.create(
        name = "Test Room",
        uid = "12345678",
        owner = admin,
        user = admin,
    )
    now = timezone.now()
    self.assertLess(room.created_at, now)