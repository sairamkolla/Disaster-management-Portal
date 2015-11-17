# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0003_auto_20151117_0652'),
        ('siteadmin', '0004_auto_20151112_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acceptance_disaster_org',
            name='disaster_id',
        ),
        migrations.RemoveField(
            model_name='acceptance_disaster_org',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='disaster_approval_admin',
            name='disaster_id',
        ),
        migrations.DeleteModel(
            name='Disaster_Proposal',
        ),
        migrations.RemoveField(
            model_name='sos_reports',
            name='disaster_id',
        ),
        migrations.DeleteModel(
            name='Acceptance_Disaster_Org',
        ),
        migrations.DeleteModel(
            name='Disaster_Approval_Admin',
        ),
        migrations.DeleteModel(
            name='Disaster_Description',
        ),
        migrations.DeleteModel(
            name='Sos_Reports',
        ),
    ]
