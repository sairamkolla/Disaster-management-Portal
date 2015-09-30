# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0003_disaster_description_disaster_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster_description',
            name='disaster_name',
            field=models.CharField(default='lila thuphan', max_length=20),
            preserve_default=False,
        ),
    ]
