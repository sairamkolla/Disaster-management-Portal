from rest_framework import serializers
from organisation.models import *
from siteadmin.models import *

### Organisation related serializers start here

class OrgProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgs
        fields= ("userid","org_head","org_strength","name_of_org","latitude","longitude","tags")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages_Orgs
        fields = ("id","sender_org_id","message_content","created")


###### Admin related serializers start here

class DisasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disaster_Description
        fields = ("id","created","disaster_name","disaster_code","reason","no_people_affected","latitude","longitude")
class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disaster_Description
        fields = ("id","created","disaster_name","disaster_code","reason","no_people_affected","latitude","longitude")