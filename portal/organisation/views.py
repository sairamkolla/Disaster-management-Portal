from django.shortcuts import render
from django.shortcuts import render_to_response
from organisation.models import Notifications_Org
# Create your views here.

def org_home(request,org_id):
    notification=Notifications_Org.objects.all() 
    return render_to_response('org_home.html')
