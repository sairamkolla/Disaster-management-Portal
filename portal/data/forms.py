from django import forms
from models import *
class OrgProfileForm(forms.ModelForm):
    class Meta:
        model=Orgs
        fields = ('org_head','org_strength','name_of_org','latitude','longitude','tags')

class DisasterProposalForm(forms.ModelForm):
    class Meta:
        model = DisasterProposal
        exclude = ('is_confirmed','is_viewed')