from django.db import models

# Create your models here.

class Orgs(models.Model):
    person_in_charge=models.CharField(max_length=100)
    people_working=models.IntegerField(default=0)
    conta
