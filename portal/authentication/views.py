from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from data.models import *
from data.forms import OrgProfileForm


def login(request):
    if request.user.username:
        return HttpResponseRedirect('/orgs/home/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/orgs/home/')
            else:
                return HttpResponseRedirect('/accounts/invalid/')
        else:
            c = {}
            c.update(csrf(request))
            return render_to_response('authentication/login.html', c)


@api_view(['POST', 'GET'])
def testlogin(request):
    if request.user.username:
        if request.method == 'GET':
            return render_to_response('authentication/logintest.html')
        return Response({"response": "AlreadyLoggedIn :) "})

    else:
        if request.method == 'POST':
            print request.body
            postdata = json.loads(request.body)
            username = str(postdata['username'])
            password = str(postdata['password'])
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                print "Sucessfully authenticated"
                return Response({"response": user.id})
            else:
                return Response({"response": "Provided Credentials are incorrect  :) "})
        elif request.method == 'GET':
            return render_to_response('authentication/logintest.html')


def fill_profile(request):
    if request.method == 'POST':
        form = OrgProfileForm(request.POST)
        if form.is_valid:
            a = form.save(commit=False)
            a.userid = request.user.id
            a.save()

            return HttpResponseRedirect('/')
    else:
        form = OrgProfileForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('authentication/fill_profile.html', args)


def invalid(request):
    if request.user.username:
        return HttpResponseRedirect('/')
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('authentication/invalid.html', c)


def register(request):
    if request.user.username:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
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
            }, context_instance=RequestContext(request))


@login_required
def logout(request):
    auth.logout(request)
    return redirect('authentication.views.login')
