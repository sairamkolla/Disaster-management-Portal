# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_auto_20150929_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications_org',
            name='is_seen',
            field=models.BooleanField(default=0),
        ),
    ]
