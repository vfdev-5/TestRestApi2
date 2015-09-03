from django.conf.urls import url, include

from WebSite.views import index, logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^logout/$', logout, name='logout'),
]

