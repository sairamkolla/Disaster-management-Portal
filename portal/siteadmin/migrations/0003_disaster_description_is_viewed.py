# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0002_acceptance_disaster_org_org_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster_description',
            name='is_viewed',
            field=models.BooleanField(default=0),
        ),
    ]
