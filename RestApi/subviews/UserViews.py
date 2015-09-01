from django.contrib.auth.models import User
from django.http import Http404

# Rest
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

# Project
from RestApi.serializers import UserSerializer


class UserList(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        return Response(data={}, status=status.HTTP_200_OK)



class UserDetail(views.APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)