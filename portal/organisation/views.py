from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render_to_response
from forms import Messageform, Notificationform
#from organisation.models import Notifications_Org, Messages_Orgs, Contact_Mails_Orgs, Contact_Numbers_Orgs
from organisation.models import Notifications_Org, Messages_Orgs, Contact_Mails_Orgs, Contact_Numbers_Orgs, Orgs
#from authentication.models import Orgs
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from siteadmin.models import Acceptance_Disaster_Org, Disaster_Description
from rest_framework.decorators import api_view
from organisation.serializers import *
from rest_framework.response import Response
# Create your views here.

def org_home(request):
    notifications=Notifications_Org.objects.filter(target_org_id=Orgs.objects.get(userid=request.user.id))
    present_org=Orgs.objects.get(userid=request.user.id)
    args={}
    disasters=Disaster_Description.objects.all()
    args.update(csrf(request))
    messages=Messages_Orgs.objects.filter(receiver_org_id=Orgs.objects.get(userid=request.user.id))
    args['form']=Messageform()
    args['messages']=messages
    args['disasters']=disasters
    args['notifications']=notifications
    args['present_org']=present_org
    return render_to_response('organisation/maintrail.html',args)

def create_message_org(request):
    if request.POST:
        form=Messageform(request.POST)
        if form.is_valid:
            a=form.save(commit=False)
            a.sender_org_id=Orgs.objects.get(userid=request.user.id)
            a.save()
            ##### Message is stored into database now #####
            send=a.sender_org_id
            receive=a.receiver_org_id
            message=a.message_content
            mm=Notifications_Org(target_org_id=receive,is_message_from_org=1,message_from_org_id=a)
            ##### A notification for the receiver is  created now #####
            mm.save()
            return HttpResponseRedirect('/')
def profile(request):
    org=Orgs.objects.get(userid=request.user.id)
    args={}
    args['org']=org
    contact_numbers=Contact_Numbers_Orgs.objects.filter(org_id=Orgs.objects.get(userid=request.user.id))
    args['contact_numbers']=contact_numbers
    contact_mails=Contact_Mails_Orgs.objects.filter(org_id=Orgs.objects.get(userid=request.user.id))
    args['contact_mails']=contact_mails
    args['username']=request.user.username
    return render_to_response('organisation/orgprofiletrail.html',args)

@api_view(['GET','POST'])
def getdisasters(request):
    if request.method == 'GET' :
        return Response({"id":request.user.id})
    if request.method == 'GET':
        list_of_orgs = Orgs.objects.all()
        serializer = OrganisationSerializer(list_of_orgs, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def test(request):
    if request.method == 'GET' :
        return Response({"id":request.user.id})
def best(request):
    args={}
    args['id']=request.user.id
    return render_to_response('organisation/test.html',args)

