
print '----- Test shell scripts ------'

from rest_framework.response import Response
from rest_framework import status

from RestApi.serializers import CommentSerializer
from RestApi.models import Comment
from django.contrib.auth.models import User

comments = Comment.objects.all()
print 'comments : ', comments

users = User.objects.all()
print 'users : ', users

data = {"comment": "test comment 3", "owner": users[1].pk}

serializer = CommentSerializer(data=data)
print serializer.is_valid()

if not serializer.is_valid():
    print serializer.errors
else:
    commentInstance = serializer.save(owner=users[1])
    print "commentInstance : ", commentInstance
    print "serializer.validated_data : ", serializer.validated_data
    print Response(serializer.validated_data, status=status.HTTP_201_CREATED)






