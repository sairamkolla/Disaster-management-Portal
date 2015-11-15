from rest_framework import serializers
from org_models import *
from siteadmin_models import *


# Organisation related serializers start here

class OrgProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgs
        fields = ("user", "org_head", "org_strength", "name_of_org", "latitude", "longitude", "tags")


class OrgListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgs
        fields = ("id", "name_of_org")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesOrgs
        fields = ("id", "sender_org", "message_content", "created")


# Admin related serializers start here

class DisasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterDescription
        fields = ("id", "created", "disaster_name", "disaster_code", "reason",
                  "no_people_affected", "latitude", "longitude"
                  )


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterDescription
        fields = (
            "id", "created", "disaster_name", "disaster_code", "reason", "no_people_affected", "latitude", "longitude")
