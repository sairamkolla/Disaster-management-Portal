from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from forms import CreateDisasterform
from organisation.models import Orgs,Notifications_Org
from siteadmin.models import Disaster_Description,Acceptance_Disaster_Org
# Create your views here.

def admin_home(request):
    return render_to_response('admin_home.html')

def create_disaster(request):
    if request.POST:
        form = CreateDisasterform(request.POST)
        if form.is_valid:
            a=form.save()
            return HttpResponseRedirect('/siteadmin/notify_orgs/%s/' % a.id)
    else:
        form = CreateDisasterform()
        args={}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('make_disaster.html',args)
def notify_orgs_disaster(request,disaster_id):
    organisations = Orgs.objects.all()
    disaster=Disaster_Description.objects.get(id=disaster_id)
    for organisation in organisations:
        form=Notifications_Org(target_org_id=organisation,is_request_from_admin=1,disaster_id=disaster)
        form.save()
        form=Acceptance_Disaster_Org(disaster_id=disaster,org_id=organisation)
        form.save()
    
    return HttpResponseRedirect('/siteadmin/')
def disaster_orgs(request):
    requests=Acceptance_Disaster_Org.objects.all()
    disasters=Disaster_Description.objects.all()
    args={}
    args['requests']=requests
    args['disasters']=disasters
    return render_to_response('disaster_orgs.html',args)
