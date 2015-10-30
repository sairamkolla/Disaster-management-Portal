from django import forms
#from models import OrgProfile
from models import Orgs
from django.contrib.auth.forms import UserCreationForm

class OrgProfileForm(forms.ModelForm):
    class Meta:
        model=Orgs
        fields = ('org_head','org_strength','name_of_org','latitude','longitude','tags')

class TestUserReg(UserCreationForm):
    org_head=forms.CharField(max_length=100)
    org_strength=forms.IntegerField()
    name_of_org=forms.CharField(max_length=100)
    latitude=forms.CharField(max_length=15)
    longitude=forms.CharField(max_length=15)
    created=forms.DateTimeField()
    tags=forms.CharField(max_length=100)

    fields = ('username','org_head','org_strength','name_of_org','latitude','longitude','tags')

    def save(self,commit=True):
        user=super(TestUserReg,self).save(commit=False)
        user.org_head = self.cleaned_data['org_head']
        user.org_strength = self.cleaned_data['org_strength']
        user.name_of_org = self.cleaned_data['name_of_org']
        user.latitude = self.cleaned_data['latitude']
        user.longitude = self.cleaned_data['longitude']
        tags = self.cleaned_data['tags']
        
        if commit:
            user.save()

        return user
