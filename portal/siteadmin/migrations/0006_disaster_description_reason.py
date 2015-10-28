# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0005_auto_20150930_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster_description',
            name='reason',
            field=models.CharField(default='Just kidding dude', max_length=200),
            preserve_default=False,
        ),
    ]
