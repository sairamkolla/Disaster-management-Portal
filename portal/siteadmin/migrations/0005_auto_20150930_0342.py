# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0004_disaster_description_disaster_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptance_disaster_org',
            name='is_accepted',
            field=models.IntegerField(default=0),
        ),
    ]
