# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0003_notifications_org_is_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='tags',
            field=models.CharField(default='We always chill', max_length=100),
            preserve_default=False,
        ),
    ]
