from django import forms
from models import *

class CreateDisasterform(forms.ModelForm):
    class Meta:
        model=Disaster_Proposal
        exclude = ('is_confirmed','created','is_viewed')
