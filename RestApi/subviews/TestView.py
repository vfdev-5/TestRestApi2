# Django
from django.shortcuts import render

#######################################################################################################################
# Test view
#######################################################################################################################

def index(request, template_name='test.html'):

    context = {
    }

    return render(request, template_name, context)




