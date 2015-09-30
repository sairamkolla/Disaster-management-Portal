from django import forms
from models import *

class CreateDisasterform(forms.ModelForm):
    class Meta:
        model=Disaster_Description
        exclude = ('is_confirmed','created')
