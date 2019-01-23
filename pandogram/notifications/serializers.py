from rest_framework import serializers
from . import models
from pandogram.users import serializers as user_serializer
from pandogram.images import serializers as image_serializer


class NotificationSerializer(serializers.ModelSerializer):

    creator = user_serializer.ListUserSerializer()
    image = image_serializer.SmallImageSerializer()

    class Meta:
        model = models.Notification
        fields = '__all__'
