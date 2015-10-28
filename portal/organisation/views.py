from django.shortcuts import render
from django.shortcuts import render_to_response
from forms import Messageform, Notificationform
from organisation.models import Notifications_Org, Orgs, Messages_Orgs, Contact_Mails_Orgs, Contact_Numbers_Orgs
from django.contrib import messages
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from siteadmin.models import Acceptance_Disaster_Org, Disaster_Description
# Create your views here.

#def org_home(request,org_id):
def org_home(request):
    #notifications=Notifications_Org.objects.filter(target_org_id=Orgs.objects.get(id=org_id))
    notifications=Notifications_Org.objects.filter(target_org_id=Orgs.objects.get(user=request.user))
    #present_org=Orgs.objects.get(id=org_id)
    present_org=Orgs.objects.get(user=request.user)
    args={}
    disasters=Disaster_Description.objects.all()
    args.update(csrf(request))
    #messages=Messages_Orgs.objects.filter(receiver_org_id=Orgs.objects.get(id=org_id))
    messages=Messages_Orgs.objects.filter(receiver_org_id=Orgs.objects.get(user=request.user))
    args['form']=Messageform()
    args['messages']=messages
    args['disasters']=disasters
    args['notifications']=notifications
    args['present_org']=present_org
    return render_to_response('organisation/maintrail.html',args)

#def create_message_org(request,org_id):
def create_message_org(request):
    if request.POST:
        form=Messageform(request.POST)
        if form.is_valid:
            a=form.save(commit=False)
            #a.sender_org_id=Orgs.objects.get(id=org_id)
            a.sender_org_id=Orgs.objects.get(user=request.user)
            a.save()
            ##### Message is stored into database now #####
            send=a.sender_org_id
            receive=a.receiver_org_id
            message=a.message_content
            mm=Notifications_Org(target_org_id=receive,is_message_from_org=1,message_from_org_id=a)
            ##### A notification for the receiver is  created now #####
            mm.save()
            return HttpResponseRedirect('/')
            #return HttpResponseRedirect('/orgs/get/%s' % org_id)
def profile(request):
    #org=Orgs.objects.get(id=org_id)
    org=Orgs.objects.get(user=request.user)
    args={}
    args['org']=org
    #contact_numbers=Contact_Numbers_Orgs.objects.filter(org_id=Orgs.objects.get(id=org_id))
    contact_numbers=Contact_Numbers_Orgs.objects.filter(org_id=Orgs.objects.get(user=request.user))
    args['contact_numbers']=contact_numbers
    #contact_mails=Contact_Mails_Orgs.objects.filter(org_id=Orgs.objects.get(id=org_id))
    contact_mails=Contact_Mails_Orgs.objects.filter(org_id=Orgs.objects.get(user=request.user))
    args['contact_mails']=contact_mails
    args['username']=request.user.username
    return render_to_response('organisation/orgprofiletrail.html',args)
