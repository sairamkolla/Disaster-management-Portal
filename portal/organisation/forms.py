from django import forms
from models import *

class Messageform(forms.ModelForm):
    class Meta:
        model=Messages_Orgs
        exclude = ('sender_org_id',)
class Notificationform(forms.ModelForm):
    class Meta:
        model=Notifications_Org
        fields=('target_org_id','is_message_from_org','message_from_org_id','is_message_from_admin','message_from_admin_id','is_request_from_admin','disaster_id')
