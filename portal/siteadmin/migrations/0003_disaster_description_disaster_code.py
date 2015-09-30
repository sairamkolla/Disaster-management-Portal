# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0002_acceptance_disaster_org_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster_description',
            name='disaster_code',
            field=models.CharField(default='NA', max_length=2),
            preserve_default=False,
        ),
    ]
