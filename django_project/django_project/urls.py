"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rooms.views import index, room_detail, user_room_list
from teachers.views import add_member, edit_room, remove_member, create_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('room/<str:pk>', room_detail, name='room_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('user/rooms', user_room_list, name='user_room_list'),
    path('teacher/add_member/<str:pk>', add_member, name='add_member'),
    path('teacher/remove_member/<str:pk>', remove_member, name='remove_member'),
    path('teacher/edit/create_room', create_room, name="create_room"),
    path('teacher/edit/<str:pk>', edit_room, name='edit_room'),
]
