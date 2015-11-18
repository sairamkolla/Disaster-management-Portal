from django import forms
from models import *
class OrgProfileForm(forms.ModelForm):
    class Meta:
        model=Orgs
        fields = ('org_head','org_strength','name_of_org','latitude','longitude','tags')