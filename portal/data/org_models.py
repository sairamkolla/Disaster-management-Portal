from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Orgs(models.Model):
    user = models.ForeignKey(User)
    org_head = models.CharField(max_length=100)
    org_strength = models.IntegerField(default=0)
    name_of_org = models.CharField(max_length=100)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    created = models.DateTimeField(default=datetime.datetime.now())
    tags = models.CharField(max_length=100, null=True)

    # hosp,pol,fire,ngo
    def __unicode__(self):
        return unicode(self.name_of_org)


class ContactNumbersOrgs(models.Model):
    org = models.ForeignKey(Orgs)
    contact_number = models.CharField(max_length=12)
    created = models.DateTimeField(default=datetime.datetime.now())


class ContactMailsOrgs(models.Model):
    org = models.ForeignKey(Orgs)
    contact_mail = models.CharField(max_length=50)
    created = models.DateTimeField(default=datetime.datetime.now())


class AddressOrgs(models.Model):
    org = models.ForeignKey(Orgs)
    street_name = models.CharField(max_length=50)
    state_name = models.CharField(max_length=20)
    door_number = models.CharField(max_length=10)
    city_name = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    created = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return unicode(self.org.name_of_org)


class MessagesOrgs(models.Model):
    sender_org = models.ForeignKey(Orgs, related_name="sender")
    receiver_org = models.ForeignKey(Orgs, related_name="receiver")
    message_content = models.CharField(max_length=256)
    created = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return unicode(self.message_content)


class MessagesFromAdmin(models.Model):
    target_org = models.ForeignKey(Orgs)
    message_content = models.CharField(max_length=500)
    created = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return unicode(self.id)

# class Notifications_Org(models.Model):
#    target_org=models.ForeignKey(Orgs)
#    is_message_from_org=models.BooleanField(default=0)
#    message_from_org=models.ForeignKey(Messages_Orgs,null=True,blank=True)
#    is_message_from_admin=models.BooleanField(default=0)
#    message_from_admin_id=models.ForeignKey(Messages_From_Admin,null=True,blank=True)
#    is_request_from_admin=models.BooleanField(default=0)
#    disaster_id=models.ForeignKey('siteadmin.Disaster_Description',null=True,blank=True)
#    is_seen=models.BooleanField(default=0)
#    created=models.DateTimeField(auto_now_add=True)
