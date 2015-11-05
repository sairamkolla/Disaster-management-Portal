from django.shortcuts import render
from data.serializers import *
from organisation.models import *
from authentication.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict
# Create your views here.

@api_view(['GET','POST'])
def getdisasters(request,id,disasterid):
    if request.method == 'GET':
        list_of_disasters = Disaster_Description.objects.filter(id__gt = disasterid)
        serializer = DisasterSerializer(list_of_disasters, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getmessages(request,id,messageid):
    """
    This function return a list of Ordered Dicts which has "message" "sender org name" and "timestamp of creation and id of message is greater than messageid
    """
    if request.method == 'GET':
        org = Orgs.objects.get(userid = id)
        messages = Messages_Orgs.objects.filter(receiver_org_id = org, id__gt = messageid)
        serializer = MessageSerializer(messages, many = True)
        for x in serializer.data:
            x.__setitem__("sender",Orgs.objects.get(id=x.items()[1][1]).name_of_org)
            del x['sender_org_id']
        return Response(serializer.data)

@api_view(['GET'])
def getuserid(request):
    if request.method == 'GET' :
        return Response({"id":request.user.id})

