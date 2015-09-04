from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout as auth_logout

from social.backends.utils import load_backends
# from social.apps.django_app.utils import psa

from social.apps.django_app.default.models import UserSocialAuth

# from rest_framework_social_oauth2.authentication import SocialAuthentication


# Create your views here.
def index(request, template_name='index.html'):

    user = request.user
    print "User : ", user

    access_token = None
    if user.is_authenticated():

        # get the last login provider
        provider = request.session['social_auth_last_login_backend']
        print "provider : ", provider
        social = user.social_auth.get(provider=provider)
        print "social.extra_data : ", social.extra_data
        access_token = social.extra_data['access_token']
        print "access_token", access_token

        # print "social_auth : ", user.social_auth
        # print "social_auth.values_list('provider') : ", user.social_auth.values_list('provider')
        # print "social_auth.values_list('extra_data') : ", user.social_auth.values_list('extra_data')
        # print "social_auth.provider : ", user.social_auth.provider
        # social = user.social_auth.get(provider='google')
        # print "social : ", social
        # print "social.extra_data['access_token'] : ", social.extra_data['access_token']

    context = {
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS),
        'access_token': access_token,
    }

    return render(request, template_name, context)


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')
