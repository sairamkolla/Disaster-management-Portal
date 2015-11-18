from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
# Create your views here.
def SiteAdminHome(request):
    """
        This function renders homepage of admin
    """
    return render_to_response('siteadmin/disasters.html')

def CreateDisaster(request):
    """
        This function Creates a disaster and redirects to another function to send requests
    """
    return render_to_response('make_disaster.html')
#def notify_orgs_disaster(request,disaster_id):
#    """
#    This function sends requests to selected organisations in time of a disaster
#    """
#   organisations = Orgs.objects.all()
#    disaster=Disaster_Description.objects.get(id=disaster_id)
#    for organisation in organisations:
#        form=Notifications_Org(target_org_id=organisation,is_request_from_admin=1,disaster_id=disaster)
#        form.save()
#        form=Acceptance_Disaster_Org(disaster_id=disaster,org_id=organisation)
#        form.save()
    
    return HttpResponseRedirect('/siteadmin/')

def Organisations(request):
    return render_to_response('siteadmin/organisations.html')

def Information(request):
    return render_to_response('siteadmin/organisations_view.html')
