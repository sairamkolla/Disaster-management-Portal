from django.db import models


# Create your models here.

class Orgs(models.Model):
    userid = models.IntegerField(default=0)
    org_head = models.CharField(max_length=100)
    org_strength = models.IntegerField(default=0)
    name_of_org = models.CharField(max_length=100)
    latitude = models.CharField(max_length=35)
    longitude = models.CharField(max_length=35)
    created = models.DateTimeField(auto_now_add = True)
    tags = models.CharField(max_length=100, null=True)
    profilecolor = models.CharField(max_length=7,default="#030303")
    # hosp,pol,fire,ngo
    def __unicode__(self):
        return unicode(self.name_of_org)


class ContactNumbersOrgs(models.Model):
    org = models.ForeignKey(Orgs)
    contact_number = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add = True)


class ContactMailsOrgs(models.Model):
    org = models.ForeignKey(Orgs)
    contact_mail = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add = True)


class AddressOrgs(models.Model):
    org = models.ForeignKey(Orgs)
    street_name = models.CharField(max_length=50)
    state_name = models.CharField(max_length=20)
    door_number = models.CharField(max_length=10)
    city_name = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return unicode(self.org.name_of_org)


class MessagesOrgs(models.Model):
    sender_org = models.ForeignKey(Orgs, related_name="sender")
    receiver_org = models.ForeignKey(Orgs, related_name="receiver")
    message_content = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return unicode(self.message_content)


class MessagesFromAdmin(models.Model):
    target_org = models.ForeignKey(Orgs)
    message_content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add = True)

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


# site admin models starts from here

class DisasterDescription(models.Model):
    no_of_sos_received = models.IntegerField(default=0)
    latitude = models.CharField(max_length=35)
    longitude = models.CharField(max_length=35)
    created = models.DateTimeField(auto_now_add = True)
    disaster_code = models.CharField(max_length=2)
    disaster_name = models.CharField(max_length=20)
    reason = models.CharField(max_length=200)
    no_people_affected = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.disaster_name)


class DisasterProposal(models.Model):
    no_of_sos_received = models.IntegerField(default=0)
    latitude = models.CharField(max_length=35)
    longitude = models.CharField(max_length=35)
    is_confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)
    disaster_code = models.CharField(max_length=2)
    disaster_name = models.CharField(max_length=20)
    reason = models.CharField(max_length=200,default = "NotKnown")
    no_people_affected = models.IntegerField(default=0)
    is_viewed = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.disaster_name)


class DecisionsOrgs(models.Model):
    disaster = models.ForeignKey(DisasterDescription)
    is_accepted = models.IntegerField(default=0)
    org = models.ForeignKey(Orgs)
    created = models.DateTimeField(auto_now_add = True)


class SosReports(models.Model):
    disaster_code = models.CharField(max_length=2)
    latitude = models.CharField(max_length=35)
    longitude = models.CharField(max_length=35)
    sos_timestamp = models.DateTimeField(auto_now_add = True)
    is_disaster = models.BooleanField(default=0)
    disaster = models.ForeignKey(DisasterDescription)


class DisasterApprovalAdmin(models.Model):
    disaster = models.ForeignKey(DisasterDescription)
    is_visited = models.BooleanField(default=0)
