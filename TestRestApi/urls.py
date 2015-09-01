from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'TestRestApi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('RestApi.urls')),

    url(r'^auth/', include('rest_framework_social_oauth2.urls')),

]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
