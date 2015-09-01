from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'images', 'comments')

