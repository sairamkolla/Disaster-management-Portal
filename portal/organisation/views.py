from django.shortcuts import render
from django.shortcuts import render_to_response
from forms import Messageform, Notificationform
from organisation.models import Notifications_Org, Orgs, Messages_Orgs
from django.contrib import messages
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from siteadmin.models import Acceptance_Disaster_Org, Disaster_Description
# Create your views here.

def org_home(request,org_id):
    notifications=Notifications_Org.objects.filter(target_org_id=Orgs.objects.get(id=org_id))
    present_org=Orgs.objects.get(id=org_id)
    args={}
    args.update(csrf(request))
    args['notifications']=notifications
    args['org_id']=org_id
    args['present_org']=present_org
    return render_to_response('org_home.html',args)

def create_message_org(request,org_id):
    if request.POST:
        form=Messageform(request.POST)
        if form.is_valid:
            a=form.save(commit=False)
            a.sender_org_id=Orgs.objects.get(id=org_id)
            a.save()
            ##### Message is stored into database now #####
            send=a.sender_org_id
            receive=a.receiver_org_id
            message=a.message_content
            mm=Notifications_Org(target_org_id=receive,is_message_from_org=1,message_from_org_id=a)
            ##### A notification for the receiver is  created now #####
            mm.save()
            return HttpResponseRedirect('/orgs/get/%s' % org_id)
    else:
        form=Messageform()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['org_id']=org_id
    return render_to_response('create_message.html',args)
def view_message_from_org(request,message_id,org_id):
   message=Messages_Orgs.objects.get(id=message_id)
   args={}
   args['message'] = message
   args['org_id'] = org_id
   return render_to_response('view_message_from_org.html',args)

def view_disaster_org(request,disaster_id,org_id):
    args={}
    args['org_id'] = org_id
    yes=Acceptance_Disaster_Org.objects.filter(disaster_id=Disaster_Description.objects.get(id=disaster_id),org_id=Orgs.objects.get(id=org_id))
    if len(yes) :
        yes = yes[0].is_accepted
    args['disaster'] = Disaster_Description.objects.get(id=disaster_id)
    args['yes'] = yes
    return render_to_response('view_disaster_org.html',args)

def aod(request,disaster_id,org_id,decision):
    x=Acceptance_Disaster_Org.objects.filter(disaster_id=Disaster_Description.objects.get(id=disaster_id),org_id=Orgs.objects.get(id=org_id))[0].id
    m=Acceptance_Disaster_Org.objects.get(id=x)
    m.seen=1
    if decision :
        m.is_accepted = 1
    else:
        m.is_accepted = 0
    m.save()
    return HttpResponseRedirect('/orgs/view_disaster_org/%s/%s/' %(disaster_id,org_id))
def profile(request,org_id):
    org=Orgs.objects.get(id=org_id)
    args={}
    args['org']=org
    return render_to_response('profile.html',args)
