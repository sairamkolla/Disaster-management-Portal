from data.serializers import *
from models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework import status
import json
# Create your views here.

@api_view(['GET','POST'])
def GetApprovedDisasters(request,id,di4sasterid):
    if request.method == 'GET':
        list_of_disasters = DisasterDescription.objects.filter(id__gt = disasterid)
        serializer = DisasterSerializer(list_of_disasters, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def GetNotApprovedDisasters(request,disasterid):
    if request.method == 'GET':
        list_of_disasters = DisasterProposal.objects.filter(id__gt = disasterid, is_viewed=False)
        serializer = ProposalSerializer(list_of_disasters, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def Approval(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        sample = DisasterProposal.objects.get(id = int(postdata['disasterid']))
        sample.is_viewed = True
        if int(postdata['opinion']) == 1:
            disaster = DisasterDescription(no_people_affected = sample.no_people_affected,latitude = sample.latitude, longitude = sample.longitude,disaster_code = sample.disaster_code, disaster_name = sample.disaster_name,reason = sample.reason)
            sample.is_confirmed = True
            disaster.save()
        sample.save()
        return Response({"response":"created"},status=status.HTTP_201_CREATED)

@api_view(['GET'])
def GetMessages(request,id,messageid):
    """
    This function return a list of Ordered Dicts which has "message" "sender org name" and "timestamp of creation and id of message is greater than messageid
    """
    if request.method == 'GET':
        org = Orgs.objects.get(user__id = id)
        messages = MessagesOrgs.objects.filter(receiver_org = org, id__gt = messageid)
        serializer = MessageSerializer(messages, many = True)
        for x in serializer.data:
            x.__setitem__("sender",Orgs.objects.get(id=x.items()[1][1]).name_of_org)
            del x['sender_org']
        return Response(serializer.data)


@api_view(['POST','PUT'])
def Test(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        message = Messages_Orgs(sender_org__user__id=5,receiver_org__user__id=int(postdata['receiver_org']),message_content = str(postdata['message_content']))
        message.save()
        return Response({"response":"Message is created"},status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def GetOrgList(request):
    """
    :param request: keyword,istag
    :return:
    """
    if request.method == 'POST':
        postdata = json.loads(request.body)
        keyword = str(postdata['keyword'])
        is_tag = int(postdata['istag'])
        if is_tag == 1 :
            org_list = Orgs.objects.filter(tags__contains =keyword)
        else :
            org_list = Orgs.objects.filter(name_of_org__contains = keyword)
        serializer = OrgListSerializer(org_list, many = True)
    return Response(serializer.data)

