
from rest_framework import serializers

from RestApi.models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Photo
