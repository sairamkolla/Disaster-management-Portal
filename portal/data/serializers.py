from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

### Organisation related serializers start here

class OrgProfileSerializer(serializers.ModelSerializer):
    orgname = serializers.CharField(source='name_of_org')
    orghead = serializers.CharField(source='org_head')
    orgstrength = serializers.CharField(source='org_strength')
    username = serializers.SerializerMethodField('fetchusername')
    since = serializers.SerializerMethodField('timeconvert')
    def fetchusername(self,obj):
        return User.objects.get(id = obj.userid).username

    def timeconvert(self,object):
        return object.created.strftime("%B %d, %Y ")


    class Meta:
        model = Orgs
        fields= ("userid","orghead","orgstrength","orgname","latitude","longitude","tags","username","since")


class OrgListSerializer(serializers.ModelSerializer):
    orgname = serializers.CharField(source='name_of_org')
    class Meta:
        model = Orgs
        fields= ("userid","orgname")

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesOrgs
        fields = ("id","sender_org","message_content","created")


###### Admin related serializers start here

class DisasterSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField('timeconvert')

    def timeconvert(self,object):
        return object.created.strftime("%B %d, %Y,%I %p ")

    class Meta:
        model = DisasterDescription
        fields = ("id","created","disaster_name","disaster_code","reason","no_people_affected","latitude","longitude")
class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterDescription
        fields = ("id","created","disaster_name","disaster_code","reason","no_of_sos_received","latitude","longitude")
