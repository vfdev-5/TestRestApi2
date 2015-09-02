# # Django
# from django.http import Http404
#
# # Rest
# from rest_framework import permissions, status, views
# from rest_framework.response import Response
#
# # Project
# from RestApi.models import Photo
# from RestApi.serializers import PhotoSerializer
#
#
# class ClientInfo(views.APIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def get(self, request, format=None):
#
#         client_id=""
#         client_secret=""
#
#         data={
#             "client_id":client_id,
#             "client_secret": client_secret
#             }
#         return Response(data=data, status=status.HTTP_200_OK)
#
#     # def post(self, request, format=None):
#     #     # print "request.data : ", request.data
#     #     data = request.data
#     #     data['owner'] = request.user.pk
#     #     serializer = PhotoSerializer(data=data)
#     #     if serializer.is_valid():
#     #         photoIntance = serializer.save(owner=request.user)
#     #         print "photoIntance : ", photoIntance
#     #         print 'serializer.validated_data : ', serializer.validated_data
#     #         # return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#     #         return Response("A photo is created", status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # def pre_save(self, obj):
#     #      print "pre_save : object = ", obj
#     #      obj.owner = self.request.user.id
#
