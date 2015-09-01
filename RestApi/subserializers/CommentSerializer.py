
from rest_framework import serializers

from RestApi.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment

