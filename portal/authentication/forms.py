from django import forms
from models import *

class OrgProfileform(forms.ModelForm):
    class Meta:
        model=OrgProfile
        exclude = ('user',)
