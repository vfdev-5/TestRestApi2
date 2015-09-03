# Django
from django.shortcuts import render

#######################################################################################################################
# Test view
#######################################################################################################################

def index(request, template_name='test.html'):

    print "Test html"
    print "Test html : request.user : ", request.user

    # print "user.social_auth : ", request.user.social_auth

    context = {
    }

    return render(request, template_name, context)




