from django.db import models
from django.contrib.auth.models import User
#from authentication.models import Orgs
#from django.conf import settings
# Create your models here.
class Orgs(models.Model):
    #user=models.OneToOneField(User,null=True)
    userid=models.IntegerField(default=0)
    org_head=models.CharField(max_length=100)
    org_strength=models.IntegerField(default=0)
    name_of_org=models.CharField(max_length=100)
    latitude=models.CharField(max_length=15)
    longitude=models.CharField(max_length=15)
    created=models.DateTimeField(auto_now_add=True)
    tags=models.CharField(max_length=100,null=True)
    def __unicode__(self):
        return unicode(self.name_of_org)


class Contact_Numbers_Orgs(models.Model):
    org_id=models.ForeignKey(Orgs,null=True)
    contact_number=models.CharField(max_length=12)
    created=models.DateTimeField(auto_now_add=True)

class Contact_Mails_Orgs(models.Model):
    org_id=models.ForeignKey(Orgs,null=True)
    contact_mail=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)

class Address_Org(models.Model):
    org_id=models.ForeignKey(Orgs,null=True)
    street_name=models.CharField(max_length=50)
    state_name=models.CharField(max_length=20)
    door_number=models.CharField(max_length=10)
    city_name=models.CharField(max_length=20)
    pincode=models.CharField(max_length=6)
    created=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return unicode(self.org_id.name_of_org)


class Messages_Orgs(models.Model):
    sender_org_id=models.ForeignKey(Orgs,related_name="sender",null=True)
    receiver_org_id=models.ForeignKey(Orgs,related_name="receiver",null=True)
    message_content=models.CharField(max_length=256)
    created=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.message_content)

class Messages_From_Admin(models.Model):
    target_org_id=models.ForeignKey(Orgs,null=True)
    message_content=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.id)

class Notifications_Org(models.Model):
    target_org_id=models.ForeignKey(Orgs,null=True)
    is_message_from_org=models.BooleanField(default=0)
    message_from_org_id=models.ForeignKey(Messages_Orgs,null=True,blank=True)
    is_message_from_admin=models.BooleanField(default=0)
    message_from_admin_id=models.ForeignKey(Messages_From_Admin,null=True,blank=True)
    is_request_from_admin=models.BooleanField(default=0)
    disaster_id=models.ForeignKey('siteadmin.Disaster_Description',null=True,blank=True)
    is_seen=models.BooleanField(default=0)
    created=models.DateTimeField(auto_now_add=True)
