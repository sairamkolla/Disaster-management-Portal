from django.shortcuts import render
from django.shortcuts import render_to_response
from organisation.models import Notifications_Org
# Create your views here.

def org_home(request,org_id):
    notifications=Notifications_Org.objects.filter(target_org_id=org_id)
    args={}
    args['notifications']=notifications
    return render_to_response('org_home.html',args)
