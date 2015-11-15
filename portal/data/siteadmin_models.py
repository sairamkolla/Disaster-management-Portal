from django.db import models
import datetime


# Create your models here.

class DisasterDescription(models.Model):
    no_of_sos_received = models.IntegerField(default=0)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    created = models.DateTimeField(default=datetime.datetime.now())
    disaster_code = models.CharField(max_length=2)
    disaster_name = models.CharField(max_length=20)
    reason = models.CharField(max_length=200)
    no_people_affected = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.disaster_name)


class DisasterProposal(models.Model):
    no_of_sos_received = models.IntegerField(default=0)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    is_confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.datetime.now())
    disaster_code = models.CharField(max_length=2)
    disaster_name = models.CharField(max_length=20)
    reason = models.CharField(max_length=200)
    no_people_affected = models.IntegerField(default=0)
    is_viewed = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.disaster_name)


class DecisionsOrgs(models.Model):
    disaster = models.ForeignKey(DisasterDescription)
    is_accepted = models.IntegerField(default=0)
    seen = models.BooleanField(default=False)
    org = models.ForeignKey('org_models.Orgs')
    created = models.DateTimeField(default=datetime.datetime.now())


class SosReports(models.Model):
    disaster_code = models.CharField(max_length=2)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    sos_timestamp = models.DateTimeField(default=datetime.datetime.now())
    is_disaster = models.BooleanField(default=0)
    disaster = models.ForeignKey(DisasterDescription)


class DisasterApprovalAdmin(models.Model):
    disaster = models.ForeignKey(DisasterDescription)
    is_visited = models.BooleanField(default=0)
