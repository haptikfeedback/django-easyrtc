from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
]