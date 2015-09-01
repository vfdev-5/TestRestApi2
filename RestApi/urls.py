from django.conf.urls import url

from rest_framework.authtoken import views

from RestApi.views import PhotoList, PhotoDetail, CommentList
from RestApi.views import UserDetail, UserList, TestView

urlpatterns = [
    url(r'^$', TestView.index, name='test'),
    url(r'^auth-token/', views.obtain_auth_token),
    url(r'^comment/$', CommentList.as_view(), name='comment-list'),
    url(r'^photo/$', PhotoList.as_view(), name='photo-list'),
    url(r'^photo/(?P<pk>[0-9]+)/$', PhotoDetail.as_view(), name='photo-detail'),
    url(r'^user/$', UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
]
