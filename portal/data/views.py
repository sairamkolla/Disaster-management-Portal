from django.shortcuts import render
from data.serializers import *
from organisation.models import *
from authentication.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework import status
import json
# Create your views here.

@api_view(['GET','POST'])
def getapproveddisasters(request,id,disasterid):
    if request.method == 'GET':
        list_of_disasters = Disaster_Description.objects.filter(id__gt = disasterid)
        serializer = DisasterSerializer(list_of_disasters, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def getnotapproveddisasters(request,disasterid):
    if request.method == 'GET':
        list_of_disasters = Disaster_Proposal.objects.filter(id__gt = disasterid, is_viewed=False)
        serializer = ProposalSerializer(list_of_disasters, many=True)
        return Response(serializer.data)
@api_view(['POST'])
def approval(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        #print int(a['disasterid'])
        #print int(a['opinion'])
        sample = Disaster_Proposal.objects.get(id = int(a['disasterid']))
        sample.is_viewed = True
        if int(a['opinion']) == 1:
            disaster = Disaster_Description(no_people_affected = sample.no_people_affected,latitude = sample.latitude, longitude = sample.longitude,disaster_code = sample.disaster_code, disaster_name = sample.disaster_name,reason = sample.reason)
            sample.is_confirmed = True
            disaster.save()
        sample.save()
        return Response({"response":"created"},status=status.HTTP_201_CREATED)

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
@api_view(['POST','PUT'])
def test(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        message = Messages_Orgs(sender_org_id=Orgs.objects.get(userid=5),receiver_org_id=Orgs.objects.get(userid=int(a['receiver_org_id'])),message_content = str(a['message_content']))
        #print int(request.POST.get('receiver_org_id',False))

        message.save()
        return Response({"response":"created"},status=status.HTTP_201_CREATED)
@api_view(['POST'])
def getorglist(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        keyword = str(a['keyword'])
        org_list = Orgs.objects.filter(tags__contains =keyword)
        serializer = OrgListSerializer(org_list, many = True)
    return Response(serializer.data)

