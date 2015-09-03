from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout as auth_logout

from social.backends.utils import load_backends
from social.apps.django_app.utils import psa


# Create your views here.
def index(request, template_name='index.html'):

    context = {
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }

    return render(request, template_name, context)


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')


@psa("social:complete")
def get_social_access_token():
    print "get_social_access_token"
    pass