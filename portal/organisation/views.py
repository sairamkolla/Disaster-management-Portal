from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render_to_response
from forms import Messageform, Notificationform
#from organisation.models import Notifications_Org, Messages_Orgs, Contact_Mails_Orgs, Contact_Numbers_Orgs
#from authentication.models import Orgs
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from organisation.serializers import *
from rest_framework.response import Response
# Create your views here.

def org_home(request):
    args = {}
    args.update(csrf(request))
    messages=Messages_Orgs.objects.filter(receiver_org_id=Orgs.objects.get(userid=request.user.id))
    args['form']=Messageform()
    args['present_org']=present_org
    return render_to_response('organisation/maintrail.html',args)
@api_view(['GET'])
def getuserid(request):
    if request.method == 'GET' :
        return Response({"id":request.user.id})


