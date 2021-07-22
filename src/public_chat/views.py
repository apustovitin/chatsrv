from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from public_chat.serializers import *
from public_chat.models import *


class PublicChatRoomViewset(viewsets.ModelViewSet):
    queryset = PublicChatRoom.objects.all()
    serializer_class = PublicChatRoomSerializer
