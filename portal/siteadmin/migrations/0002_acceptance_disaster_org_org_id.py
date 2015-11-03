# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0001_initial'),
        ('siteadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptance_disaster_org',
            name='org_id',
            field=models.ForeignKey(to='organisation.Orgs', null=True),
        ),
    ]
