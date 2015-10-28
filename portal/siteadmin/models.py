from django.db import models
# Create your models here.

class Disaster_Description(models.Model):
    no_of_sos_received=models.IntegerField(default=0)
    latitude=models.CharField(max_length=15)
    longitude=models.CharField(max_length=15)
    is_confirmed=models.BooleanField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    disaster_code=models.CharField(max_length=2)
    disaster_name=models.CharField(max_length=20)
    reason=models.CharField(max_length=200)
    no_people_affected=models.IntegerField(default=0)
    #approved_timestamp=DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.disaster_name)

class Acceptance_Disaster_Org(models.Model):
    disaster_id=models.ForeignKey(Disaster_Description)
    is_accepted=models.IntegerField(default=0)
    seen=models.BooleanField(default=False)
    org_id=models.ForeignKey('organisation.Orgs')
    created=models.DateTimeField(auto_now_add=True)
    #accepted_timestamp=DateTimeField(auto_now_add=True)

#class Messages_From_Admin(models.Model):
#    target_org_id=models.ForeignKey(Orgs)
#    message_content=models.CharField(max_length=100)
#    created=models.DateTimeField(auto_now_add=True)
    #seen_timestamp=DateTimeField(auto_now_add=True)

class Sos_Reports(models.Model):
    disaster_code=models.CharField(max_length=2)
    latitude=models.CharField(max_length=15)
    longitude=models.CharField(max_length=15)
    sos_timestamp=models.DateTimeField(auto_now_add=True)
    is_disaster=models.BooleanField(default=0)
    disaster_id=models.ForeignKey(Disaster_Description,null=True,blank=True)

class Disaster_Approval_Admin(models.Model):
    disaster_id=models.ForeignKey(Disaster_Description)
    is_visited=models.BooleanField(default=0)
    


