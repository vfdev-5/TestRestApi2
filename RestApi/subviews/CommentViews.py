# Django
from django.http import Http404

# Rest
from rest_framework import permissions, status, views
from rest_framework.response import Response

# Project
from RestApi.models import Comment
from RestApi.serializers import CommentSerializer


class CommentList(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print "request.data : ", request.data
        data = request.data
        data['owner'] = request.user.pk
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            print 'serializer.validated_data : ', serializer.validated_data
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def pre_save(self, obj):
    #      print "pre_save : object = ", obj
    #      obj.owner = self.request.user.id
