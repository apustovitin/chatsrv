from .models import *
from rest_framework import serializers

class PublicChatRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublicChatRoom
        fields = ['title', 'id', ]
