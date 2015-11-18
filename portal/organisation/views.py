from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def OrgHome(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('organisation/org_home1.html',args)

def OrgProfile(request):
    return render_to_response('organisation/orgprofile1.html')

@api_view(['GET'])
def GetUserId(request):
    if request.method == 'GET' :
        return Response({"id":request.user.id})

def orgsearch(request):
    return render_to_response('organisation/orgsearch1.html')
