from django import forms
#from models import OrgProfile
#from models import Orgs
from organisation.models import Orgs
from django.contrib.auth.forms import UserCreationForm

class OrgProfileForm(forms.ModelForm):
    class Meta:
        model=Orgs
        fields = ('org_head','org_strength','name_of_org','latitude','longitude','tags')

