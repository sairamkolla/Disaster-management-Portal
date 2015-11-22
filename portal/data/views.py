from django.shortcuts import render
from data.serializers import *
from models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework import status
import json
import twitter
from django.contrib import auth
# Create your views here.
@api_view(['POST'])
def testfillprofile(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        print postdata
        OrganisationName = str(postdata['OrganisationName'])
        OrganisationStrength = int(postdata['OrganisationStrength'])
        OrganisationHead = str(postdata['OrganisationHead'])
        lat  = float(postdata['latitude'])
        lon = float(postdata['longitude'])
        Tags = str(postdata['Tags'])

        neworg = Orgs(userid = request.user.id,org_head = OrganisationHead,org_strength = OrganisationStrength,name_of_org = OrganisationName,latitude = lat,longitude = lon,tags = Tags)
        neworg.save()
        return Response({'response':'redirect to home page','ok':'1'})
    return Response({'ok':'1'})

@api_view(['POST'])
def testfillcredentials(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        print postdata
        name = str(postdata['username'])
        pass1 = str(postdata['password'])
        pass2 = str(postdata['password1'])

        if not len(User.objects.filter(username = name)) == 0:
            return Response({'error':'Username already Exists'})
        if not pass1 == pass2:
            return Response({'error':'Passwords Dont match!!'})

        newuser = User(username = name , password = pass1)
        user = newuser.save()

        user = auth.authenticate(username = name,password = pass2)
        if user is not None:
            auth.login(request, user)
            print "Sucessfully authenticated"
            return Response({"response": user.id})
        else:
            return Response({"response": "Provided Credentials are incorrect  :) "})

    return Response({'ok':'1'})



@api_view(['POST'])
def SearchTwitter(request):
    keyword = str(json.loads(request.body)['keyword'])
    testapi = twitter.Api('x3xggt7CsLflL2iOZBz1boHWe', 'HmnXcaWuSHxArxuB2CM4e82wjQ3LW3OoD1EqxMGIzCWogb6Der',
                     '298409124-5z7ySh9PcgTHuxyOF0AfeffMcatr0ZyfYpl8pQDp', 'RWimzN4VDcL1otBr9Tv27JomemIxYQMNlgHRDXWl7iCmq')
    r = testapi.GetSearch(term=keyword,count=200)#,result_type='recent')

    json_results = [result.AsDict() for result in r]
    #print json_results.media
    return Response(json_results)

@api_view(['GET','POST'])
def getapproveddisasters(request,id,disasterid):
    if request.method == 'GET':
        list_of_disasters = DisasterDescription.objects.filter(id__gt = disasterid)
        serializer = DisasterSerializer(list_of_disasters, many=True)
        for disaster in serializer.data :
            x = DecisionsOrgs.objects.filter(org = Orgs.objects.get(userid = id) , disaster = DisasterDescription.objects.get(id = disaster.items()[0][1]))
            if len(x) == 1 :
                disaster.__setitem__("value",x[0].is_accepted)
            else:
                disaster.__setitem__("value",2)
        return Response(serializer.data)

@api_view(['GET','POST'])
def getnotapproveddisasters(request,disasterid):
    if request.method == 'GET':
        list_of_disasters = DisasterProposal.objects.filter(id__gt = disasterid, is_viewed=False)
        serializer = ProposalSerializer(list_of_disasters, many=True)
        return Response(serializer.data)
@api_view(['POST'])
def approval(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        #print int(a['disasterid'])
        #print int(a['opinion'])
        sample = DisasterProposal.objects.get(id = int(a['disasterid']))
        sample.is_viewed = True
        if int(a['opinion']) == 1:
            disaster = DisasterDescription(no_people_affected = sample.no_people_affected,latitude = sample.latitude, longitude = sample.longitude,disaster_code = sample.disaster_code, disaster_name = sample.disaster_name,reason = sample.reason)
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

        messages = MessagesOrgs.objects.filter(receiver_org_id = org, id__gt = messageid)
        serializer = MessageSerializer(messages, many = True)
        for x in serializer.data:
            x.__setitem__("sender",Orgs.objects.get(id=x.items()[1][1]).name_of_org)
            del x['sender_org']
        return Response(serializer.data)
@api_view(['POST','PUT'])
def CreateMessage(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        print "hello here"

        message = MessagesOrgs(sender_org=Orgs.objects.get(userid=request.user.id),receiver_org=Orgs.objects.get(userid=int(a['receiver'])),message_content = str(a['messagecontent']))
        #print int(request.POST.get('receiver_org_id',False))

        message.save()
        return Response({"response":"created"},status=status.HTTP_201_CREATED)
@api_view(['POST'])
def getorglist(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        keyword = str(a['keyword'])
        if 'tag' in a.keys():
            org_list = Orgs.objects.filter(tags__contains =keyword)
        else:
            org_list = Orgs.objects.filter(name_of_org__contains =keyword)

        serializer = OrgProfileSerializer(org_list, many = True)
        print serializer.data
    return Response(serializer.data)

@api_view(['POST'])
def DecisionOrgs(request):
    postdata = json.loads(request.body)
    disasterid = int(postdata['disasterid'])
    id = int(postdata['userid'])
    decision = int(postdata['decision'])
    if len(DecisionsOrgs.objects.filter(disaster = DisasterDescription.objects.filter(id = disasterid),org = Orgs.objects.get(userid = id))) == 1:
        print "exists"
        new=0
    else:
        print "new"
        new=1

    if decision == 1 :
        if new == 1:
            x = DecisionsOrgs(disaster = DisasterDescription.objects.get(id = disasterid),org = Orgs.objects.get(userid = id),is_accepted = True)
        else:
            x = DecisionsOrgs.objects.filter(disaster = DisasterDescription.objects.filter(id = disasterid),org = Orgs.objects.get(userid = id))[0]
            x.is_accepted = True
    else :
        if new == 1:
            x = DecisionsOrgs(disaster = DisasterDescription.objects.get(id = disasterid),org = Orgs.objects.get(userid = id),is_accepted = False)
        else:
            x = DecisionsOrgs.objects.filter(disaster = DisasterDescription.objects.filter(id = disasterid),org = Orgs.objects.get(userid = id))[0]
            x.is_accepted = False
    x.save()
    return Response({"response":"successfull"})

@api_view(['GET','POST'])
def GetUserDetails(request):
    if request.method == 'GET':
        orgdetails = Orgs.objects.get(userid = request.user.id)
        serializer = OrgProfileSerializer(orgdetails)
        return Response(serializer.data)

# Api's made for admin

@api_view(['GET'])
def AdminStatistics(request):
    TotalManPower = 0
    for org in Orgs.objects.all():
        TotalManPower += org.org_strength
    TotalDisasters = len(DisasterProposal.objects.all())
    Fake = len(DisasterProposal.objects.filter(is_viewed = True,is_confirmed = False))
    Original = len(DisasterProposal.objects.filter(is_viewed = True,is_confirmed = True))
    TotalOrgs = len(Orgs.objects.all())
    Hospitals = len(Orgs.objects.filter(tags__contains = 'hospital'))
    Fire = len(Orgs.objects.filter(tags__contains = 'fire'))
    Ngo = len(Orgs.objects.filter(tags__contains = 'ngo'))
    Police = len(Orgs.objects.filter(tags__contains = 'police'))

    return Response({"TotalManPower":TotalManPower,"TotalDisasters":TotalDisasters,"Fake":Fake,"Original":Original,"TotalOrgs":TotalOrgs,"Hospitals":Hospitals,"Fire":Fire,"Ngo":Ngo,"Police":Police})


@api_view(['POST','GET'])
def GetAcceptedDisasters(request):
    print json.loads(request.body)
    userid = json.loads(request.body)['userid']
    accepted = DecisionsOrgs.objects.filter(org__userid = userid ,is_accepted =1 ).values_list('disaster_id',flat=True)
    disasters = DisasterDescription.objects.filter(id__in = accepted)
    serializer = DisasterSerializer(disasters,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def NotGetAcceptedDisasters(request):

    userid = json.loads(request.body)['userid']
    notaccepted = DecisionsOrgs.objects.filter(org__userid = userid,is_accepted =0 ).values_list('disaster_id',flat=True)
    disasters = DisasterDescription.objects.filter(id__in = notaccepted)
    serializer = DisasterSerializer(disasters,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def NotOpinionDisasters(request):

    userid = json.loads(request.body)['userid']
    opinion = DecisionsOrgs.objects.filter(org__userid = userid).values_list('disaster_id',flat=True)
    disasters = DisasterDescription.objects.exclude(id__in = opinion)
    serializer = DisasterSerializer(disasters,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def GetAcceptedOrgs(request):
    print json.loads(request.body)
    disasterid = json.loads(request.body)['disasterid']
    accepted = DecisionsOrgs.objects.filter(disaster__id = disasterid,is_accepted =1 ).values_list('org__userid',flat=True)
    orgslist = Orgs.objects.filter(userid__in = accepted)
    serializer = OrgProfileSerializer(orgslist,many=True)
    return Response(serializer.data)


@api_view(['POST','GET'])
def NotGetAcceptedOrgs(request):
    print json.loads(request.body)
    disasterid = json.loads(request.body)['disasterid']
    notaccepted = DecisionsOrgs.objects.filter(disaster__id = disasterid,is_accepted =0 ).values_list('org__userid',flat=True)
    orgslist = Orgs.objects.filter(userid__in = notaccepted)
    serializer = OrgProfileSerializer(orgslist,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def NotOpinionOrgs(request):

    disasterid = json.loads(request.body)['disasterid']
    opinion = DecisionsOrgs.objects.filter(disaster__id = disasterid).values_list('org__userid',flat=True)
    orgslist = Orgs.objects.exclude(userid__in = opinion)
    serializer = OrgProfileSerializer(orgslist,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def getdisasterlist(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        keyword = str(a['keyword'])
        if 'code' in a.keys():
            disaster_list = DisasterDescription.objects.filter(disaster_code__contains =keyword)
        else:
            disaster_list = DisasterDescription.objects.filter(disaster_name__contains =keyword)

        serializer = DisasterSerializer(disaster_list, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def AddNumber(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        new = ContactNumbersOrgs(org=Orgs.objects.get(userid = int(postdata['userid'])),contact_number = str(postdata['number']))
        new.save()
        return Response({"response":"created"})

@api_view(['POST'])
def AddEmail(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        new = ContactMailsOrgs(org=Orgs.objects.get(userid = int(postdata['userid'])),contact_mail = str(postdata['email']))
        new.save()
        return Response({"response":"created"})

@api_view(['POST'])
def GetNumbers(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        numbers = ContactNumbersOrgs.objects.filter(org__userid = int(postdata['userid']))
        serializer = ContactNumberSerializer(numbers,many = True)
        return Response(serializer.data)


@api_view(['POST'])
def GetEmails(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        mails = ContactMailsOrgs.objects.filter(org__userid = int(postdata['userid']))
        serializer = ContactMailSerializer(mails,many = True)
        return Response(serializer.data)