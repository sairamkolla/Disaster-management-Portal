from rest_framework import serializers
from organisation.models import *
from django.contrib.auth.models import User
#from authentication.models import Orgs
class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgs
        fields= ("userid","org_head","org_strength","name_of_org","latitude","longitude","tags")

