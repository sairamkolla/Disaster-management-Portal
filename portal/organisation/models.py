from django.db import models

# Create your models here.

class Orgs(models.Model):
    person_in_charge=models.CharField(max_length=100)
    people_working=models.IntegerField(default=0)
    name_of_org=models.CharField(max_length=100)
    latitude=models.CharField(max_length=15)
    longitude=models.CharField(max_length=15)


class Contact_Numbers_Orgs(models.Model):
    org_id=models.ForeignKey(Orgs)
    contact_number=models.CharField(max_length=12)

class Contact_Mails_Orgs(models.Model):
    org_id=models.ForeignKey(Orgs)
    contact_mail=models.CharField(max_length=50)

#class Name_Orgs(models.Model):
#    org_id=models.ForeignKey(Orgs)
#    name=models.CharField(max_length=100)

class Address_Org(models.Model):
    org_id=models.ForeignKey(Orgs)
    street_name=models.CharField(max_length=50)
    state_name=models.CharField(max_length=20)
    door_number=models.CharField(max_length=10)
    city_name=models.CharField(max_length=20)
    pincode=models.CharField(max_length=6)

class Messages_Orgs(models.Model):
    sender_org_id=models.ForeignKey(Orgs,related_name="sender")
    receiver_org_id=models.ForeignKey(Orgs,related_name="receiver")
    message_content=models.CharField(max_length=256)

class Messages_From_Admin(models.Model):
    target_org_id=models.ForeignKey(Orgs)
    message_content=models.CharField(max_length=500)

class Notifications_Org(models.Model):
    target_org_id=models.ForeignKey(Orgs)
    is_message_from_org=models.BooleanField(default=0)
    message_from_org_id=models.ForeignKey(Messages_Orgs)
    is_message_from_admin=models.BooleanField(default=0)
    message_from_admin_id=models.ForeignKey(Messages_From_Admin)
    is_request_from_admin=models.BooleanField(default=0)
    disaster_id=models.IntegerField()     ######################################  should make disasters app
    created=models.DateTimeField(auto_now_add=True)


