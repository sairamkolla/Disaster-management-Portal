from django.shortcuts import render
from django.shortcuts import render_to_response
from forms import Messageform, Notificationform
from organisation.models import Notifications_Org, Orgs
from django.contrib import messages
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
# Create your views here.

def org_home(request,org_id):
    notifications=Notifications_Org.objects.filter(target_org_id=org_id)
    present_org=Orgs.objects.get(id=org_id)
    args={}
    args.update(csrf(request))
    args['notifications']=notifications
    args['org_id']=org_id
    args['present_org']=present_org
    return render_to_response('org_home.html',args)

def message_org(request,org_id):
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

