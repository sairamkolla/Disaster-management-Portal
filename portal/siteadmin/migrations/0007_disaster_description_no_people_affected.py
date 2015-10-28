# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0006_disaster_description_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster_description',
            name='no_people_affected',
            field=models.IntegerField(default=0),
        ),
    ]
