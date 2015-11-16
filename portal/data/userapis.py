from models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json


@api_view(['POST'])
def login(request):
    if request.user.username:
        return Response({"response": "AlreadyLoggedIn :) "})
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response({"response": request.user.id})
            else:
                return Response({"response": "Provided Credentials are incorrect  :) "})



@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        message = "Registration Successful!!"
        # checking validity here

        ok = 1

        try:
            name = str(postdata['OrganisationName'])
        except:
            message = "Please enter Valid Organisation Name"
            return Response({"response": message})

        if len(Orgs.objects.filter(name_of_org=name)):
            message = "An Organisation with the given name is already registered."
            return Response({"response": message})

        try:
            head = str(postdata['OrganisationHead'])
        except:
            message = "Please enter a Valid Organisation Head name"
            return Response({"response": message})

        try:
            strength = str(postdata['OrganisationStrength'])
        except:
            message = "Please enter Valid Organisation Strength"
            return Response({"response": message})

        try:
            lati = str(postdata['latitude'])
        except:
            message = "Please enter Valid Latitude"
            return Response({"response": message})

        try:
            longi = str(postdata['longitude'])
        except:
            message = "Please enter Valid Longitude"
            return Response({"response": message})

        try:
            tagfield = str(postdata['tags'])
        except:
            message = "Please enter fire,police,ngo or hospital only"
            return Response({"response": message})
        ok = 1
        if not str(postdata['password']) == str(postdata['password1']):
            ok = 0
            message = "Passwords Didnot Match.Try Again"
            return Response({"response": message})

        if len(User.objects.get(username=str(postdata['username']))):
            message = "User with same username exists.Try another Username"
            ok = 0
            return Response({"response": message})

        # validity check ends
        if ok == 1:
            message = "Registration is successfull"
            user = User(username=str(postdata['username']), password=str(postdata['password1']))
            user.save()
            user = auth.authenticate(username=postdata['username'],
                                     password=postdata['password1'])
            auth.login(request, user)
            orgsdetails = Orgs(user=user, org_head=head, org_strength=strength, name_of_org=name, latitude=lati,
                               longitude=longi, tags=tagfield)
            orgsdetails.save()
        return Response({"response": message})


@login_required
@api_view(['GET'])
def logout(request):
    auth.logout(request)
    return Response({"response": "Logout Sucessfull"})
