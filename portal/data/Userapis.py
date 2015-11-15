from data.serializers import *
from models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework import status
import json
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from forms import OrgProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
@api_view(['POST'])
def login(request):
    if request.user.username:
        return Response({"response":"AlreadyLoggedIn :) "})
    else:
        if request.method == 'POST':
	        username=request.POST.get('username','')
	        password=request.POST.get('password','')
	        user=auth.authenticate(username=username,password=password)
	        if user is not None:
		        auth.login(request,user)
		        return Response({"response":"LoggedIn SucessFully :) "})
	        else:
		        return Response({"response":"Provided Credentials are incorrect  :) "})

@api_view(['POST'])
def fill_profile(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        head = str(postdata['OrganisationHead'])
        strength = str(postdata['OrganisationStrength'])
        name = str(postdata['OrganisationName'])
        lati = str(postdata['latitude'])
        longi = str(postdata['longitude'])
        tagfield = str(postdata['tags'])

        orgsdetails = Org(user = request.user, org_head = head, org_strength = strength, name_of_org = name, latitude = lati, longitude = longi, tags = tagfield)
        orgsdetails.save()
        return Response({"response":"Registration sucessfull"})

@api_view(['POST'])
def register(request):
	if request.method =='POST':
	    form = UserCreationForm(request.POST)
	    if form.is_valid():
		user = form.save()
                user = auth.authenticate(username=request.POST['username'],
                            password=request.POST['password1'])
                auth.login(request, user)
		return HttpResponseRedirect('/accounts/fill_profile/')
	else:
	    form = UserCreationForm()

	return render_to_response('authentication/register.html', {
            'form': form,
	},context_instance=RequestContext(request))


@login_required
def logout(request):
    auth.logout(request)
    return Response({"response":"Logout Sucessfull"})
