from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^', include('WebSite.urls') ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('RestApi.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
